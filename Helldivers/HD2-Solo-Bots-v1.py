#Macropad, Hotkeys - Helldivers 2 - Early Solo Build

from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.5
KEY_DELAY = 0.1

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
    'name' : 'HD2 - Solo Bot Runs',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'HMG',       stratagem(DOWN, LEFT, UP, DOWN, DOWN)),
        (0x000020, 'AC',        stratagem(DOWN,LEFT,DOWN,UP,UP,RIGHT)),
        (0x000020, 'Pack',      stratagem(DOWN,LEFT,DOWN,UP,UP,DOWN)),

        # 2nd row ----------
        (0x002000, 'S-MG',      stratagem(DOWN,UP,RIGHT,RIGHT,UP)),
        (0x002000, 'S-AC',      stratagem(DOWN,UP,RIGHT,UP, LEFT, UP)),        
        (0x002000, 'S-Roc',     stratagem(DOWN,UP,RIGHT,RIGHT,LEFT)),

        # 3rd row ----------
        (0x200000, 'O-120',     stratagem(RIGHT,RIGHT,DOWN,LEFT,RIGHT,DOWN)),
        (0x200000, 'O-Prec',    stratagem(RIGHT,RIGHT,UP)),
        (0x200000, 'O-Gat',     stratagem(RIGHT,DOWN,LEFT,UP,UP)),

        # 4th row ----------
        (0x302000, 'Resup',     stratagem(DOWN, DOWN, UP, RIGHT)),
        (0x302000, 'SOS',       stratagem(UP, DOWN, RIGHT, UP)),
        (0x302000, 'Reinf',     stratagem(UP, DOWN, RIGHT, LEFT, UP)), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}