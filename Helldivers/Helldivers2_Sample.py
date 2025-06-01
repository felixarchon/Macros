# MACROPAD Hotkeys: Helldiver II

from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.4
KEY_DELAY = 0.05

START_INPUT = Keycode.CONTROL

UP = Keycode.W
DOWN = Keycode.S
LEFT = Keycode.A
RIGHT = Keycode.D

def stratagem(*argv):
    keys = [START_INPUT, START_INPUT_DELAY]

    for key in argv:
        keys += [key, KEY_DELAY, -key, KEY_DELAY]

    return keys

app = {
    'name' : 'Helldivers II',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'M-GUN',     stratagem(DOWN, LEFT, DOWN, UP, RIGHT)),
        (0x000000, '',          []),
        (0x000000, '',          []),

        # 2nd row ----------
        (0x200000, 'Prec',      stratagem(RIGHT, RIGHT, UP)),
        (0x200000, 'Gat',       stratagem(RIGHT, DOWN, LEFT, UP, UP)),        
        (0x000000, '',          []),

        # 3rd row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x302000, 'Nape',      stratagem(UP, RIGHT, DOWN, UP)),

        # 4th row ----------
        (0x202000, 'Resup',     stratagem(DOWN, DOWN, UP, RIGHT)),
        (0x002000, 'SOS',       stratagem(UP, DOWN, RIGHT, UP)),
        (0x002000, 'Reinf',     stratagem(UP, DOWN, RIGHT, LEFT, UP)), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}