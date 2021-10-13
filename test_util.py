import win32gui
import time
import ctypes
import autobox

'''测试工具，方便获取屏幕坐标颜色及坐标'''
'''运行以后鼠标放在游戏内可以显示一些信息'''

REF="ref_nlskdsd_new.png" #参照物图片

def Hex_to_RGB(RGBint):
    R = RGBint & 255
    G = (RGBint >> 8) & 255
    B = (RGBint >> 16) & 255
    return (R, G, B)


ctypes.windll.shcore.SetProcessDpiAwareness(2)  # 缩放感知，DPI不为100%时使用
hwnd = win32gui.FindWindow(None, "Diablo II: Resurrected")  # 窗口句柄
while True:
    x, y = win32gui.GetCursorPos()
    dx, dy = win32gui.ScreenToClient(hwnd, (x, y))
    color = win32gui.GetPixel(win32gui.GetWindowDC(0), x, y)
    fx,fy=autobox.find_pic(hwnd,0,0,1920,1080,REF)
    fdx=960-fx
    fdy=530-fy
    if dx<1920 and dy<1080:
        print("鼠标%d,%d,0x%x; RGB%s; 参照物%d,%d; 角色\"%s\",%d,%d" % (dx, dy,color,Hex_to_RGB(color),fx,fy,REF,fdx,fdy))
    time.sleep(1)
