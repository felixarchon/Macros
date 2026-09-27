#Macropad, Hotkeys - Guild Wars 2 - Macro Template

from GEN_Methods_Library_v2 import GEN

app = {
    'name' : 'GW2 - Activity',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, '4m',        lambda: GEN.combos(1.0, [GEN.UP, GEN.DOWN, GEN.LEFT, GEN.RIGHT])),
        (0x000020, '12m',       lambda: GEN.combos(3.0, [GEN.UP, GEN.DOWN, GEN.LEFT, GEN.RIGHT])),
        (0x000020, '16m',       lambda: GEN.combos(4.0, [GEN.UP, GEN.DOWN, GEN.LEFT, GEN.RIGHT])),

        # 2nd row ----------
        (0x000020, '20m',       lambda: GEN.combos(5.0, [GEN.UP, GEN.DOWN, GEN.LEFT, GEN.RIGHT])),
        (0x000020, '40m',       lambda: GEN.combos(10.0, [GEN.UP, GEN.DOWN, GEN.LEFT, GEN.RIGHT])),
        (0x000020, '1h',        lambda: GEN.combos(15.0, [GEN.UP, GEN.DOWN, GEN.LEFT, GEN.RIGHT])),

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