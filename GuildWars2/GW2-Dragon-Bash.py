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

UP = Keycode.UP_ARROW
DOWN = Keycode.DOWN_ARROW
LEFT = Keycode.LEFT_ARROW
RIGHT = Keycode.RIGHT_ARROW
none = (0x000000, '', [])

def combos(delay, keys=[]):    
    keylist = []

    for key in keys:
        keylist += [key, PRESS_DELAY, -key, delay]

    return keylist




app = {
    'name' : 'GW2 - Dragon Bash',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Fire',      combos(8.0, [ONE,TWO,THREE,ONE,TWO,THREE,ONE,TWO,THREE])),
        none,
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