#Macropad, Hotkeys - Guild Wars 2 - Macro Template

from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.5
PRESS_DELAY = 0.1
KEY_DELAY = 60.0

UP = Keycode.UP_ARROW
DOWN = Keycode.DOWN_ARROW
LEFT = Keycode.LEFT_ARROW
RIGHT = Keycode.RIGHT_ARROW
none = (0x000000, '', [])

def combos(repeats, keys=[]):    
    keylist = []

    for i in range(repeats):
        for key in keys:
            keylist += [KEY_DELAY, key, PRESS_DELAY, -key ]

    return keylist




app = {
    'name' : 'GW2 - Activity',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, '4m',        combos(1.0, [UP, DOWN, LEFT, RIGHT])),
        (0x000020, '12m',       combos(3.0, [UP, DOWN, LEFT, RIGHT])),
        (0x000020, '16m',       combos(4.0, [UP, DOWN, LEFT, RIGHT])),

        # 2nd row ----------
        (0x000020, '20m',       combos(5.0, [UP, DOWN, LEFT, RIGHT])),
        (0x000020, '40m',       combos(10.0, [UP, DOWN, LEFT, RIGHT])),
        (0x000020, '1h',        combos(15.0, [UP, DOWN, LEFT, RIGHT])),

        # 3rd row ----------
        none,
        none,
        none,

        # 4th row ----------
        none,
        none,
        none,
        
        # Encoder button ---
        none,
    ]
}