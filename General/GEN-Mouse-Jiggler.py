#Macropad, Mouse Jiggler

from GEN_Methods_Library_v2 import GEN

none = (0x000000, '', [])

app = {
    'name' : 'Mouse Jiggler',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, '4m',        lambda: GEN.jiggler(1.0, [GEN.M_UP, GEN.M_DOWN, GEN.M_LEFT, GEN.M_RIGHT])),
        (0x000020, '8m',        lambda: GEN.jiggler(2.0, [GEN.M_UP, GEN.M_DOWN, GEN.M_LEFT, GEN.M_RIGHT])),
        (0x000020, '12m',       lambda: GEN.jiggler(3.0, [GEN.M_UP, GEN.M_DOWN, GEN.M_LEFT, GEN.M_RIGHT])),

        # 2nd row ----------
        (0x000020, '20m',       lambda: GEN.jiggler(5.0, [GEN.M_UP, GEN.M_DOWN, GEN.M_LEFT, GEN.M_RIGHT])),
        (0x000020, '40m',       lambda: GEN.jiggler(10.0, [GEN.M_UP, GEN.M_DOWN, GEN.M_LEFT, GEN.M_RIGHT])),
        (0x000020, '1h',        lambda: GEN.jiggler(15.0, [GEN.M_UP, GEN.M_DOWN, GEN.M_LEFT, GEN.M_RIGHT])),

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