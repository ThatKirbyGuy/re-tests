import lackey
from re_tests_plugin import *
import firebird.driver as fdb
import time

def check_membership():
        with fdb.connect("employee") as con:
            cur = con.cursor()
            cur.execute("select rdb$user, rdb$privilege, rdb$grant_option, rdb$relation_name from RDB$USER_PRIVILEGES where rdb$user='TEST_USER';")
            result = cur.fetchone()
            cur.close()
        return result

def action(type):
    with fdb.connect("employee") as con:
        if type == "USER":
            con.execute_immediate("CREATE USER TEST_USER PASSWORD 'pass';")
        else:
            con.execute_immediate("CREATE ROLE TEST_USER;")
        con.execute_immediate("CREATE ROLE ATEST_ROLE;")
        con.commit()
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("tab_membership.png")
    if type == "ROLE":
        lackey.click("checkbox_empty.png")
    loc = lackey.exists("text_TEST_USER.png").getTarget().right(200)
    lackey.click(loc)
    lackey.click("bt_grant_role.png")
    time.sleep(0.5)
    result1 = check_membership()
    lackey.click(loc)
    lackey.click("bt_grant_role_with_admin_option.png")
    time.sleep(0.5)
    result2 = check_membership()
    lackey.click(loc)
    lackey.click("bt_revoke_role.png")
    time.sleep(0.5)
    result3 = check_membership()
    lackey.rightClick("tab_user_manager_blue.png")
    lackey.click("bt_tab_close.png")
    with fdb.connect("employee") as con:
        con.execute_immediate(f"DROP {type} TEST_USER;")
        con.execute_immediate("DROP ROLE ATEST_ROLE;")
        con.commit()
    assert result1 == ('TEST_USER                                                      ', 'M     ', 0, 'ATEST_ROLE                                                     ')
    assert result2 == ('TEST_USER                                                      ', 'M     ', 2, 'ATEST_ROLE                                                     ')
    assert result3 == None

def test_check_membership_role_to_user(open_connection):
    action("USER")
    
def test_check_membership_role_to_role(open_connection):
    action("ROLE")