#Macropad, Hotkeys - Guild Wars 2 - Macro Template

from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.5
PRESS_DELAY = 0.1

ONE = Keycode.ONE
TWO = Keycode.TWO
THREE = Keycode.THREE
FOUR = Keycode.FOUR
FIVE = Keycode.FIVE

none = (0x000000, '', [])

def combos(delay, keys=[]):    
    keylist = []

    for key in keys:
        keylist += [key, PRESS_DELAY, -key, delay]

    return keylist

app = {
    'name' : 'GW2 - Heal Renown',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, '1-2-3',      combos(6.75, [ONE, TWO, THREE])),
        (0x000020, '2-3-4',      combos(6.75, [TWO, THREE, FOUR])),
        (0x000020, '3-4-5',      combos(6.75, [THREE, FOUR, FIVE])),

        # 2nd row ----------
        (0x000020, '2-3-5',      combos(6.75, [TWO, THREE, FIVE])),
        none,        
        none,

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