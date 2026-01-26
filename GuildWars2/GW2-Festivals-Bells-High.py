#Macropad, Hotkeys - Guild Wars 2 - Bells - High
from adafruit_hid.keycode import Keycode

PRESS_DELAY = 0.1

ONE = Keycode.ONE
TWO = Keycode.TWO
THREE = Keycode.THREE
FOUR = Keycode.FOUR
FIVE = Keycode.FIVE
SIX = Keycode.SIX
SEVEN = Keycode.SEVEN
EIGHT = Keycode.EIGHT
NINE = Keycode.NINE
ZERO = Keycode.ZERO

none = (0x000000, '', [])

def keytimes(keytimes=[]):
        keylist=[]

        for key, delay in keytimes:
            keylist += [key, PRESS_DELAY, -key, delay]

        return keylist

app = {
    'name' : 'GW2 - Bells High',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, '1st',      keytimes([
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
        ])),
        (0x000020, '2nd',      keytimes([
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
        ])),
        (0x000020, '3rd',      keytimes([
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
        ])),

        # 2nd row ----------
        (0x000020, '4th',      keytimes([
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
        ])),
        (0x000020, '5th',      keytimes([
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
        ])),
        (0x000020, '6th',      keytimes([
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
            (ZERO,3.0),
        ])),

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