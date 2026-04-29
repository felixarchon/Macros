from adafruit_hid.keycode import Keycode

# This file goes in the root directory (same as code.py)
class GEN:
    #Timings
    START_STRATAGEM_INPUT_DELAY = 0.5    
    STRATAGEM_KEY_DELAY = 0.1    
    PRESS_DELAY = 0.1
    JIGGLER_DELAY = 60.0

    START_STRATAGEM = Keycode.CONTROL


    #Arrow Keys
    UP = Keycode.UP_ARROW
    DOWN = Keycode.DOWN_ARROW
    LEFT = Keycode.LEFT_ARROW
    RIGHT = Keycode.RIGHT_ARROW

    #Mouse Directions
    M_UP = {'y':-10}
    M_DOWN = {'y':10}
    M_LEFT = {'x':-10}
    M_RIGHT = {'x':10}

    #Letter Keys
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

    #Numbers
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

    CTRL = Keycode.CONTROL
    ALT = Keycode.ALT
    SHFT = Keycode.SHIFT
    DEL = Keycode.DELETE
    SPACE = Keycode.SPACE
    ENTER = Keycode.ENTER
    TAB = Keycode.TAB
    INS = Keycode.INSERT
    CAPLOCK = Keycode.CAPS_LOCK

    #Function Keys
    F1 = Keycode.F1
    F2 = Keycode.F2
    F3 = Keycode.F3
    F4 = Keycode.F4
    F5 = Keycode.F5
    F6 = Keycode.F6
    F7 = Keycode.F7
    F8 = Keycode.F8
    F9 = Keycode.F9
    F10 = Keycode.F10
    F11 = Keycode.F11
    F12 = Keycode.F12
    F13 = Keycode.F13
    F14 = Keycode.F14
    F15 = Keycode.F15
    F16 = Keycode.F16
    F17 = Keycode.F17
    F18 = Keycode.F18
    F19 = Keycode.F19
    F20 = Keycode.F20
    F21 = Keycode.F21
    F22 = Keycode.F22
    F23 = Keycode.F23
    F24 = Keycode.F24

    #Colors
    Support = 0x000020

    #Methods
    @staticmethod
    def jiggler(repeats, keys=[]):    
        keylist = []
        repeat = int(repeats)

        for i in range(repeat):
            for key in keys:
                keylist += [GEN.JIGGLER_DELAY, key]

        return keylist

    #from hd2
    @staticmethod
    def stratagem(*argv):
        keys = [GEN.START_STRATAGEM, GEN.START_STRATAGEM_INPUT_DELAY]

        for key in argv:
            keys += [key, GEN.STRATAGEM_KEY_DELAY, -key, GEN.STRATAGEM_KEY_DELAY]

        return keys
    


    #from gw2 fireworks
    @staticmethod
    def combos(delay, keys=[]):
        if keys is None:
            keys=[]
    
        keylist = []

        for key in keys:
            keylist += [key, GEN.PRESS_DELAY, -key, delay]

        return keylist

    @staticmethod
    def keytimes(keytimes=None):
        if keytimes is None:
            keytimes=[]

        keylist=[]

        for key, delay in keytimes:
            keylist += [key, GEN.PRESS_DELAY, -key, delay]

        return keylist
    

    @staticmethod
    def keypress(*argv):    
        keylist = []

        for key in argv:
            keylist += [key, GEN.PRESS_DELAY, -key, GEN.PRESS_DELAY]

        return keylist
    
    @staticmethod
    def shortcuts(keys=[]):    
        keylist = []

        for key in keys:
            keylist += [key]

        return keylist
