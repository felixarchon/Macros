#Macropad, Hotkeys - Helldivers 2 - Macro Template

from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.5
KEY_DELAY = 0.1

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

UP = Keycode.UP_ARROW
DOWN = Keycode.DOWN_ARROW
LEFT = Keycode.LEFT_ARROW
RIGHT = Keycode.RIGHT_ARROW

def mount(argv):    
    keys = [CTRL, KEY_DELAY, ALT, KEY_DELAY, SHFT, KEY_DELAY, argv, KEY_DELAY]
    return keys

app = {
    'name' : 'GW2 - Mounts',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'Rptr',      mount(R)),
        (0x000020, 'Sprng',     mount(S)),
        (0x000020, 'Skim',      mount(K)),

        # 2nd row ----------
        (0x002000, 'Jckl',      mount(J)),
        (0x002000, 'Grffn',     mount(G)),        
        (0x002000, 'RBtl',      mount(B)),

        # 3rd row ----------
        (0x200000, 'Skscl',     mount(A)),
        (0x200000, 'Trtl',      mount(T)),
        (0x200000, 'WarClw',    mount(C)),

        # 4th row ----------
        (0x000000, '',          []),
        (0x000000, '',          []),
        (0x000000, '',          []), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}