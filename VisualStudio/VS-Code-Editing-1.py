#Macropad, Hotkeys - Visual Studio
from GEN_Methods_Library_v2 import GEN

none = (0x000000, '', [])

app = {
    'name' : 'VS - Code Editing 1',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Word',      GEN.shortcuts([GEN.CTRL,GEN.SPACE])),
        (0x000020, 'SigHlp',    GEN.shortcuts([GEN.CTRL,GEN.SHFT,GEN.SPACE])),
        (0x000020, 'MvUp',      GEN.shortcuts([GEN.ALT,GEN.UP])),
        
        # 2nd row ----------
        (0x000020, 'Dup',      GEN.shortcuts([GEN.CTRL,GEN.D])),
        (0x000020, 'Del',      GEN.shortcuts([GEN.CTRL,GEN.SHFT,GEN.ENTER])),
        (0x000020, 'MvDn',     GEN.shortcuts([GEN.ALT,GEN.DOWN])),

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