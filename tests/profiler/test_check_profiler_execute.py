import lackey
from re_tests_plugin import *
import firebird.driver as fdb

def test_check_profiler_execute(open_connection):
    lackey.click("tab_query_editor_text.png")
    lackey.type("CREATE TABLE TEST (")
    lackey.type("{ENTER}")
    lackey.type("{TAB}")
    lackey.type("TEST BIGINT)")
    lackey.click("icon_profiler_execute.png")
    result1 = lackey.exists("icon_profiler_select.png")
    lackey.click("discard.png")
    lackey.click("icon_cross.png")
    lackey.type("a", lackey.Key.CTRL)
    lackey.type("{BACKSPACE}")
    with fdb.connect("employee") as con:
        con.execute_immediate("DROP TABLE TEST;")
        con.commit()
    assert result1 != None