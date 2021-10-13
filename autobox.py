import win32api
import win32con
import win32gui
import win32ui
import cv2
import numpy
from PIL import Image


def get_color(hwnd, x, y):
    '''获取窗口相对坐标的颜色值'''
    dx, dy = win32gui.ClientToScreen(hwnd, (x, y))
    color = win32gui.GetPixel(win32gui.GetWindowDC(0), dx, dy)
    return color


def move_to(hwnd, x, y):
    '''移动鼠标至窗口相对坐标'''
    (dx, dy) = win32gui.ClientToScreen(hwnd, (x, y))
    win32api.SetCursorPos([dx, dy])


def left_click(hwnd=0, x=0, y=0):
    '''模拟鼠标左键单机，不加参数时点击当前鼠标位置'''
    if hwnd != 0 and x != 0 and y != 0:
        move_to(hwnd, x, y)
        # time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_click(hwnd=0, x=0, y=0):
    '''模拟鼠标右键单机，不加参数时点击当前鼠标位置'''
    if hwnd != 0 and x != 0 and y != 0:
        move_to(hwnd, x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def key_press(hwnd, key):
    '''发送按键消息，key为虚拟键码'''
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)


def find_window(classname, title):
    '''通过窗口类名和标题获取窗口句柄，类名可为空'''
    hwnd = win32gui.FindWindow(classname, title)
    return hwnd


def get_window_rect(hwnd):
    '''获取窗口left, top, right, bottom坐标，范围包括标题栏和边框'''
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return left, top, right, bottom


def set_foreground_window(hwnd):
    '''置顶窗口'''
    win32gui.SetForegroundWindow(hwnd)


def set_window_pos(hwnd, x=0, y=0, flag=win32con.HWND_TOP):
    '''flag可以设置强制窗口置顶等，参考win32api SetWindowPos'''
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x,
                          y, 0, 0, win32con.SWP_NOSIZE)


def capture(hwnd, x1, y1, x2, y2):
    '''截图窗口相对坐标的指定区域'''
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    nl, nt = win32gui.ScreenToClient(hwnd, (left, top))
    left = left-nl
    top = top-nt
    hdesktop = win32gui.GetDesktopWindow()
    hwndDC = win32gui.GetWindowDC(hdesktop)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, 1920, 1080)
    saveDC.SelectObject(saveBitMap)
    result = saveDC.BitBlt((0, 0), (x2-x1, y2-y1), mfcDC,
                           (left+x1, top+y1), win32con.SRCCOPY)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hdesktop, hwndDC)
    if result == None:
        pass
    #     im.save("capture.png")
    return im


def hex_to_rgb(color):
    r = (color >> 16) & 255
    g = (color >> 8) & 255
    b = color & 255
    return r, g, b


def is_color_similar(color1, color2, r=0, g=0, b=0):
    r1, g1, b1 = hex_to_rgb(color1)
    r2, g2, b2 = hex_to_rgb(color2)
    if abs(r1-r2) < r and abs(g1-g2) < g and abs(b1-b2) < b:
        return True
    return False


def __template_macthing(src, template, method):
    result = cv2.matchTemplate(src, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    location = [0, 0]
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    return location


def __get_great_majority(list):
    '''获取列表中重复次数最多的键值'''
    dict = {}
    for v in list:
        if v in dict.keys():
            dict[v] += 1
        else:
            dict[v] = 1
    key = max(dict, key=dict.get)
    return key, dict[key]


def find_pic(hwnd, x1, y1, x2, y2, template, accurate=3):
    '''在指定范围中搜索图片'''
    image = capture(hwnd, x1, y1, x2, y2)
    src = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
    template = cv2.imread(template, 1)
    methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR,
               cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]
    locations = []
    for method in methods:
        locations.append(__template_macthing(src, template, method))
    location, count = __get_great_majority(locations)
    if count >= accurate:
        return location
    return -1, -1
