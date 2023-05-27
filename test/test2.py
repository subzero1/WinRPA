# @Time    : 2022/8/22 18:36
# @Author  : 南黎
# @FileName: 10.消息框.py
import win32api
import win32gui
# 注意窗口句柄获取如果失败，要做好异常处理
try:
    # 获取窗口句柄
    handle = win32gui.FindWindowEx(0, 0, "Notepad", None)#桌面窗口的所有子窗口检索类名"Edit"，标题为None的窗口
    print("窗口句柄是：{}".format(handle))

    result = win32api.MessageBox(handle, "消息内容", "消息标题",  1)
    #win32con.MB_OK和0是一样的 表示一个选项，1表示有两个选项，2表示有三个选项
    print(result)#返回1表示选择第一个选项，返回2表示选择第二个选项

    if result==1:
        win32api.MessageBox(handle, "我猜对了吗？", "我猜你你选了第1个选项", 0)
    elif result==2:
        win32api.MessageBox(handle, "我猜对了吗？", "我猜你你选了第2个选项", 0)

except Exception as e:
    print("窗口句柄获取失败或是前台设置失败：{}".format(e))