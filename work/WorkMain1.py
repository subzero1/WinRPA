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
    print('hwnd_active hwnd:',hwnd_active)
    print('hwnd_active text:',win32gui.GetWindowText(hwnd_active))
    print('hwnd_active class:',win32gui.GetClassName(hwnd_active))

try:
    os.system("netsh interface set interface \"WLAN2\" admin=disabled")
    handle = win32gui.FindWindowEx(0, 0, "QWidget", None)
    if handle == 0:
        os.startfile("D:\\HDPClient\\CloudClient.exe")
    else:
        win32gui.SetForegroundWindow(handle)
        win32gui.ShowWindow(handle, win32con.SW_SHOW)
        time.sleep(1)
        pyautogui.click(1255, 730)
    time.sleep(2)
    pyautogui.click(960, 525)
    time.sleep(1)
    pyautogui.typewrite('Huawei!@#')
    time.sleep(1)
    pyautogui.click(960, 625)
except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))

