from adafruit_hid.keycode import Keycode

# This file goes in the root directory (same as code.py)
class GEN_Base:
    #Timings
    @property
    def START_STRATAGEM_INPUT_DELAY(self): 
        return 0.5    
    @property
    def STRATAGEM_KEY_DELAY(self): 
        return 0.1

    @property
    def JIGGLER_DELAY(self):
        return 60.0

  
    @property
    def START_STRATAGEM(self): 
        return Keycode.CONTROL


    #Arrow Keys
    @property
    def UP(self): 
        return Keycode.UP_ARROW
    @property
    def DOWN(self): 
        return Keycode.DOWN_ARROW
    @property
    def LEFT(self): 
        return Keycode.LEFT_ARROW
    @property
    def RIGHT(self): 
        return Keycode.RIGHT_ARROW

    #Mouse Directions
    @property
    def M_UP(self):
        return {'y':-10}

    @property
    def M_DOWN(self):
        return {'y':10}

    @property
    def M_LEFT(self):
        return {'x':-10}

    @property
    def M_RIGHT(self):
        return {'x':10}


    #Extra Keys
    @property
    def CTRL(self):
        return Keycode.CONTROL

    @property        
    dev ALT(self):
        return Keycode.ALT

    @property
    def SHFT(self):
        return Keycode.SHIFT

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

    #Function Keys
    F1 = Keycode.F1


    #Colors
    @property
    def Support(self): 
        return 0x000020



    #Methods
    @property
    def jiggler(self, repeats, keys=[]):    
        keylist = []
        repeat = int(repeats)

        for i in range(repeat):
            for key in keys:
                keylist += [self.JIGGLER_DELAY, key]

        return keylist

    #from hd2
    @property
    def stratagem(self, *argv):
        keys = [self.START_STRATAGEM, self.START_STRATAGEM_INPUT_DELAY]

        for key in argv:
            keys += [key, self.STRATAGEM_KEY_DELAY, -key, self.STRATAGEM_KEY_DELAY]

        return keys
    


    #from gw2 fireworks
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
