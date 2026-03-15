#Macropad, Hotkeys - Guild Wars 2 - Bells - Lower
from GEN_Methods_Library_v2 import GEN

none = (0x000000, '', [])

first = 0.471
#second = 0.46 #works but the last one was a touch too fast
second = 0.46
third = 0.47

eighth=1.0
quarter=2.0
half=3.0
whole=4.0

app = {
    'name' : 'GW2 - Bells Lower',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, '1st',      GEN.keytimes([
            (GEN.ONE,first*half), #1/2
            (GEN.TWO,first*half), #1/2
            (GEN.THREE,first*half), #1/2
            (GEN.FOUR,first*half), #1/2
            (GEN.SIX,first*half), #1/2
            (GEN.NINE,first*half), #1/2
            (GEN.EIGHT,first*half), #1/2
            (GEN.SEVEN,first*half), #1/2
            (GEN.EIGHT,first*half), #1/2
            (GEN.FOUR,first*half), #1/2
            (GEN.SIX,first*half), #1/2
            (GEN.TWO,first*half), #1/2
            (GEN.THREE,first*half), #1/2
            (GEN.FOUR,first*half), #1/2
            (GEN.THREE,first*half), #1/2
            (GEN.ONE,first*half), #1/2
            (GEN.SIX,0.0)
        ])),
        (0x000020, '2nd',      GEN.keytimes([
            (GEN.SIX,second*eighth), #1/8   1
            (GEN.NINE,second*eighth), #1/8  2
            (GEN.EIGHT,second*half), #1/2  3
            (GEN.SIX,second*quarter), #1/4   4
            (GEN.SEVEN,second*eighth), #1/8 5
            (GEN.EIGHT,second*half), #1/2  6
            (GEN.SEVEN,second*quarter), #1/4 7
            (GEN.SIX,second*eighth), #1/8   8
            (GEN.FOUR,second*half), #1/2   9
            (GEN.SIX,second*quarter), #1/4   10
            (GEN.FOUR,second*eighth), #1/8  11
            (GEN.EIGHT,second*whole), #1   12
            (GEN.SIX,second*eighth), #1/8   13
            (GEN.NINE,second*eighth), #1/8  14
            (GEN.EIGHT,second*half), #1/2  15
            (GEN.SIX,second*quarter), #1/4   16
            (GEN.SEVEN,second*eighth), #1/8 17
            (GEN.EIGHT,second*whole), #1   18
            (GEN.SIX,second*eighth), #1/8   19
            (GEN.NINE,second*eighth), #1/8  20
            (GEN.EIGHT,second*quarter), #1/4 21
            (GEN.SIX,second*eighth), #1/8   22
            (GEN.ONE,second*half), #1/2   23
            (GEN.ONE,0.0)
        ])),
        (0x000020, '3rd',      GEN.keytimes([
            (GEN.NINE,0.0),
            (GEN.SIX,0.0),
            (GEN.EIGHT,0.0),
            (GEN.EIGHT,0.0),
            (GEN.SIX,0.0),
            (GEN.THREE,0.0),
            (GEN.FOUR,0.0),
            (GEN.SIX,0.0),
            (GEN.NINE,0.0),
            (GEN.SIX,0.0),
            (GEN.EIGHT,0.0),
            (GEN.EIGHT,0.0),
            (GEN.SIX,0.0),
            (GEN.THREE,0.0),
            (GEN.FOUR,0.0),
            (GEN.SIX,0.0),
            (GEN.ONE,0.0)
        ])),

        # 2nd row ----------
        (0x000020, '4th',      GEN.keytimes([
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0)
        ])),
        (0x000020, '5th',      GEN.keytimes([
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0)
        ])),
        (0x000020, '6th',      GEN.keytimes([
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0),
            (GEN.ZERO,0.0)
        ])),

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