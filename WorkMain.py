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
    if handle > 0:
        os.system("taskkill /F /IM CloudClient.exe")
        time.sleep(2)
    os.startfile("D:\\HDPClient\\CloudClient.exe")
    time.sleep(3)
    pyautogui.click(960, 525)
    pyautogui.typewrite('Huawei!@#')
    pyautogui.click(960, 625)
    time.sleep(16)
    os.system("netsh interface set interface \"WLAN2\" admin=enabled")
except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))

