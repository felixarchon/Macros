#Macropad, Mouse Jiggler

from adafruit_hid.mouse import Mouse

KEY_DELAY = 60.0

M_UP = {'y':-10}
M_DOWN = {'y':10}
M_LEFT = {'x':-10}
M_RIGHT = {'x':10}

none = (0x000000, '', [])

def combos(repeats, keys=[]):    
    keylist = []
    repeat = int(repeats)

    for i in range(repeat):
        for key in keys:
            keylist += [KEY_DELAY, key]

    return keylist


app = {
    'name' : 'Mouse Jiggler',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, '4m',        combos(1.0, [M_UP, M_DOWN, M_LEFT, M_RIGHT])),
        (0x000020, '8m',        combos(2.0, [M_UP, M_DOWN, M_LEFT, M_RIGHT])),
        (0x000020, '12m',       combos(3.0, [M_UP, M_DOWN, M_LEFT, M_RIGHT])),

        # 2nd row ----------
        (0x000020, '20m',       combos(5.0, [M_UP, M_DOWN, M_LEFT, M_RIGHT])),
        (0x000020, '40m',       combos(10.0, [M_UP, M_DOWN, M_LEFT, M_RIGHT])),
        (0x000020, '1h',        combos(15.0, [M_UP, M_DOWN, M_LEFT, M_RIGHT])),

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