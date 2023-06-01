import win32api
import win32con
import win32gui
import os
import time

# 注意窗口句柄获取如果失败，要做好异常处理
try:
    os.startfile("C:\\Program Files (x86)\\Sangfor\\SSL\\SangforCSClient\\SangforCSClient.exe")
    time.sleep(2)
    # 获取窗口句柄
    handle = win32gui.FindWindowEx(0, 0, "Static", None)  # 桌面窗口的所有子窗口检索类名"Edit"，标题为None的窗口
    print("窗口句柄是：{}".format(handle))
    loginid = win32gui.GetWindowPlacement(handle)
    time.sleep(10)
    print(999999999, loginid)
    print(loginid[4][0])
    print(loginid[4][1])
    result = win32api.MessageBox(handle, "我要关闭句柄为{}的窗口了".format(handle), "关闭窗口警告", 1)
    if result == 1:
        win32api.MessageBox(handle, "关闭窗口了", "关闭窗口", 0)
        win32gui.PostMessage(handle, win32con.WM_CLOSE, 0, 0)  # 关闭窗口

    elif result == 2:
        win32api.MessageBox(handle, "看来你不想关闭窗口啊", "不关闭窗口", 0)

except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))
