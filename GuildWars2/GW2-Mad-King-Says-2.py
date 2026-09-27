#Macropad, Hotkeys - Guild Wars 2 - Mad King Says Part 1
from GEN_Methods_Library_v2 import GEN

none = (0x000000, '', [])

app = {
    'name' : 'GW2 - Mad King Says 2',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Sit',      lambda: GEN.emotes([GEN.S,GEN.I,GEN.T])),
        (0x002000, 'Sleep',      lambda: GEN.emotes([GEN.S,GEN.L,GEN.E,GEN.E,GEN.P])),
        (0x000020, 'Srprsd',      lambda: GEN.emotes([GEN.S,GEN.U,GEN.R,GEN.P,GEN.R,GEN.I,GEN.S,GEN.E,GEN.D])),
        
        # 2nd row ----------
        (0x002000, 'Thrtn',      lambda: GEN.emotes([GEN.T,GEN.H,GEN.R,GEN.E,GEN.A,GEN.T,GEN.E,GEN.N])),
        (0x000020, 'Wave',      lambda: GEN.emotes([GEN.W,GEN.A,GEN.V,GEN.E])),       
        (0x002000, 'Yes',      lambda: GEN.emotes([GEN.Y,GEN.E,GEN.S])),

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