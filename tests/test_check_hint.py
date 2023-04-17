import lackey
from re_tests_plugin import *

def test_1(open_connection):
    move_location = lackey.find("files/images/icon_connected.png").getTarget()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    time.sleep(1)
    assert lackey.find("files/images/hint_disconnect.png") != None

def test_2():
    move_location = lackey.find("files/images/icon_disconnected.png").getTarget()
    mouse = lackey.Mouse()
    mouse.move(loc=move_location)
    time.sleep(1)
    assert lackey.find("files/images/hint_connect.png") != None