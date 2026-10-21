#Macropad, NVDA Shortcuts - 1
from GEN_Methods_Library_v2 import GEN

none = (0x000000, '', [])

app = {
    'name' : 'NVDA - 1',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'V/T-Tog',     lambda: GEN.shortcuts([GEN.INS,GEN.SPACE])), #Toggle between Virtual Cursor and Tabbing
        (0x000020, 'Exit',        lambda: GEN.shortcuts([GEN.INS,GEN.Q])), #Quit / Exit
        (0x000020, 'Pause',       lambda: GEN.shortcuts([GEN.INS,GEN.SHFT, GEN.S])), #Sleep / Pause / Wakeup

        # 2nd row ----------
        (0x000020, 'List',        lambda: GEN.shortcuts([GEN.INS,GEN.F7])), # Show Element Lists
        none,
        none,

        # 3rd row ----------
        none,
        none,
        (0x000020, 'Exit 2',      lambda: GEN.combos(0.1, [GEN.TAB, GEN.ENTER] )), #Quit / Exit

        # 4th row ----------
        none,
        none,
        (0x000020, 'Strt',        lambda: GEN.shortcuts([GEN.CTRL,GEN.ALT,GEN.N])), # Show Element Lists
        
        # Encoder button ---
        none,
    ]
}