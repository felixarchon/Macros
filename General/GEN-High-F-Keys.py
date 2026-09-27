#Macropad, High F Keys
from GEN_Methods_Library_v2 import GEN

none = (0x000000, '', [])

app = {
    'name' : 'High F Keys',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'F24',        lambda: GEN.keypress(GEN.F24)),
        (0x000020, 'F23',        lambda: GEN.keypress(GEN.F23)),
        (0x000020, 'F22',        lambda: GEN.keypress(GEN.F22)),

        # 2nd row ----------
        (0x000020, 'F21',        lambda: GEN.keypress(GEN.F21)),
        (0x000020, 'F20',        lambda: GEN.keypress(GEN.F20)),
        (0x000020, 'F19',        lambda: GEN.keypress(GEN.F19)),

        # 3rd row ----------
        (0x000020, 'F18',        lambda: GEN.keypress(GEN.F18)),
        (0x000020, 'F17',        lambda: GEN.keypress(GEN.F17)),
        (0x000020, 'F16',        lambda: GEN.keypress(GEN.F16)),

        # 4th row ----------
        (0x000020, 'F15',        lambda: GEN.keypress(GEN.F15)),
        (0x000020, 'F14',        lambda: GEN.keypress(GEN.F14)),
        (0x000020, 'F13',        lambda: GEN.keypress(GEN.F13)),
        
        # Encoder button ---
        none,
    ]
}