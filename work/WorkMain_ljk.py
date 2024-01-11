import os
import time
import pyautogui
import win32api
import win32con
import win32gui


#
# 输出当前活动窗体句柄
#
def print_GetForegroundWindow():
    hwnd_active = win32gui.GetForegroundWindow()
    print('hwnd_active hwnd:', hwnd_active)
    print('hwnd_active text:', win32gui.GetWindowText(hwnd_active))
    print('hwnd_active class:', win32gui.GetClassName(hwnd_active))


def ws(hwnd, window_list):
    title= win32gui.GetWindowText(hwnd)
    className= win32gui.GetClassName(hwnd)
    print(title+":"+className)
    window_list.append(hwnd)


try:
    os.system("netsh interface set interface \"Eth\" admin=disabled")
    # window_list = []
    # win32gui.EnumWindows(ws, window_list)
    time.sleep(1)
    # print_GetForegroundWindow()
    handle = win32gui.FindWindowEx(0, 0, "Qt5QWindowIcon", None)
    title = ''
    if handle > 0:
        title = win32gui.GetWindowText(handle)
    if not '华为云客户端' in title:
        os.system("taskkill /F /IM CloudClient.exe")
        time.sleep(2)
        os.startfile("C:\\Program Files (x86)\\Huawei\\HDPClient\\CloudClient.exe")
        time.sleep(4)
        pyautogui.click(870, 455)
        # time.sleep(1)
        pyautogui.typewrite('ytsn.jzhq000')
        time.sleep(1)
        pyautogui.click(1113, 456)
        time.sleep(16)
        os.system("netsh interface set interface \"Eth\" admin=enabled")
        os.system("taskkill /F /IM CloudClient.exe")
except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))
