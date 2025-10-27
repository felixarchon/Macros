#Macropad, Hotkeys - Guild Wars 2 - Mad King Says Part 1
from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.1
PRESS_DELAY = 0.05

CTRL = Keycode.CONTROL
ALT = Keycode.ALT
SHFT = Keycode.SHIFT
ENTER = Keycode.ENTER

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

FSLASH = Keycode.FORWARD_SLASH

F1 = Keycode.F1

none = (0x000000, '', [])

def emotes(keys=[]):    
    keylist = []

    keylist += [FSLASH, PRESS_DELAY, -FSLASH, PRESS_DELAY]

    for key in keys:
        keylist += [key, PRESS_DELAY, -key, PRESS_DELAY]
    
    keylist += [ENTER, PRESS_DELAY, -ENTER, PRESS_DELAY]

    return keylist


#(0x000020, 'Gntlt',      [F1,PRESS_DELAY,-F1,    0.2,THREE,PRESS_DELAY,-THREE,     1.0,ZERO,PRESS_DELAY,-ZERO,      0.2,SEVEN,PRESS_DELAY,-SEVEN,     0.2,EIGHT,PRESS_DELAY,-EIGHT,     0.2,FOUR,PRESS_DELAY,-FOUR,    0.2,TWO,PRESS_DELAY,-TWO]),

app = {
    'name' : 'GW2 - Mad King Says 2',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Sit',      emotes([S,I,T])),
        (0x002000, 'Sleep',      emotes([S,L,E,E,P])),
        (0x000020, 'Srprsd',      emotes([S,U,R,P,R,I,S,E,D])),
        
        # 2nd row ----------
        (0x002000, 'Thrtn',      emotes([T,H,R,E,A,T,E,N])),
        (0x000020, 'Wave',      emotes([W,A,V,E])),       
        (0x002000, 'Yes',      emotes([Y,E,S])),

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