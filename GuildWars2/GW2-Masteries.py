#Macropad, Hotkeys - Guild Wars 2 - Macro Template
from GEN_Methods_Library_v2 import GEN

app = {
    'name' : 'GW2 - Masteries',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Fish',      lambda: GEN.mastery(GEN.F)),
        (0x000020, 'Skiff',     lambda: GEN.mastery(GEN.S)),
        (0x000020, 'Bot',       lambda: GEN.mastery(GEN.J)),

        # 2nd row ----------
        (0x002000, 'Rift',      lambda: GEN.mastery(GEN.R)),
        (0x002000, 'Door',      lambda: GEN.mastery(GEN.D)),        
        (0x000000, '',          []),

        # 3rd row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000000, '',          []),

        # 4th row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000000, '',          []), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}