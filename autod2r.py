from cv2 import edgePreservingFilter
import autobox
import time
import ctypes
import functools
import random
'''游戏分辨率1920*1080，地图设置为玩家置中，100%不透明，在屏幕中间，不显示npc和玩家名称'''

# region constant
IMAGE_DIR=".\\images\\"
PLAYER_X = 960
'''角色在屏幕中心坐标X'''
PLAYER_Y = 530
'''角色在屏幕中心坐标Y'''
VK_LBUTTON = 0x01  # Left mouse button
VK_RBUTTON = 0x02  # Right mouse button
VK_CANCEL = 0x03  # Control-break processing
VK_MBUTTON = 0x04  # Middle mouse button (three-button mouse)
VK_XBUTTON1 = 0x05  # X1 mouse button
VK_XBUTTON2 = 0x06  # X2 mouse button
VK_BACK = 0x08  # BACKSPACE key
VK_TAB = 0x09  # TAB key
VK_CLEAR = 0x0C  # CLEAR key
VK_RETURN = 0x0D  # ENTER key
VK_SHIFT = 0x10  # SHIFT key
VK_CONTROL = 0x11  # CTRL key
VK_MENU = 0x12  # ALT key
VK_PAUSE = 0x13  # PAUSE key
VK_CAPITAL = 0x14  # CAPS LOCK key
VK_KANA = 0x15  # IME Kana mode
# IME Hanguel mode (maintained for compatibility; use VK_HANGUL)
VK_HANGUEL = 0x15
VK_HANGUL = 0x15  # IME Hangul mode
VK_JUNJA = 0x17  # IME Junja mode
VK_FINAL = 0x18  # IME final mode
VK_HANJA = 0x19  # IME Hanja mode
VK_KANJI = 0x19  # IME Kanji mode
VK_ESCAPE = 0x1B  # ESC key
VK_CONVERT = 0x1C  # IME convert
VK_NONCONVERT = 0x1D  # IME nonconvert
VK_ACCEPT = 0x1E  # IME accept
VK_MODECHANGE = 0x1F  # IME mode change request
VK_SPACE = 0x20  # SPACEBAR
VK_PRIOR = 0x21  # PAGE UP key
VK_NEXT = 0x22  # PAGE DOWN key
VK_END = 0x23  # END key
VK_HOME = 0x24  # HOME key
VK_LEFT = 0x25  # LEFT ARROW key
VK_UP = 0x26  # UP ARROW key
VK_RIGHT = 0x27  # RIGHT ARROW key
VK_DOWN = 0x28  # DOWN ARROW key
VK_SELECT = 0x29  # SELECT key
VK_PRINT = 0x2A  # PRINT key
VK_EXECUTE = 0x2B  # EXECUTE key
VK_SNAPSHOT = 0x2C  # PRINT SCREEN key
VK_INSERT = 0x2D  # INS key
VK_DELETE = 0x2E  # DEL key
VK_HELP = 0x2F  # HELP key
VK_0 = 0x30  # 0 key
VK_1 = 0x31  # 1 key
VK_2 = 0x32  # 2 key
VK_3 = 0x33  # 3 key
VK_4 = 0x34  # 4 key
VK_5 = 0x35  # 5 key
VK_6 = 0x36  # 6 key
VK_7 = 0x37  # 7 key
VK_8 = 0x38  # 8 key
VK_9 = 0x39  # 9 key
VK_A = 0x41
VK_B = 0x42
VK_C = 0x43
VK_D = 0x44
VK_E = 0x45
VK_F = 0x46
VK_G = 0x47
VK_H = 0x48
VK_I = 0x49
VK_J = 0x4A
VK_K = 0x4B
VK_L = 0x4C
VK_M = 0x4D
VK_N = 0x4E
VK_O = 0x4F
VK_P = 0x50
VK_Q = 0x51
VK_R = 0x52
VK_S = 0x53
VK_T = 0x54
VK_U = 0x55
VK_V = 0x56
VK_W = 0x57
VK_X = 0x58
VK_Y = 0x59
VK_Z = 0x5A
VK_LWIN = 0x5B  # Left Windows key (Natural keyboard)
VK_RWIN = 0x5C  # Right Windows key (Natural keyboard)
VK_APPS = 0x5D  # Applications key (Natural keyboard)
VK_SLEEP = 0x5F  # Computer Sleep key
VK_NUMPAD0 = 0x60  # Numeric keypad 0 key
VK_NUMPAD1 = 0x61  # Numeric keypad 1 key
VK_NUMPAD2 = 0x62  # Numeric keypad 2 key
VK_NUMPAD3 = 0x63  # Numeric keypad 3 key
VK_NUMPAD4 = 0x64  # Numeric keypad 4 key
VK_NUMPAD5 = 0x65  # Numeric keypad 5 key
VK_NUMPAD6 = 0x66  # Numeric keypad 6 key
VK_NUMPAD7 = 0x67  # Numeric keypad 7 key
VK_NUMPAD8 = 0x68  # Numeric keypad 8 key
VK_NUMPAD9 = 0x69  # Numeric keypad 9 key
VK_MULTIPLY = 0x6A  # Multiply key
VK_ADD = 0x6B  # Add key
VK_SEPARATOR = 0x6C  # Separator key
VK_SUBTRACT = 0x6D  # Subtract key
VK_DECIMAL = 0x6E  # Decimal key
VK_DIVIDE = 0x6F  # Divide key
VK_F1 = 0x70  # F1 key
VK_F2 = 0x71  # F2 key
VK_F3 = 0x72  # F3 key
VK_F4 = 0x73  # F4 key
VK_F5 = 0x74  # F5 key
VK_F6 = 0x75  # F6 key
VK_F7 = 0x76  # F7 key
VK_F8 = 0x77  # F8 key
VK_F9 = 0x78  # F9 key
VK_F10 = 0x79  # F10 key
VK_F11 = 0x7A  # F11 key
VK_F12 = 0x7B  # F12 key
VK_F13 = 0x7C  # F13 key
VK_F14 = 0x7D  # F14 key
VK_F15 = 0x7E  # F15 key
VK_F16 = 0x7F  # F16 key
VK_F17 = 0x80  # F17 key
VK_F18 = 0x81  # F18 key
VK_F19 = 0x82  # F19 key
VK_F20 = 0x83  # F20 key
VK_F21 = 0x84  # F21 key
VK_F22 = 0x85  # F22 key
VK_F23 = 0x86  # F23 key
VK_F24 = 0x87  # F24 key
VK_NUMLOCK = 0x90  # NUM LOCK key
VK_SCROLL = 0x91  # SCROLL LOCK key
VK_LSHIFT = 0xA0  # Left SHIFT key
VK_RSHIFT = 0xA1  # Right SHIFT key
VK_LCONTROL = 0xA2  # Left CONTROL key
VK_RCONTROL = 0xA3  # Right CONTROL key
VK_LMENU = 0xA4  # Left MENU key
VK_RMENU = 0xA5  # Right MENU key
VK_BROWSER_BACK = 0xA6  # Browser Back key
VK_BROWSER_FORWARD = 0xA7  # Browser Forward key
VK_BROWSER_REFRESH = 0xA8  # Browser Refresh key
VK_BROWSER_STOP = 0xA9  # Browser Stop key
VK_BROWSER_SEARCH = 0xAA  # Browser Search key
VK_BROWSER_FAVORITES = 0xAB  # Browser Favorites key
VK_BROWSER_HOME = 0xAC  # Browser Start and Home key
VK_VOLUME_MUTE = 0xAD  # Volume Mute key
VK_VOLUME_DOWN = 0xAE  # Volume Down key
VK_VOLUME_UP = 0xAF  # Volume Up key
VK_MEDIA_NEXT_TRACK = 0xB0  # Next Track key
VK_MEDIA_PREV_TRACK = 0xB1  # Previous Track key
VK_MEDIA_STOP = 0xB2  # Stop Media key
VK_MEDIA_PLAY_PAUSE = 0xB3  # Play/Pause Media key
VK_LAUNCH_MAIL = 0xB4  # Start Mail key
VK_LAUNCH_MEDIA_SELECT = 0xB5  # Select Media key
VK_LAUNCH_APP1 = 0xB6  # Start Application 1 key
VK_LAUNCH_APP2 = 0xB7  # Start Application 2 key
VK_OEM_1 = 0xBA  # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the ';:' key
VK_OEM_PLUS = 0xBB  # For any country/region, the '+' key
VK_OEM_COMMA = 0xBC  # For any country/region, the ',' key
VK_OEM_MINUS = 0xBD  # For any country/region, the '-' key
VK_OEM_PERIOD = 0xBE  # For any country/region, the '.' key
VK_OEM_2 = 0xBF  # Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '/?' key =
VK_OEM_3 = 0xC0  # Used for miscellaneous characters; it can vary by keyboard. = For the US standard keyboard, the '`~' key
# Used for miscellaneous characters; it can vary by keyboard. For the US standard keyboard, the '[{' key
VK_OEM_4 = 0xDB
VK_OEM_5 = 0xDC  # Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the '\|' key
VK_OEM_6 = 0xDD  # Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the ']}' key
VK_OEM_7 = 0xDE  # Used for miscellaneous characters; it can vary by keyboard.For the US standard keyboard, the 'single-quote/double-quote' key
VK_OEM_8 = 0xDF  # Used for miscellaneous characters; it can vary by keyboard.
VK_OEM_102 = 0xE2  # Either the angle bracket key or the backslash key on the RT 102-key keyboard 0xE3-E4 OEM specific
VK_PROCESSKEY = 0xE5  # IME PROCESS key 0xE6 = OEM specific #
VK_PACKET = 0xE7  # Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP #-
VK_ATTN = 0xF6  # Attn key
VK_CRSEL = 0xF7  # CrSel key
VK_EXSEL = 0xF8  # ExSel key
VK_EREOF = 0xF9  # Erase EOF key
VK_PLAY = 0xFA  # Play key
VK_ZOOM = 0xFB  # Zoom key
VK_NONAME = 0xFC  # Reserved
VK_PA1 = 0xFD  # PA1 key
VK_OEM_CLEAR = 0xFE
# endregion


def stuck_check(func):
    n = [0]

    @functools.wraps(func)
    def decorated(*args, **kwargs):
        if n[0] > 10:
            print("****角色卡死，尝试解除****")
            n[0] = 0
            for i in range(2):
                func(*args, **kwargs, stuck=True)
            return True
        if func(*args, **kwargs):
            n[0] += 1
            return True
        else:
            n[0] = 0
            return False
    return decorated


class autod2r:

    def __init__(self, hwnd=None) -> None:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
        if hwnd == None:
            self.hwnd = autobox.find_window(
                "OsWindow", "Diablo II: Resurrected")
            if self.hwnd == 0:
                raise Exception("d2r window not found", self.hwnd)
        else:
            self.hwnd = hwnd
        self.func_count = 0

    def is_right_color(self, x, y, color, r=0, g=0, b=0):
        '''判断x,y的像素颜色是否为color'''
        c = autobox.get_color(self.hwnd, x, y)
        if c == color:
            return True
        else:
            return autobox.is_color_similar(c, color, r, g, b)

    def set_foreground(self):
        '''置顶窗口'''
        autobox.set_foreground_window(self.hwnd)

    def is_on_landing(self):
        return self.is_right_color(1720, 1010, 0x82b7cd)

    def is_on_select_difficulty(self):
        '''相对坐标856,454 绝对坐标869,501 0xfd9234 (52, 146, 253)'''
        return self.is_right_color(856, 454, 0xfd9234)

    def click_start_game(self):
        '''在登录界面进行游戏'''
        self.left_click( 800, 983)  # 战网模式

    def click_difficulty(self, diff=0):
        '''点击选择游戏难度 0-普通 1噩梦 2地狱'''
        if diff != 0 and diff != 1 and diff != 2:
            raise Exception("diff only can be 0 1 2", self.hwnd)

        self.left_click( 956, 454+66*diff)


    def is_map_open(self):
        ''''''
        return self.is_right_color(971, 531, 0xfd9832)

    def set_window_pos(self):
        '''窗口移动至0，0并置顶'''
        autobox.set_window_pos(self.hwnd)

    def left_click(self, x=0, y=0):
        autobox.left_click(self.hwnd,x, y)

    def get_player_ref_location(self, ref_pic, trans=False):
        #start = time.time()
        x, y = autobox.find_pic(self.hwnd, 0, 0, 1920, 1080, IMAGE_DIR+ref_pic)
        #elapsed = (time.time() - start)
        #print("find pic time used:", elapsed)
        if x >= 0 and y >= 0:
            dx = PLAYER_X-x
            dy = PLAYER_Y-y
            if trans:
                return dx*10, dy*10
            else:
                return dx, dy
        else:
            raise Exception("find_pic未找到%s" % ref_pic)

    @stuck_check
    def move_to_ref_location(self, ref_pic, x, y, stuck=False):

        dx, dy = self.get_point_ref_player_location(ref_pic, x, y)
        distance = int(pow(dx**2+dy**2, 0.5))  # 地图距离，实际距离10倍像素

        tx = dx if abs(dx) < 20 else dx*10  # 地图比例尺10倍
        ty = dy if abs(dy) < 20 else dy*10

        while abs(tx) > 700 or abs(ty) > 360:
            tx = int(tx/1.2)
            ty = int(ty/1.2)
        # print("当前坐标%d,%d,目的坐标%d,%d,相对坐标%d,%d,距离%d,点击屏幕%d,%d,是否到达%s" %
        #      (cx, cy, x, y, dx, dy, distance, tx, ty, distance < 20))
        if distance < 20:
            return False
        if not stuck:
            print("moving to %d,%d" % (x, y))
            self.left_click(PLAYER_X+tx, PLAYER_Y+ty)
        else:
            self.left_click(PLAYER_X+random.randint(-50, 50),
                            PLAYER_Y+random.randint(-50, 50))
        return True

    def key_press(self, key):
        autobox.key_press(self.hwnd, key)

    def find_drops(self, pick=True):
        '''返回找到的x,y坐标'''
        '未找到返回-1,-1'
        self.key_press(VK_LMENU)
        time.sleep(0.3)
        x, y = autobox.find_pic(self.hwnd, 0, 0, 1920, 1080, IMAGE_DIR+"drops.png")
        if pick and x >= 0 and y >= 0:
            autobox.move_to(self.hwnd, x+30, y+15)
            time.sleep(0.5)
            self.left_click()
        return x, y

    def find_clickable(self, x1, y1, x2, y2, template, interval=30):
        '''未找到图像将抛出异常'''
        for y in range(y1, y2, interval):
            for x in range(x1, x2, interval):
                autobox.move_to(self.hwnd, x, y)
                fx, fy = autobox.find_pic(
                    self.hwnd, x1-200, y1-200, x2, y2, IMAGE_DIR+template)
                if fx >= 0 and fy >= 0:
                    return x, y
        raise Exception("未找到%s" % template)

    def get_point_ref_player_location(self, ref_pic, x, y, trans=False):
        '''获取参考系内某个点相对于角色的坐标'''
        cx, cy = self.get_player_ref_location(ref_pic)  # 当前相对参考物坐标
        if cx == 0 and cy == 0:
            print("没有找到参照物，确认地图是否开启？")
            return 0, 0
        if trans:
            return (x-cx)*10, (y-cy)*10
        else:
            return x-cx, y-cy

    def click_door(self, ref_pic, x, y, dx=0, dy=0):
        tx, ty = self.get_point_ref_player_location(ref_pic, x, y, True)
        autobox.move_to(self.hwnd, PLAYER_X+tx, PLAYER_Y+ty)
        time.sleep(0.5)
        self.left_click()
        return

    def cast(self, key, x=PLAYER_X, y=PLAYER_Y):
        '''在指定位置施放技能，默认为角色脚下'''
        self.key_press(key)
        autobox.right_click(self.hwnd, x, y)

    def click_exit(self):
        self.left_click( 962, 473)

    def is_on_menu(self):
        return self.is_right_color(1062, 313, 0x576777)

    def is_on_loading(self):
        return self.is_right_color(926, 769, 0x88bfd0)

    def is_in_game(self):
        return self.is_right_color(961, 1043, 0x33444f)

    def wait_for_loading(self):
        time.sleep(1)
        while self.is_on_loading():
            time.sleep(1)

    def is_drugs_bag_open(self):
        return not self.is_right_color(1209, 1005, 0x8fb9cb)

    def is_bad_connect(self):
        return self.is_right_color(1062, 482, 0xe8f8ff)

    def click_bad_connect_OK(self):
        self.left_click( 941, 577)

    def get_drugs(self):
        drugs = []
        if not self.is_drugs_bag_open():
            self.key_press(VK_OEM_3)
        for i in range(4):
            for j in range(4):
                drugs.append(not self.is_right_color(
                    1113+j*62, 1038-i*56, 0x232323, 5, 5, 5))
        return drugs
    def use_drug(self):
        drugs = []
        for i in range(4):
                drugs.append(not self.is_right_color(
                    1113, 1038-i*56, 0x232323, 5, 5, 5))
        for i in range(3):
            if drugs[i]:
                self.key_press(VK_1+i)
                break

    def use_drug_if_hp_is_low(self):
        if self.is_low_hp():
            self.use_drug()

    def is_low_hp(self):
        return not self.is_right_color(467, 965, 0x2d2ab1, 50, 20, 20)
    

    def restart_game(self, diff=2):
        self.key_press(autobox.win32con.VK_ESCAPE)
        time.sleep(0.5)
        while True:
            time.sleep(1)
            if self.is_on_landing():
                self.click_start_game()
                continue
            if self.is_on_select_difficulty():
                self.click_difficulty(diff)
                continue
            if self.is_on_menu():
                self.click_exit()
                continue
            if self.is_bad_connect():
                self.click_bad_connect_OK()
                continue
            if self.is_in_game():
                return
            


#
