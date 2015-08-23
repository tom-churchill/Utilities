import win32api
import win32con
import time
import autoit

def wait_for_modifiers():
    is_alt_down = lambda: win32api.GetAsyncKeyState(win32con.VK_LMENU | win32con.VK_CONTROL)
    is_ctrl_down = lambda: win32api.GetAsyncKeyState(win32con.VK_CONTROL)
    
    while is_alt_down():
        time.sleep(0.05)

wait_for_modifiers()

autoit.opt('SendKeyDelay', 0)
autoit.opt('SendKeyDownDelay', 0)
autoit.send('{LALT down}', 0)
autoit.send('{LALT up}', 0)
time.sleep(0.05)
autoit.send('import pdb; pdb.set_trace()', 0)
