#Macropad, Hotkeys - Guild Wars 2 - Mad King Says Part 1
from GEN_Methods_Library_v2 import GEN

none = (0x000000, '', [])

app = {
    'name' : 'GW2 - Mad King Says 1',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Beckon',    lambda: GEN.emotes([GEN.B,GEN.E,GEN.C,GEN.K,GEN.O,GEN.N])),
        (0x002000, 'Bow',       lambda: GEN.emotes([GEN.B,GEN.O,GEN.W])),
        (0x000020, 'Cheer',     lambda: GEN.emotes([GEN.C,GEN.H,GEN.E,GEN.E,GEN.R])),
        
        # 2nd row ----------
        (0x002000, 'Cower',     lambda: GEN.emotes([GEN.C,GEN.O,GEN.W,GEN.E,GEN.R])),
        (0x000020, 'Dance',     lambda: GEN.emotes([GEN.D,GEN.A,GEN.N,GEN.C,GEN.E])),       
        (0x002000, 'Kneel',     lambda: GEN.emotes([GEN.K,GEN.N,GEN.E,GEN.E,GEN.L])),

        # 3rd row ----------
        (0x000020, 'Laugh',     lambda: GEN.emotes([GEN.L,GEN.A,GEN.U,GEN.G,GEN.H])),
        (0x002000, 'No',        lambda: GEN.emotes([GEN.N,GEN.O])),
        (0x000020, 'Point',     lambda: GEN.emotes([GEN.P,GEN.O,GEN.I,GEN.N,GEN.T])),

        # 4th row ----------
        (0x002000, 'Ponder',    lambda: GEN.emotes([GEN.P,GEN.O,GEN.N,GEN.D,GEN.E,GEN.R])),
        (0x000020, 'Salute',    lambda: GEN.emotes([GEN.S,GEN.A,GEN.L,GEN.U,GEN.T,GEN.E])),
        (0x002000, 'Shrug',     lambda: GEN.emotes([GEN.S,GEN.H,GEN.R,GEN.U,GEN.G])),
        
        # Encoder button ---
        none,
    ]
}