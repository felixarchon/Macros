#Macropad, Hotkeys - Guild Wars 2 - Bells - Lower
from GEN_Methods_Library import GEN_Base

g = GEN_Base()

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
        (0x000020, '1st',      g.keytimes([
            (g.ONE,first*half), #1/2
            (g.TWO,first*half), #1/2
            (g.THREE,first*half), #1/2
            (g.FOUR,first*half), #1/2
            (g.SIX,first*half), #1/2
            (g.NINE,first*half), #1/2
            (g.EIGHT,first*half), #1/2
            (g.SEVEN,first*half), #1/2
            (g.EIGHT,first*half), #1/2
            (g.FOUR,first*half), #1/2
            (g.SIX,first*half), #1/2
            (g.TWO,first*half), #1/2
            (g.THREE,first*half), #1/2
            (g.FOUR,first*half), #1/2
            (g.THREE,first*half), #1/2
            (g.ONE,first*half), #1/2
            (g.SIX,0.0)
        ])),
        (0x000020, '2nd',      g.keytimes([
            (g.SIX,second*eighth), #1/8   1
            (g.NINE,second*eighth), #1/8  2
            (g.EIGHT,second*half), #1/2  3
            (g.SIX,second*quarter), #1/4   4
            (g.SEVEN,second*eighth), #1/8 5
            (g.EIGHT,second*half), #1/2  6
            (g.SEVEN,second*quarter), #1/4 7
            (g.SIX,second*eighth), #1/8   8
            (g.FOUR,second*half), #1/2   9
            (g.SIX,second*quarter), #1/4   10
            (g.FOUR,second*eighth), #1/8  11
            (g.EIGHT,second*whole), #1   12
            (g.SIX,second*eighth), #1/8   13
            (g.NINE,second*eighth), #1/8  14
            (g.EIGHT,second*half), #1/2  15
            (g.SIX,second*quarter), #1/4   16
            (g.SEVEN,second*eighth), #1/8 17
            (g.EIGHT,second*whole), #1   18
            (g.SIX,second*eighth), #1/8   19
            (g.NINE,second*eighth), #1/8  20
            (g.EIGHT,second*quarter), #1/4 21
            (g.SIX,second*eighth), #1/8   22
            (g.ONE,second*half), #1/2   23
            (g.ONE,0.0)
        ])),
        (0x000020, '3rd',      g.keytimes([
            (g.NINE,0.0),
            (g.SIX,0.0),
            (g.EIGHT,0.0),
            (g.EIGHT,0.0),
            (g.SIX,0.0),
            (g.THREE,0.0),
            (g.FOUR,0.0),
            (g.SIX,0.0),
            (g.NINE,0.0),
            (g.SIX,0.0),
            (g.EIGHT,0.0),
            (g.EIGHT,0.0),
            (g.SIX,0.0),
            (g.THREE,0.0),
            (g.FOUR,0.0),
            (g.SIX,0.0),
            (g.ONE,0.0)
        ])),

        # 2nd row ----------
        (0x000020, '4th',      g.keytimes([
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0)
        ])),
        (0x000020, '5th',      g.keytimes([
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0)
        ])),
        (0x000020, '6th',      g.keytimes([
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0),
            (g.ZERO,0.0)
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