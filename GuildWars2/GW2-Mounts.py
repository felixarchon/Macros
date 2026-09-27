#Macropad, Hotkeys - Guild Wars 2 - Macro Template

from GEN_Methods_Library_v2 import GEN

app = {
    'name' : 'GW2 - Mounts',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Rptr',      lambda: GEN.mount(GEN.R)),
        (0x000020, 'Sprng',     lambda: GEN.mount(GEN.S)),
        (0x000020, 'Skim',      lambda: GEN.mount(GEN.K)),

        # 2nd row ----------
        (0x002000, 'Jckl',      lambda: GEN.mount(GEN.J)),
        (0x002000, 'Grffn',     lambda: GEN.mount(GEN.G)),        
        (0x002000, 'RBtl',      lambda: GEN.mount(GEN.B)),

        # 3rd row ----------
        (0x200000, 'Skscl',     lambda: GEN.mount(GEN.A)),
        (0x200000, 'Trtl',      lambda: GEN.mount(GEN.T)),
        (0x200000, 'WarClw',    lambda: GEN.mount(GEN.C)),

        # 4th row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000000, '',          []), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}