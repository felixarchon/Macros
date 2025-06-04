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

def gw2_thing(argv):
    keys = [CTRL, KEY_DELAY, ALT, KEY_DELAY, SHFT, KEY_DELAY, argv, KEY_DELAY]
    return keys

app = {
    'name' : 'GW2 - The Thing',
    'macros' : [
        # COLOR    LABEL        KEY SEQUENCE
        # 1st row ----------
        (0x000020, 'HMG',       gw2_thing(UP)),
        (0x000020, 'AC',        gw2_thing(DOWN)),
        (0x000020, 'Pack',      gw2_thing(DOWN)),

        # 2nd row ----------
        (0x002000, 'S-MG',      gw2_thing(DOWN)),
        (0x002000, 'S-Gat',     gw2_thing(DOWN)),        
        (0x002000, 'S-Roc',     gw2_thing(DOWN)),

        # 3rd row ----------
        (0x200000, 'O-120',     gw2_thing(RIGHT)),
        (0x200000, 'O-Prec',    gw2_thing(RIGHT)),
        (0x200000, 'O-Gat',     gw2_thing(RIGHT)),

        # 4th row ----------
        (0x302000, 'Resup',     gw2_thing(DOWN)),
        (0x302000, 'SOS',       gw2_thing(UP)),
        (0x302000, 'Reinf',     gw2_thing(UP)), 
        
        # Encoder button ---
        (0x000000, '',          []),
    ]
}