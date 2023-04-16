# @Time    : 2022/8/21 19:01
# @Author  : 南黎
# @FileName: 6.鼠标事件.py
import win32api
import win32con
import win32gui
# 注意窗口句柄获取如果失败，要做好异常处理
try:
    # 获取窗口句柄
    handle = win32gui.FindWindowEx(0, 0, "Notepad", None)#
    print("窗口句柄是：{}".format(handle))
    # 获取鼠标位置
    point_position = win32api.GetCursorPos()
    print("鼠标位置是：{}".format(point_position))

    # 模拟鼠标在(1000, 500)位置进行点击操作
    point = (1000, 500)
    win32api.SetCursorPos(point)#设置鼠标位置
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)#按下鼠标左键
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)#松开鼠标左键


    # 获取鼠标位置
    point_position = win32api.GetCursorPos()
    print("鼠标位置是：{}".format(point_position))

except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))

# MOUSEEVENTF_LEFTDOWN：表明接按下鼠标左键
#
# MOUSEEVENTF_LEFTUP：表明松开鼠标左键
#
# MOUSEEVENTF_RIGHTDOWN：表明按下鼠标右键
#
# MOUSEEVENTF_RIGHTUP：表明松开鼠标右键
#
# MOUSEEVENTF_MIDDLEDOWN：表明按下鼠标中键
#
# MOUSEEVENTF_MIDDLEUP：表明松开鼠标中键
#
# MOUSEEVENTF_WHEEL：鼠标轮移动,数量由data给出
#
# 参数解读（dwFlags ，dx ，dy ，dwData ，dwExtraInfo）
# dwFlags=0：双字
# 指定各种功能选项的标志
# dx：double类型
# 鼠标的水平位置
# dy : double类型
# 鼠标的垂直位置
# dwData：double类型
# 标志特定参数
# dwExtraInfo=0：double类型
# 与鼠标事件相关的附加数据