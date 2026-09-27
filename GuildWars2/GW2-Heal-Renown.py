#Macropad, Hotkeys - Guild Wars 2 - Macro Template
from GEN_Methods_Library_v2 import GEN

#START_INPUT_DELAY = 0.5
#PRESS_DELAY = 0.1

#ONE = Keycode.ONE
#TWO = Keycode.TWO
#THREE = Keycode.THREE
#FOUR = Keycode.FOUR
#FIVE = Keycode.FIVE

none = (0x000000, '', [])

#def combos(delay, keys=[]):    
#    keylist = []
#
#    for key in keys:
#        keylist += [key, PRESS_DELAY, -key, delay]
#
#    return keylist

app = {
    'name' : 'GW2 - Heal Renown',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, '1-2-3',      lambda: GEN.combos(6.75, [GEN.ONE, GEN.TWO, GEN.THREE])),
        (0x000020, '2-3-4',      lambda: GEN.combos(6.75, [GEN.TWO, GEN.THREE, GEN.FOUR])),
        (0x000020, '3-4-5',      lambda: GEN.combos(6.75, [GEN.THREE, GEN.FOUR, GEN.FIVE])),

        # 2nd row ----------
        (0x000020, '2-3-5',      lambda: GEN.combos(6.75, [GEN.TWO, GEN.THREE, GEN.FIVE])),
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