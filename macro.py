from typing import Self
import pyautogui as pag
import time
import keyboard
import threading
from pynput.keyboard import Key, Controller as KBController
from pynput.mouse import Button, Controller as MController
import sys
import ctypes

# OS-Specific Imports
if sys.platform == "darwin":
    try:
        import Quartz
    except ImportError:
        Quartz = None
elif sys.platform == "win32":
    # Define Windows low-level input structures
    PUL = ctypes.POINTER(ctypes.c_ulong)
    
    class MOUSEINPUT(ctypes.Structure):
        _fields_ = [
            ("dx", ctypes.c_long),
            ("dy", ctypes.c_long),
            ("mouseData", ctypes.c_ulong),
            ("dwFlags", ctypes.c_ulong),
            ("time", ctypes.c_ulong),
            ("dwExtraInfo", PUL)
        ]

    class INPUT_UNION(ctypes.Union):
        _fields_ = [("mi", MOUSEINPUT)]

    class INPUT(ctypes.Structure):
        _fields_ = [
            ("type", ctypes.c_ulong),
            ("ui", INPUT_UNION)
        ]


KEYBOARD = KBController()
MOUSE = MController()


# for 1920x1080, fullscreen


def fuzzy_equals(num1: int | float, num2: int | float, episilon: int | float) -> bool:
    return abs(num1 - num2) <= episilon


class Color3:
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def fuzzy_equals(self, other: Self, epsilon: int | Self = 2) -> bool:
        if isinstance(epsilon, int):
            return (
                fuzzy_equals(self.red, other.red, epsilon) and
                fuzzy_equals(self.green, other.green, epsilon) and
                fuzzy_equals(self.blue, other.blue, epsilon)
            )
        else: # elif isinstance(epsilon, Color3): # type: ignore
            return (
                fuzzy_equals(self.red, other.red, epsilon.red) and
                fuzzy_equals(self.green, other.green, epsilon.green) and 
                fuzzy_equals(self.blue, other.blue, epsilon.blue)
            )


INSET_COLOR = Color3(239, 232, 214)
RECIPES_COLOR = Color3(247, 245, 187)
TEXT_COLOR = Color3(0, 43, 89)


SPRINT = pag.Point(48, 1019)


RECIPE_CARROT = (12, 20)
RECIPE_CHAI = (107, 74)
RECIPE_PUMPKIN_PIE = (78, 60)
RECIPE_PUMPKIN_SPICE = (101, 7)
RECIPE_SHORTBREAD = (115, 41)
RECIPE_BANANA = (36, 86)
RECIPE_CINNAMON = (110, 58)
RECIPE_CORN = (116, 70)


RECIPE_LIST: list[tuple[int, int]] = [
    RECIPE_CARROT,
    RECIPE_CHAI,
    RECIPE_PUMPKIN_PIE,
    RECIPE_PUMPKIN_SPICE,
    RECIPE_SHORTBREAD,
    RECIPE_BANANA,
    RECIPE_CINNAMON,
    RECIPE_CORN
]


ID_CARROT = 0
ID_CHAI = 1
ID_PUMPKIN_PIE = 2
ID_PUMPKIN_SPICE = 3
ID_SHORTBREAD = 4
ID_BANANA = 5
ID_CINNAMON = 6
ID_CORN = 7


CLICK_FIRST = pag.Point(1309, 400)
CLICK_SECOND = pag.Point(1473, 393)
CLICK_THRID = pag.Point(1626, 394)
CLICK_FOURTH = pag.Point(1792, 391)


CINNAMON = pag.Point(87, 179)
GINGER = pag.Point(178, 221)
CLOVES = pag.Point(271, 185)
VANILLA = pag.Point(361, 232)
NUTMEG = pag.Point(451, 180)
SALT = pag.Point(549, 143)
NUTS = pag.Point(717, 185)
SUGAR = pag.Point(934, 187)
FLOUR = pag.Point(1103, 187)
BAKING_SODA = pag.Point(1368, 179)
CORNMEAL = pag.Point(1579, 177)
FLAX_SEEDS = pag.Point(1800, 188)
APPLES = pag.Point(95, 449)
BANANAS = pag.Point(302, 447)
PUMPKIN_PUREE = pag.Point(110, 709)
GRATED_CARROTS = pag.Point(308, 724)
OAT_BUTTER = pag.Point(325, 1009)
FRIDGE = pag.Point(377, 629)
MIXER = pag.Point(1713, 626)


CLOSE = pag.Point(1879, 101)
CLOSE_SHOP = pag.Point(1318, 212)


INGREDIENTS_CARROT = [
    FLOUR,
    SUGAR,
    BAKING_SODA,
    FLAX_SEEDS,
    FRIDGE,
    GRATED_CARROTS,
    CINNAMON,
    NUTMEG,
    VANILLA,
    NUTS
]

INGREDIENTS_CHAI = [
    FLOUR,
    SUGAR,
    BAKING_SODA,
    FRIDGE,
    OAT_BUTTER,
    FLAX_SEEDS,
    CINNAMON,
    GINGER,
    CLOVES,
    VANILLA,
    SALT
]

INGREDIENTS_PUMPKIN_PIE = [
    FLOUR,
    SUGAR,
    FRIDGE,
    PUMPKIN_PUREE,
    FLAX_SEEDS,
    OAT_BUTTER,
    GINGER,
    NUTMEG,
    CLOVES
]

INGREDIENTS_PUMPKIN_SPICE = [
    FRIDGE,
    PUMPKIN_PUREE,
    FLOUR,
    SUGAR,
    BAKING_SODA,
    OAT_BUTTER,
    FLAX_SEEDS,
    CINNAMON,
    NUTMEG,
    CLOVES
]

INGREDIENTS_SHORTBREAD = [
    FLOUR,
    SUGAR,
    FRIDGE,
    OAT_BUTTER,
    VANILLA,
    SALT
]

INGREDIENTS_BANANA = [
    BANANAS,
    FLOUR,
    SUGAR,
    FRIDGE,
    OAT_BUTTER,
    BAKING_SODA,
    VANILLA,
    SALT,
    NUTS
]

INGREDIENTS_CINNAMON = [
    FLOUR,
    SUGAR,
    APPLES,
    FRIDGE,
    OAT_BUTTER,
    FLAX_SEEDS,
    CINNAMON,
    NUTMEG
]

INGREDIENTS_CORN = [
    CORNMEAL,
    FLOUR,
    SUGAR,
    FRIDGE,
    OAT_BUTTER,
    BAKING_SODA,
    SALT
]


LOCK_OUT1 = pag.Point(843, 428)
LOCK_OUT2 = pag.Point(565, 777)
LOCK_OUT3 = pag.Point(1331, 1019)

LOCK_OUT_COL = pag.Point(1044, 92)


PIC1 = pag.Point(466, 440)
PIC2 = pag.Point(707, 440)
PIC3 = pag.Point(957, 440)
PIC4 = pag.Point(1213, 440)
PIC5 = pag.Point(1485, 440)
PIC6 = pag.Point(466, 690)
PIC7 = pag.Point(707, 690)
PIC8 = pag.Point(957, 690)
PIC9 = pag.Point(1213, 690)
PIC10 = pag.Point(1485, 690)
PIC11 = pag.Point(466, 940)
PIC12 = pag.Point(707, 940)
PIC13 = pag.Point(957, 940)
PIC14 = pag.Point(1213, 940)
PIC15 = pag.Point(1485, 940)



CLR1 = Color3(224, 237, 253)
CLR2 = Color3(104, 78, 124)
CLR3 = Color3(212, 117, 132)
CLR4 = Color3(255, 190, 253)
CLR5 = Color3(4, 254, 255)
CLR6 = Color3(178, 238, 255)
CLR7 = Color3(161, 218, 246)
CLR8 = Color3(248, 213, 251)
CLR9 = Color3(13, 8, 113)
CLR10 = Color3(228, 165, 188)
CLR11 = Color3(250, 116, 203)
CLR12 = Color3(45, 5, 14)
CLR13 = Color3(4, 64, 83)
CLR14 = Color3(31, 8, 41)
CLR15 = Color3(207, 183, 224)

CLR_LIST = [
    CLR1,
    CLR2,
    CLR3,
    CLR4,
    CLR5,
    CLR6,
    CLR7,
    CLR8,
    CLR9,
    CLR10,
    CLR11,
    CLR12,
    CLR13,
    CLR14,
    CLR15
]

PIC_LIST = [
    PIC1,
    PIC2,
    PIC3,
    PIC4,
    PIC5,
    PIC6,
    PIC7,
    PIC8,
    PIC9,
    PIC10,
    PIC11,
    PIC12,
    PIC13,
    PIC14,
    PIC15
]


WHITE = Color3(255, 255, 255)


FIND_RECIPES_START = 1270


shift_lock = False


def find_recipes() -> tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]:
    x = FIND_RECIPES_START
    y = 300
    r, g, b = pag.pixel(0, y)
    clr = Color3(r, g, b)
    while not clr.fuzzy_equals(RECIPES_COLOR, 10):
        y += 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)

    y += 2

    r, g, b = pag.pixel(x-1, y)
    clr = Color3(r, g, b)
    while clr.fuzzy_equals(RECIPES_COLOR, 10):
        x -= 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)
    while not clr.fuzzy_equals(RECIPES_COLOR, 10):
        x += 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)


    first = (x, y-2)

    while clr.fuzzy_equals(RECIPES_COLOR, 10):
        x += 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)
    while not clr.fuzzy_equals(RECIPES_COLOR, 10):
        x += 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)
    
    second = (x, y-2)
    
    while clr.fuzzy_equals(RECIPES_COLOR, 10):
        x += 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)
    while not clr.fuzzy_equals(RECIPES_COLOR, 10):
        x += 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)
    
    third = (x, y-2)
    
    while clr.fuzzy_equals(RECIPES_COLOR, 10):
        x += 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)
    while not clr.fuzzy_equals(RECIPES_COLOR, 10):
        x += 1
        r, g, b = pag.pixel(x, y)
        clr = Color3(r, g, b)
    
    fourth = (x, y-2)

    print(first)
    print(second)
    print(third)
    print(fourth)

    return first, second, third, fourth


def check_recipe(recipe: tuple[int, int]) -> int:
    x = recipe[0]
    y = recipe[1]
    for id, off in enumerate(RECIPE_LIST):
        offx = off[0] - 1
        offy = off[1] - 1
        r, g, b = pag.pixel(x + offx, y + offy)
        clr = Color3(r, g, b)
        if TEXT_COLOR.fuzzy_equals(clr, 150):
            return id
    raise


def get_priority_recipe() -> tuple[int, pag.Point]:
    r1, r2, r3, r4 = find_recipes()
    c1 = check_recipe(r1)
    c2 = check_recipe(r2)
    c3 = check_recipe(r3)
    c4 = check_recipe(r4)
    id = min([c1, c2, c3, c4])
    print(c1, c2, c3, c4)
    if id == c1:
        return c1, CLICK_FIRST
    elif id == c2:
        return c2, CLICK_SECOND
    elif id == c3:
        return c3, CLICK_THRID
    else: # id == c4
        return c4, CLICK_FOURTH


# AI :D
def send_low_level_mouse_move(x: int, y: int, move_relative: bool = False):
    """
    Moves the mouse using OS low-level hardware event injection APIs.
    
    :param x: Target X coordinate (absolute pixel space) or delta X (relative)
    :param y: Target Y coordinate (absolute pixel space) or delta Y (relative)
    :param move_relative: If True, moves relative to current cursor. If False, absolute.
    """

    # ==========================================
    # macOS: Quartz CoreGraphics Event Pipeline
    # ==========================================
    if sys.platform == "darwin":
        if Quartz is None:
            raise ImportError("Please run: pip install pyobjc-framework-Quartz")
        
        # Determine targeting coordinates
        if move_relative:
            # Fetch current mouse position via an empty event container
            current_event = Quartz.CGEventCreate(None)
            current_pos = Quartz.CGEventGetLocation(current_event)
            target_x = current_pos.x + x
            target_y = current_pos.y + y
        else:
            target_x = float(x)
            target_y = float(y)

        # Build low-level event object for a mouse move event
        mouse_event = Quartz.CGEventCreateMouseEvent(
            None,                       # Event source (None defaults to hardware)
            Quartz.kCGEventMouseMoved,  # Event Type
            (target_x, target_y),       # Target Coordinate Tuple
            0                           # Mouse Button (0 for move)
        )
        
        # Inject event straight into the active Human Interface Device stream
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouse_event)

    # ==========================================
    # Windows: DirectInput via SendInput API
    # ==========================================
    elif sys.platform == "win32":
        # Windows API flag definitions
        INPUT_MOUSE = 0
        MOUSEEVENTF_MOVE = 0x0001
        MOUSEEVENTF_ABSOLUTE = 0x8000

        flags = MOUSEEVENTF_MOVE
        
        if not move_relative:
            flags |= MOUSEEVENTF_ABSOLUTE
            # Windows absolute coordinates map to a normalized 0-65535 matrix virtual space
            # rather than pixel space to ensure cross-monitor safety.
            screen_width = ctypes.windll.user32.GetSystemMetrics(0)
            screen_height = ctypes.windll.user32.GetSystemMetrics(1)
            target_x = int((x * 65535) / screen_width)
            target_y = int((y * 65535) / screen_height)
        else:
            target_x = int(x)
            target_y = int(y)

        # Construct hardware input container matching Windows API signatures
        mouse_input = MOUSEINPUT(target_x, target_y, 0, flags, 0, None)
        input_container = INPUT(type=INPUT_MOUSE, ui=INPUT_UNION(mi=mouse_input))
        
        # Fire low-level driver event input block
        ctypes.windll.user32.SendInput(1, ctypes.pointer(input_container), ctypes.sizeof(input_container))

    else:
        raise NotImplementedError(f"Low-level driver handling not implemented for platform: {current_os}")


def left_click():
    MOUSE.press(Button.left)
    time.sleep(0.05)
    MOUSE.release(Button.left)


def click_at(point: pag.Point):
    send_low_level_mouse_move(point.x, point.y)
    send_low_level_mouse_move(point.x, point.y+1)
    time.sleep(0.3)
    left_click()
    time.sleep(0.1)
    left_click()
    time.sleep(0.1)


def _lockout_check() -> None:
    r, g, b = pag.pixel(LOCK_OUT_COL.x, LOCK_OUT_COL.y)
    clr = Color3(r, g, b)
    for i, col in enumerate(CLR_LIST):
        if clr.fuzzy_equals(col, 10):
            click_at(PIC_LIST[i])
            return
    click_at(PIC8)
    return
def lockout_check() -> None:
    global shift_lock
    r1, g1, b1 = pag.pixel(LOCK_OUT1.x, LOCK_OUT1.y)
    r2, g2, b2 = pag.pixel(LOCK_OUT2.x, LOCK_OUT2.y)
    r3, g3, b3 = pag.pixel(LOCK_OUT3.x, LOCK_OUT3.y)
    clr1 = Color3(r1, g1, b1)
    clr2 = Color3(r2, g2, b2)
    clr3 = Color3(r3, g3, b3)
    procced = False
    attempts = 0
    while WHITE.fuzzy_equals(clr1, 15) and WHITE.fuzzy_equals(clr2, 15) and WHITE.fuzzy_equals(clr3, 15):
        attempts += 1
        KEYBOARD.release(Key.shift_l)
        time.sleep(0.5)
        procced = True
        if shift_lock:
            tap_key(Key.shift_l)
            shift_lock = False
        _lockout_check()
        r1, g1, b1 = pag.pixel(LOCK_OUT1.x, LOCK_OUT1.y)
        r2, g2, b2 = pag.pixel(LOCK_OUT2.x, LOCK_OUT2.y)
        r3, g3, b3 = pag.pixel(LOCK_OUT3.x, LOCK_OUT3.y)
        clr1 = Color3(r1, g1, b1)
        clr2 = Color3(r2, g2, b2)
        clr3 = Color3(r3, g3, b3)
        time.sleep(3)
        if attempts >= 2:
            exit()
    if procced:
        raise Exception()


def do_ingredients(ingredients: list[pag.Point]):
    for point in ingredients:
        time.sleep(0.08)
        click_at(point)


def tap_key(key: str | Key):
    KEYBOARD.press(key)
    time.sleep(0.05)
    KEYBOARD.release(key)


def hold_key(key: str | Key, seconds: int | float):
    KEYBOARD.press(key)
    time.sleep(seconds)
    KEYBOARD.release(key)


def center_cursor():
    tap_key(Key.shift_l)
    time.sleep(0.05)
    tap_key(Key.shift_l)


def try_close_shop():
    time.sleep(0.1)
    x, y = MOUSE.position
    click_at(CLOSE_SHOP)
    send_low_level_mouse_move(x, y)


def end_cycle(id: int):
    global shift_lock
    hold_key('s', 1)
    tap_key(Key.shift_l)
    shift_lock = True
    time.sleep(0.08)
    for _ in range(10):
        x, y = MOUSE.position
        send_low_level_mouse_move(x, y+50)
        time.sleep(0.025)
    tap_key(Key.shift_l)
    shift_lock = False
    x, y = MOUSE.position
    click_at(pag.Point(x+100, y+225))
    time.sleep(34)
    lockout_check()
    x, y = MOUSE.position
    click_at(pag.Point(x, y))
    KEYBOARD.press('w')
    KEYBOARD.press('a')
    time.sleep(4)
    KEYBOARD.release('w')
    KEYBOARD.release('a')
    tap_key('e')
    hold_key('s', 1.2)
    for _ in range(16):
        tap_key('e')
        KEYBOARD.press('s')
        KEYBOARD.press('d')
        time.sleep(0.1)
        KEYBOARD.release('s')
        KEYBOARD.release('d')
        tap_key('e')
        time.sleep(0.05)


def end_cycle2(id: int):
    x, y = MOUSE.position
    click_at(pag.Point(x+100, y+225))
    time.sleep(34)
    lockout_check()
    x, y = MOUSE.position
    click_at(pag.Point(x, y))
    KEYBOARD.press('w')
    KEYBOARD.press('a')
    time.sleep(4)
    KEYBOARD.release('w')
    KEYBOARD.release('a')
    tap_key('e')
    hold_key('s', 1.2)
    for _ in range(20):
        tap_key('e')
        KEYBOARD.press('s')
        KEYBOARD.press('d')
        time.sleep(0.1)
        KEYBOARD.release('s')
        KEYBOARD.release('d')
        tap_key('e')
        time.sleep(0.05)


def ui_cycle() -> int:
    id, point = get_priority_recipe()
    click_at(point)
    if id == ID_CARROT: # 0
        do_ingredients(INGREDIENTS_CARROT)
    elif id == ID_CHAI: # 1
        do_ingredients(INGREDIENTS_CHAI)
    elif id == ID_PUMPKIN_PIE: # 2
        do_ingredients(INGREDIENTS_PUMPKIN_PIE)
    elif id == ID_PUMPKIN_SPICE: # 3
        do_ingredients(INGREDIENTS_PUMPKIN_SPICE)
    elif id == ID_SHORTBREAD: # 4
        do_ingredients(INGREDIENTS_SHORTBREAD)
    elif id == ID_BANANA: # 5
        do_ingredients(INGREDIENTS_BANANA)
    elif id == ID_CINNAMON: # 6
        do_ingredients(INGREDIENTS_CINNAMON)
    elif id == ID_CORN: # 7
        do_ingredients(INGREDIENTS_CORN)
    time.sleep(1)
    click_at(MIXER)
    time.sleep(16)
    click_at(MIXER)
    click_at(CLOSE)
    return id


def spawn_cycle():
    global shift_lock
    time.sleep(1)
    click_at(SPRINT)
    KEYBOARD.press(Key.shift_l)
    shift_lock = True
    hold_key('w', 0.5)
    hold_key('a', 7)
    hold_key('d', 0.9)
    hold_key('w', 0.5)
    tap_key('e')
    time.sleep(0.3)
    tap_key('e')
    hold_key('d', 1.37)
    hold_key('w', 5)
    hold_key('d', 0.3)
    hold_key('w', 7.2)
    hold_key('d', 4)
    hold_key('w', 1.7)
    KEYBOARD.press('d')
    time.sleep(3)
    tap_key(Key.space)
    time.sleep(0.5)
    KEYBOARD.release('d')
    hold_key('s', 1)
    KEYBOARD.release(Key.shift_l)
    hold_key('d', 0.5)


def respawn():
    tap_key(Key.esc)
    time.sleep(0.3)
    tap_key('r')
    time.sleep(0.3)
    tap_key(Key.enter)
    time.sleep(8)


def start() -> None:
    global shift_lock
    while True:
        try:
            lockout_check()

            click_at(CLOSE)
            respawn()
            lockout_check()

            spawn_cycle()
            lockout_check()

            tap_key(Key.shift_l)
            shift_lock = False
            tap_key('e')
            try_close_shop()
            lockout_check()

            id = ui_cycle()
            end_cycle(id)
            lockout_check()
            
            KEYBOARD.press('s')
            KEYBOARD.press('d')
            time.sleep(0.8)
            KEYBOARD.release('s')
            KEYBOARD.release('d')
            hold_key('w', 1.6)
            tap_key('e')
            try_close_shop()
            lockout_check()

            id2 = ui_cycle()
            lockout_check()
            
            KEYBOARD.press('s')
            KEYBOARD.press('d')
            time.sleep(1)
            KEYBOARD.release('s')
            KEYBOARD.release('d')
            hold_key('s', 0.5)
            center_cursor()
            hold_key('d', 0.2)
            lockout_check()

            end_cycle2(id2)
            lockout_check()

            KEYBOARD.press('s')
            KEYBOARD.press('d')
            time.sleep(0.8)
            KEYBOARD.release('s')
            KEYBOARD.release('d')
            hold_key('w', 1.6)
            tap_key('e')
            try_close_shop()
            lockout_check()

            id3 = ui_cycle()
            lockout_check()
            
            KEYBOARD.press('s')
            KEYBOARD.press('d')
            time.sleep(1)
            KEYBOARD.release('s')
            KEYBOARD.release('d')
            hold_key('s', 0.5)
            center_cursor()
            hold_key('d', 0.2)
            lockout_check()

            end_cycle2(id3)
            lockout_check()

            time.sleep(40)
        except Exception:
            pass


started = False


def listener():
    global started
    while True:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'l':
                if started:
                    exit()
                else:
                    started = True
                    threading.Thread(target=start, daemon=True).start()


if __name__ == "__main__":
    listener()