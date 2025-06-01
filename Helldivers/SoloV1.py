# MACROPAD Hotkeys: Helldiver II

from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.4
KEY_DELAY = 0.05

START_INPUT = Keycode.CONTROL

UP = Keycode.UP_ARROW
DOWN = Keycode.DOWN_ARROW
LEFT = Keycode.LEFT_ARROW
RIGHT = Keycode.RIGHT_ARROW

def stratagem(*argv):
    keys = [START_INPUT, START_INPUT_DELAY]

    for key in argv:
        keys += [key, KEY_DELAY, -key, KEY_DELAY]

    return keys

app = {
    'name' : 'HD2 - Solo Runs',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'M-GUN',     stratagem(DOWN, LEFT, DOWN, UP, RIGHT)),
        (0x000020, 'HM-GUN',    stratagem(DOWN, LEFT, UP, DOWN, DOWN)),
        (0x000020, 'A-CAN',     stratagem(DOWN,LEFT,DOWN,UP,UP,RIGHT)),

        # 2nd row ----------
        (0x200000, 'S-MG',      stratagem(DOWN,UP,RIGHT,RIGHT,UP)),
        (0x200000, 'S-Gat',     stratagem(DOWN,UP,RIGHT,LEFT)),        
        (0x200000, 'S-Roc',     stratagem(DOWN,UP,RIGHT,RIGHT,LEFT)),

        # 3rd row ----------
        (0x000000, '120',       stratagem(RIGHT,RIGHT,DOWN,LEFT,RIGHT,DOWN)),
        (0x000000, '',          []),
        (0x302000, '',          []),

        # 4th row ----------
        (0x002000, 'Resup',     stratagem(DOWN, DOWN, UP, RIGHT)),
        (0x002000, 'SOS',       stratagem(UP, DOWN, RIGHT, UP)),
        (0x002000, 'Reinf',     stratagem(UP, DOWN, RIGHT, LEFT, UP)), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}