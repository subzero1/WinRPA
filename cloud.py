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
    handle = win32gui.FindWindowEx(0, 0, "QWidget", None)
    if handle > 0:
        os.system("taskkill /F /IM CloudClient.exe")
        time.sleep(2)
    os.startfile("C:\\Program Files (x86)\\Huawei\\HDPClient\\CloudClient.exe")
    time.sleep(10)
    pyautogui.click(960, 491)
    pyautogui.typewrite('Huawei!@#')
    pyautogui.click(960, 566)
    time.sleep(1)
except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))

