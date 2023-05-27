import win32api
import win32con
import win32gui
import os
import time
import pyautogui


try:
    os.startfile("C:\\Program Files (x86)\\Sangfor\\SSL\\SangforCSClient\\SangforCSClient.exe")
    time.sleep(8)
    # 获取窗口句柄
    handle = win32gui.FindWindowEx(0, 0, "Static", None)  # 桌面窗口的所有子窗口检索类名"Edit"，标题为None的窗口
    print("請輸入賬號")
    # 模拟鼠标在(1000, 500)位置进行点击操作
    point = (860, 535)
    win32api.SetCursorPos(point)#设置鼠标位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)#按下鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)#松开鼠标左键
    pyautogui.typewrite('zhongweijie0920')

    print("請輸入密碼")
    time.sleep(5)
    point = (860, 570)
    win32api.SetCursorPos(point)#设置鼠标位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)#按下鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)#松开鼠标左键
    pyautogui.typewrite('QYIed#@7163')
except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))
