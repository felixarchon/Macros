#Macropad, Hotkeys - Guild Wars 2 - Macro Template

from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.5
PRESS_DELAY = 0.1

CTRL = Keycode.CONTROL
ALT = Keycode.ALT
SHFT = Keycode.SHIFT

A = Keycode.A
B = Keycode.B
C = Keycode.C
D = Keycode.D
E = Keycode.E
F = Keycode.F
G = Keycode.G
H = Keycode.H
I = Keycode.I
J = Keycode.J
K = Keycode.K
L = Keycode.L
M = Keycode.M
N = Keycode.N
O = Keycode.O
P = Keycode.P
Q = Keycode.Q
R = Keycode.R
S = Keycode.S
T = Keycode.T
U = Keycode.U
V = Keycode.V
W = Keycode.W
X = Keycode.X
Y = Keycode.Y
Z = Keycode.Z
ONE = Keycode.ONE
TWO = Keycode.TWO
THREE = Keycode.THREE
FOUR = Keycode.FOUR
FIVE = Keycode.FIVE
SIX = Keycode.SIX
SEVEN = Keycode.SEVEN
EIGHT = Keycode.EIGHT
NINE = Keycode.NINE
ZERO = Keycode.ZERO

UP = Keycode.UP_ARROW
DOWN = Keycode.DOWN_ARROW
LEFT = Keycode.LEFT_ARROW
RIGHT = Keycode.RIGHT_ARROW

F1 = Keycode.F1

none = (0x000000, '', [])

def combos(delay, keys=[]):    
    keylist = []

    for key in keys:
        keylist += [key, PRESS_DELAY, -key, delay]

    return keylist

def keytimes(keytimes=[]):
        keylist=[]

        for key, delay in keytimes:
            keylist += [key, PRESS_DELAY, -key, delay]

        return keylist

#(0x000020, 'Gntlt',      [F1,PRESS_DELAY,-F1,    0.2,THREE,PRESS_DELAY,-THREE,     1.0,ZERO,PRESS_DELAY,-ZERO,      0.2,SEVEN,PRESS_DELAY,-SEVEN,     0.2,EIGHT,PRESS_DELAY,-EIGHT,     0.2,FOUR,PRESS_DELAY,-FOUR,    0.2,TWO,PRESS_DELAY,-TWO]),

app = {
    'name' : 'GW2 - Festivals',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Gntlt',      keytimes([
            (F1,0.3), 
            (THREE,1.25),
            (ZERO,0.3),
            (SEVEN,0.3),
            (EIGHT,0.3),
            (FOUR,0.3),
            (TWO,3.0)
        ])),
        (0x000020, 'Frwks',      combos(8.0, [ONE,TWO,THREE,ONE,TWO,THREE,ONE,TWO,THREE])),
        none,
        
        # 2nd row ----------
        none,
        none,        
        none,

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