# This file goes in the root directory (same as code.py)
from adafruit_hid.keycode import Keycode

START_INPUT_DELAY = 0.5
KEY_DELAY = 0.1

START_INPUT = Keycode.CONTROL

UP = Keycode.UP_ARROW
DOWN = Keycode.DOWN_ARROW
LEFT = Keycode.LEFT_ARROW
RIGHT = Keycode.RIGHT_ARROW

def stratagem(*argv):
    keys = [START_INPUT, START_INPUT_DELAY]

    for key in argv:
        keys += [key, KEY_DELAY, -key, KEY_DELAY]

    return keys

#Colors
Support = 0x000020
Backpack = 0x000020
Guard = 0x000020
Exo = 0x000020
Sentry = 0x002000
Orbital = 0x200000
Eagle = 0x200000
Mission = 0x302000

# Strategem Support Template
# (0x000020, '',      stratagem()),
# Support ----------
def MachineGun(): 
    return (Support, 'MG', stratagem(DOWN,LEFT,DOWN,UP,RIGHT))

def HeavyMachineGun():
    return (Support, 'HMG', stratagem(DOWN, LEFT, UP, DOWN, DOWN))

def AutoCannon():
    return (Support, 'AC', stratagem(DOWN,LEFT,DOWN,UP,UP,RIGHT))

def AntiMaterial():
    return (Support, 'AMR', stratagem(DOWN, LEFT, RIGHT, UP, DOWN))

def Stallwart():
    return (Support, 'Stal', stratagem(DOWN, LEFT, DOWN, UP, UP, LEFT))

def ExpendableAntiTank():
    return (Support, 'EAT', stratagem(DOWN, DOWN, LEFT, UP, RIGHT))

def RecoillessRifle():
    return (Support, 'R-Rfl', stratagem(DOWN, LEFT, RIGHT, RIGHT, LEFT))

def Flamethrower():
    return (Support, 'Flm', stratagem(DOWN, LEFT, UP, DOWN, UP))

def Railgun():
    return (Support, 'Rail', stratagem(DOWN, RIGHT, LEFT, DOWN, UP, LEFT, RIGHT))

def Spear():
    return (Support, 'Spear', stratagem(DOWN, DOWN, UP, DOWN, DOWN))

def GrenadeLauncher():
    return (Support, 'G-Lnch', stratagem(DOWN, LEFT, UP, LEFT, DOWN))

def LaserCannon():
    return (Support, 'LAS-C', stratagem(DOWN, LEFT, DOWN, UP, LEFT))

def ArcThrower():
    return (Support, 'Arc', stratagem(DOWN, RIGHT, DOWN, UP, LEFT, LEFT))

def QuasarCannon():
    return (Support, 'Qsr-C', stratagem(DOWN, DOWN, UP, LEFT, RIGHT))

def AirburstRocketLauncher():
    return (Support, 'ARL', stratagem(DOWN, UP,UP,LEFT,RIGHT))

def Commando():
    return (Support, 'Cmmdo', stratagem(DOWN,LEFT,UP,DOWN,RIGHT))



def GuardDog_Rover():
    return (Guard, 'L-Grd', stratagem(DOWN,UP,LEFT,UP,RIGHT,RIGHT))

def GuardDog():
    return (Guard, 'M-Grd', stratagem(DOWN, UP, LEFT, UP, RIGHT, DOWN))




def SupplyPack():
    return (Backpack, 'Pack', stratagem(DOWN,LEFT,DOWN,UP,UP,DOWN))

def JumpPack():
    return (Backpack, 'Jump', stratagem(DOWN, UP, UP, DOWN, UP))

def BallisticShieldBackpack():
    return (Backpack, 'B-Shld', stratagem(DOWN, LEFT, DOWN, DOWN, UP, LEFT))



def PatriotExosuit():
    return (Exo, 'Exo', stratagem(LEFT, DOWN, RIGHT, UP, LEFT, DOWN, DOWN))


# Sentries ----------
def MachineSentry():
    return (Sentry, 'S-MG', stratagem(DOWN,UP,RIGHT,RIGHT,UP))

def GatlingSentry():
    return (Sentry, 'S-Gat', stratagem(DOWN,UP,RIGHT,LEFT))      

def RocketSentry():
    return (Sentry, 'S-Roc', stratagem(DOWN,UP,RIGHT,RIGHT,LEFT))
