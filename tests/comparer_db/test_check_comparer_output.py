import lackey
from re_tests_plugin import *
from . import create_duplicate_compare, disconnect_delete_duplicate
def test_check_comparer_output(open_connection):
    create_duplicate_compare()
    result1 = lackey.exists("text_Comparing_Finish.png")
    lackey.click("text_Output.png")
    result2 = lackey.exists("text_Tables_to_DROP.png")
    lackey.click("text_Tables_to_DROP.png")
    while lackey.exists("text_Tables_to_CREATE.png") == None:
        lackey.wheel(lackey.Mouse.WHEEL_UP, 1)
    result3 = lackey.exists("text_Tables_to_CREATE.png")
    while lackey.exists("text_Tables_to_ALTER.png") == None:
        lackey.wheel(lackey.Mouse.WHEEL_DOWN, 1)
    result4 = lackey.exists("text_Tables_to_ALTER.png")
    lackey.click("icon_cross.png")
    disconnect_delete_duplicate()
    assert result1 != None
    assert result2 != None
    assert result3 != None
    assert result4 != None