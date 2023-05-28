import win32api
import win32con
import win32gui
import os
import time
import pyautogui

try:
    time.sleep(2)
    handle = win32gui.FindWindowEx(0, 0, "Static", None)
    if handle > 0:
        os.system("taskkill /F /IM SangforCSClient.exe")
        time.sleep(2)
    os.startfile("C:\\Program Files (x86)\\Sangfor\\SSL\\SangforCSClient\\SangforCSClient.exe")
    print('输入账号密码：')
    time.sleep(20)
    pyautogui.click(855, 535)
    pyautogui.typewrite('zhongweijie0920')
    pyautogui.click(855, 570)
    pyautogui.typewrite('QYIed#@7163')
    time.sleep(2)
except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))
