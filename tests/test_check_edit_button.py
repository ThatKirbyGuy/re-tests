from unittest import result

import lackey
from re_tests_plugin import *

def test_check_edit_button():
    lackey.click("tools.png")
    lackey.click("tab_user_manager.png")
    lackey.click("bt_connect.png")
    lackey.click("bt_OK.png")
    lackey.click("text_SYSDBA.png")
    lackey.click("tree_edit_menu.png")
    lackey.click("bt_OK.png")
    assert result != None