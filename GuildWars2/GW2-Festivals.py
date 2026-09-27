#Macropad, Hotkeys - Guild Wars 2 - Macro Template
from GEN_Methods_Library_v2 import GEN

none = (0x000000, '', [])

app = {
    'name' : 'GW2 - Festivals',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Gntlt',      lambda: GEN.keytimes([
            (GEN.F1,0.3), 
            (GEN.THREE,1.25),
            (GEN.ZERO,0.3),
            (GEN.SEVEN,0.3),
            (GEN.EIGHT,0.1),
            (GEN.EIGHT,0.3),    
            (GEN.FOUR,0.75),
            (GEN.TWO,3.0)
        ])),
        (0x000020, 'Frwks',      lambda: GEN.combos(8.0, [GEN.ONE,GEN.TWO,GEN.THREE,GEN.ONE,GEN.TWO,GEN.THREE,GEN.ONE,GEN.TWO,GEN.THREE])),
        none,
        
        # 2nd row ----------
        #(0x200000, '250x',  lambda: GEN.double_click(count=250, delay=0.1)),
        #(0x200000, '100x',  lambda: GEN.double_click(count=100, delay=0.1)),
        none,
        none,    
        (0x200000, '50x',  lambda: GEN.double_click(count=50, delay=0.1)),
        
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