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
    def PRESS_DELAY(self):
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


    
    #Letter Keys
    @property
    def A(self):
        return Keycode.A
    @property
    def B(self):
        return Keycode.B
    @property
    def C(self):
        return Keycode.C
    @property
    def D(self):
        return Keycode.D
    @property
    def E(self):
        return Keycode.E
    @property
    def F(self):
        return Keycode.F
    @property
    def G(self):
        return Keycode.G
    @property
    def H(self):
        return Keycode.H
    @property
    def I(self):
        return Keycode.I
    @property
    def J(self):
        return Keycode.J
    @property
    def K(self):
        return Keycode.K
    @property
    def L(self):
        return Keycode.L
    @property
    def M(self):
        return Keycode.M
    @property
    def N(self):
        return Keycode.N
    @property
    def O(self):
        return Keycode.O
    @property
    def P(self):
        return Keycode.P
    @property
    def Q(self):
        return Keycode.Q
    @property
    def R(self):
        return Keycode.R
    @property
    def S(self):
        return Keycode.S
    @property
    def T(self):
        return Keycode.T
    @property
    def U(self):
        return Keycode.U
    @property
    def V(self):
        return Keycode.V
    @property
    def W(self):
        return Keycode.W
    @property
    def X(self):
        return Keycode.X
    @property
    def Y(self):
        return Keycode.Y
    @property
    def Z(self):
        return Keycode.Z

    #Numbers
    @property
    def ONE(self):
        return Keycode.ONE
    @property
    def TWO(self):
        return Keycode.TWO
    @property
    def THREE(self):
        return Keycode.THREE
    @property
    def FOUR(self):
        return Keycode.FOUR
    @property
    def FIVE(self):
        return Keycode.FIVE
    @property
    def SIX(self):
        return Keycode.SIX
    @property
    def SEVEN(self):
        return Keycode.SEVEN
    @property
    def EIGHT(self):
        return Keycode.EIGHT
    @property
    def NINE(self):
        return Keycode.NINE
    @property
    def ZERO(self):
        return Keycode.ZERO

    @property
    def CTRL(self):
        return Keycode.CONTROL
    @property
    def ALT(self):
        return Keycode.ALT
    @property
    def SHFT(self):
        return Keycode.SHIFT
    @property
    def DEL(self):
        return Keycode.DEL
    @property
    def SPACE(self):
        return Keycode.SPACE
    @property
    def ENTER(self):
        return Keycode.ENTER

    #Function Keys
    @property
    def F1(self):
        return Keycode.F1


    #Colors
    @property
    def Support(self): 
        return 0x000020



    #Methods
    def jiggler(self, repeats, keys=[]):    
        keylist = []
        repeat = int(repeats)

        for i in range(repeat):
            for key in keys:
                keylist += [self.JIGGLER_DELAY, key]

        return keylist

    #from hd2
    def stratagem(self, *argv):
        keys = [self.START_STRATAGEM, self.START_STRATAGEM_INPUT_DELAY]

        for key in argv:
            keys += [key, self.STRATAGEM_KEY_DELAY, -key, self.STRATAGEM_KEY_DELAY]

        return keys
    


    #from gw2 fireworks
    def combos(self, delay, keys=[]):    
        keylist = []

        for key in keys:
            keylist += [key, self.PRESS_DELAY, -key, delay]

        return keylist

    def keytimes(self, keytimes=[]):
        keylist=[]

        for key, delay in keytimes:
            keylist += [key, self.PRESS_DELAY, -key, delay]

        return keylist
    



    

    def shortcuts(self, keys=[]):    
        keylist = []

        for key in keys:
            keylist += [key]

        return keylist
