import lackey
from re_tests_plugin import *
from . import create_duplicate_compare, disconnect_delete_duplicate
def test_check_comparer_SQL(open_connection):
    create_duplicate_compare()
    result1 = lackey.exists("text_Comparing_Finish.png")
    lackey.click("text_SQL.png")
    result2 = lackey.exists("text_SET_blue.png")
    lackey.click("icon_cross.png")
    disconnect_delete_duplicate()
    assert result1 != None
    assert result2 != None