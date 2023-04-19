import os
import time
import pyautogui


try:
    os.startfile("D:\\HDPClient\\CloudClient.exe")
    os.system("netsh interface set interface \"WLAN2\" admin=disabled")
    time.sleep(2)
    pyautogui.click(960, 525)
    print("請輸入密碼")
    pyautogui.typewrite('Huawei!@#')
    time.sleep(1)
    pyautogui.click(960, 625)
except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))
