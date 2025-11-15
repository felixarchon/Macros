#Macropad, Hotkeys - Visual Studio
from GEN_Methods_Library import GEN_Base

gen = GEN_Base()


none = (0x000000, '', [])



#(0x000020, 'Gntlt',      [F1,PRESS_DELAY,-F1,    0.2,THREE,PRESS_DELAY,-THREE,     1.0,ZERO,PRESS_DELAY,-ZERO,      0.2,SEVEN,PRESS_DELAY,-SEVEN,     0.2,EIGHT,PRESS_DELAY,-EIGHT,     0.2,FOUR,PRESS_DELAY,-FOUR,    0.2,TWO,PRESS_DELAY,-TWO]),

app = {
    'name' : 'VS - Code Editing 1',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Word',      gen.shortcuts([gen.CTRL,gen.SPACE])),
        (0x000020, 'SigHlp',    gen.shortcuts([gen.CTRL,gen.SHFT,gen.SPACE])),
        (0x000020, 'MvUp',      gen.shortcuts([gen.ALT,gen.UP])),
        
        # 2nd row ----------
        (0x000020, 'Dup',      gen.shortcuts([gen.CTRL,gen.D])),
        (0x000020, 'Del',      gen.shortcuts([gen.CTRL,gen.SHFT,gen.ENTER])),
        (0x000020, 'MvDn',     gen.shortcuts([gen.ALT,gen.DOWN])),

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