from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# This file goes in the root directory (same as code.py)

#For the yield-based methods add the following code to your base code.py file 
# inside the main while statement
# add the below code after:   sequence = apps[app_index].macros[key_number][2]
#
#    # --- ADDED: Execute callable/lambda to instantiate fresh generator ---
#    if callable(sequence):
#        sequence = sequence()
#
# and before the code:    if pressed:
# If you don't want to change your code.py, remove the yield-based methods and uncomment the others
# Then remove the lambda from each stratagem
# lambda is supposed to allow more macros  (more memory efficient?)

class HD2:
    # Timings
    START_INPUT_DELAY = 0.5
    KEY_DELAY = 0.1 
    LONG_DELAY = 0.5    
    SHORT_DELAY = 0.1  

    # Stratagem Keys
    START_INPUT = Keycode.CONTROL
    UP = Keycode.UP_ARROW
    DOWN = Keycode.DOWN_ARROW
    LEFT = Keycode.LEFT_ARROW
    RIGHT = Keycode.RIGHT_ARROW

    # Other Keys
    FIVE = Keycode.FIVE
    X = Keycode.X
    Q = Keycode.Q
    B = Keycode.B
    G = Keycode.G
    F12 = Keycode.F12
    WW_UP = Keycode.F21
    WW_DOWN = Keycode.F22
    WW_LEFT = Keycode.F23
    WW_RIGHT = Keycode.F24

    # Mouse Clicks
    M_L_CLICK = {'buttons':Mouse.LEFT_BUTTON}
    M_R_CLICK = {'buttons':Mouse.RIGHT_BUTTON}

    # Mouse Directions
    DROP_WHEEL_UP = {'y':-300}
    DROP_WHEEL_DOWN = {'y':300}
    DROP_WHEEL_LEFT = {'x':-300}
    DROP_WHEEL_RIGHT = {'x':300}
    DROP_WHEEL_UP_LEFT = {'y':-300,'x':-300}
    DROP_WHEEL_UP_RIGHT = {'y':-300,'x':300}
    DROP_WHEEL_DOWN_RIGHT = {'y':300,'x':300}
    DROP_WHEEL_DOWN_LEFT = {'y':300,'x':-300}

    EMOTE_WHEEL_UP = {'y':-300}
    EMOTE_WHEEL_DOWN = {'y':300}
    EMOTE_WHEEL_LEFT = {'x':-300}
    EMOTE_WHEEL_RIGHT = {'x':300}

    COMM_WHEEL_TOP = {'y':-300}
    COMM_WHEEL_BOTTOM = {'y':300}
    COMM_WHEEL_RIGHT = {'x':300}
    COMM_WHEEL_LEFT = {'x':-300}
    COMM_WHEEL_TOP_RIGHT = {'y':-300, 'x':300}
    COMM_WHEEL_TOP_LEFT = {'y':-300, 'x':-300}
    COMM_WHEEL_BOTTOM_RIGHT = {'y':300,'x':300}
    COMM_WHEEL_BOTTOM_LEFT = {'y':300,'x':-300}

    #Colors
    Support = 0x000020
    Backpack = 0x000020
    Guard = 0x000020
    Vehicle = 0x000020
    Sentry = 0x002000
    Orbital = 0x200000
    Eagle = 0xA8422D
    Mission = 0x302000
    Function = 0xFF4400

    inv_back = [X, LONG_DELAY, DROP_WHEEL_UP_LEFT, SHORT_DELAY ,M_L_CLICK]
    inv_stratagem = [X, LONG_DELAY, DROP_WHEEL_UP_RIGHT, SHORT_DELAY ,M_L_CLICK]
    inv_samples = [X, LONG_DELAY, DROP_WHEEL_DOWN_RIGHT, SHORT_DELAY ,M_L_CLICK]
    inv_carry = [X, LONG_DELAY, DROP_WHEEL_DOWN_LEFT, SHORT_DELAY ,M_L_CLICK]

    comm_yes = [Q, LONG_DELAY, COMM_WHEEL_RIGHT, SHORT_DELAY ,M_L_CLICK]

    @staticmethod
    def stratagem(*argv):
        yield HD2.START_INPUT
        yield HD2.START_INPUT_DELAY

        for key in argv:
            yield key
            yield HD2.KEY_DELAY
            yield -key
            yield HD2.KEY_DELAY

#    @staticmethod
#    def stratagem(*argv):
#        keys = [HD2.START_INPUT, HD2.START_INPUT_DELAY]
#
#        for key in argv:
#            keys += [key, HD2.KEY_DELAY, -key, HD2.KEY_DELAY]
#
#        return keys

    @staticmethod
    def keypress(*argv):    

        for key in argv:
            yield key
            yield HD2.KEY_DELAY
            yield -key
            yield HD2.KEY_DELAY

#    @staticmethod
#    def keypress(*argv):    
#        keylist = []
#
#        for key in argv:
#            keylist += [key, HD2.KEY_DELAY, -key, HD2.KEY_DELAY]
#
#        return keylist

    
# COLOR     LABEL       KEY SEQUENCE
class SupportWeapons(HD2):    
    # Patriotic Administration Center
    MachineGun = (HD2.Support, 'MG', lambda: HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.DOWN,HD2.UP,HD2.RIGHT))
    AntiMaterial = (HD2.Support, 'AMR', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.UP, HD2.DOWN))
    Stallwart = (HD2.Support, 'Stal', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.DOWN, HD2.UP, HD2.UP, HD2.LEFT))
    ExpendableAntiTank = (HD2.Support, 'E-AT', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.LEFT, HD2.UP, HD2.RIGHT))
    RecoillessRifle = (HD2.Support, 'R-Rfl', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.RIGHT, HD2.LEFT)) 
    Flamethrower = (HD2.Support, 'Flm', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.UP, HD2.DOWN, HD2.UP))
    AutoCannon = (HD2.Support, 'AC', lambda: HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.DOWN,HD2.UP,HD2.UP,HD2.RIGHT))
    HeavyMachineGun = (HD2.Support, 'HMG', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.UP, HD2.DOWN, HD2.DOWN))
    AirburstRocketLauncher = (HD2.Support, 'ARL', lambda: HD2.stratagem(HD2.DOWN, HD2.UP,HD2.UP,HD2.LEFT,HD2.RIGHT))
    Commando = (HD2.Support, 'Cmmdo', lambda: HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.UP,HD2.DOWN,HD2.RIGHT))
    Railgun = (HD2.Support, 'Rail', lambda: HD2.stratagem(HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.LEFT, HD2.RIGHT))
    Spear = (HD2.Support, 'Spear', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.UP, HD2.DOWN, HD2.DOWN))
    WASP = (HD2.Support, 'WASP', lambda: HD2.stratagem(HD2.DOWN,HD2.DOWN,HD2.UP,HD2.DOWN,HD2.RIGHT))

    # Engineering Bay
    GrenadeLauncher = (HD2.Support, 'G-Lnch', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.UP, HD2.LEFT, HD2.DOWN))
    LaserCannon = (HD2.Support, 'LAS-C', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.DOWN, HD2.UP, HD2.LEFT))    
    ArcThrower = (HD2.Support, 'Arc', lambda: HD2.stratagem(HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.LEFT, HD2.LEFT))
    QuasarCannon = (HD2.Support, 'Qsr-C', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.UP, HD2.LEFT, HD2.RIGHT))

    # Warbonds
    Sterilizer = (HD2.Support, 'Steri', lambda: HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.UP,HD2.DOWN,HD2.LEFT))
    PortableHellbomb = (HD2.Support, 'Hell', lambda: HD2.stratagem(HD2.DOWN, HD2.RIGHT, HD2.UP, HD2.UP, HD2.UP))
    OneTrueFlag = (HD2.Support, 'Flag', lambda: HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.RIGHT,HD2.RIGHT,HD2.UP))
    DeEscalator = (HD2.Support, 'DeEs', lambda: HD2.stratagem(HD2.DOWN, HD2.RIGHT, HD2.UP, HD2.LEFT, HD2.RIGHT))
    Epoch = (HD2.Support, 'Epoch', lambda: HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.UP,HD2.LEFT,HD2.RIGHT))
    Speargun = (HD2.Support, 'Sp-Gn',lambda: HD2.stratagem(HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.UP, HD2.RIGHT))
    ExpendableNapalm = (HD2.Support, 'E-Nap', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.LEFT, HD2.UP, HD2.LEFT))
    MissleSilo = (HD2.Support, 'E-MS', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.DOWN))
    Maxigun = (HD2.Support, 'Maxi', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.UP))
    Defoliation = (HD2.Support, 'Chain', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.RIGHT, HD2.DOWN))
    C4 = (HD2.Support, 'C4', lambda: HD2.stratagem(HD2.DOWN, HD2.RIGHT, HD2.UP, HD2.UP, HD2.RIGHT, HD2.UP))
    Hammer = (HD2.Support, 'Hamm', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.LEFT, HD2.UP))
    Leveller = (HD2.Support, 'E-Lev', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.LEFT, HD2.UP, HD2.DOWN))
    BFGrenade = (HD2.Support, 'G-BFL', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.UP, HD2.LEFT, HD2.UP, HD2.UP))
    Cremator = (HD2.Support, 'Fm-BF', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.UP))
    BulletStorm = (HD2.Support, 'E-BS', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.DOWN, HD2.RIGHT, HD2.UP, HD2.LEFT))
    Meltagun = (HD2.Support, 'Melta', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.UP, HD2.LEFT, HD2.LEFT, HD2.DOWN))

class GuardDogs(HD2):
    Rover = (HD2.Guard, 'Grd-L', lambda: HD2.stratagem(HD2.DOWN,HD2.UP,HD2.LEFT,HD2.UP,HD2.RIGHT,HD2.RIGHT))
    GuardDog = (HD2.Guard, 'Grd-M', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.UP, HD2.RIGHT, HD2.DOWN))
    DogBreath = (HD2.Guard, 'Grd-G', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.UP, HD2.RIGHT, HD2.UP))
    KNine = (HD2.Guard, 'Grd-E', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.UP, HD2.RIGHT, HD2.LEFT))
    HotDog = (HD2.Guard, 'Grd-F', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.UP, HD2.LEFT, HD2.LEFT))

class Backpacks(HD2):
    # Hanger
    Jump = (HD2.Backpack, 'Jump', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.UP, HD2.DOWN, HD2.UP))

    # Engineering Bay
    Supply = (HD2.Backpack, 'Pack', lambda: HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.DOWN,HD2.UP,HD2.UP,HD2.DOWN))
    BallisticShield = (HD2.Backpack, 'B-Shld', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.DOWN, HD2.DOWN, HD2.UP, HD2.LEFT))    
    ShieldGenerator = (HD2.Backpack, 'B-Gen', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.RIGHT, HD2.LEFT, HD2.RIGHT))

    # Warbonds
    DirectionalShield = (HD2.Backpack, 'D-Shld', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.RIGHT, HD2.LEFT, HD2.RIGHT))
    Hover = (HD2.Backpack, 'B-Hovr', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.RIGHT))
    Warp = (HD2.Backpack, 'B-Wrp', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.RIGHT))

    # Experimental
    DarkFluidVessel = (HD2.Backpack, "Fluid", lambda: HD2.stratagem(HD2.UP, HD2.LEFT, HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.UP))

class Vehicles(HD2):
    PatriotExosuit = (HD2.Vehicle, 'P-Exo', lambda: HD2.stratagem(HD2.LEFT, HD2.DOWN, HD2.RIGHT, HD2.UP, HD2.LEFT, HD2.DOWN, HD2.DOWN))
    FastReconVehicle = (HD2.Vehicle, 'Recon', lambda: HD2.stratagem(HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.UP))
    EmancipatorExosuit = (HD2.Vehicle, 'E-Exo', lambda: HD2.stratagem(HD2.LEFT, HD2.DOWN, HD2.RIGHT, HD2.UP, HD2.LEFT, HD2.DOWN, HD2.UP))
    Bastion = (HD2.Vehicle, 'B-Tank', lambda: HD2.stratagem(HD2.LEFT, HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.DOWN, HD2.UP, HD2.DOWN, HD2.UP))
    LumbererExosuit = (HD2.Vehicle, 'L-Exo', lambda: HD2.stratagem(HD2.LEFT, HD2.DOWN, HD2.RIGHT, HD2.UP, HD2.RIGHT, HD2.LEFT, HD2.UP))
    BreakthroughExosuit = (HD2.Vehicle, 'B-Exo', lambda: HD2.stratagem(HD2.LEFT, HD2.DOWN, HD2.RIGHT, HD2.LEFT, HD2.RIGHT, HD2.DOWN, HD2.UP))
    Maelstrom = (HD2.Vehicle, 'M-Tank', lambda: HD2.stratagem(HD2.LEFT, HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.DOWN, HD2.UP, HD2.LEFT, HD2.RIGHT))

class Sentries(HD2):
    # Bridge
    HeavyMachineGunEmplacement = (HD2.Sentry, 'E-HMG', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.RIGHT, HD2.RIGHT, HD2.LEFT))
    Shield = (HD2.Sentry, 'E-Shld', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.LEFT, HD2.RIGHT))
    Tesla = (HD2.Sentry, 'Tsla', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.UP, HD2.LEFT, HD2.RIGHT))
    Grenadier = (HD2.Sentry, 'E-Gren', lambda: HD2.stratagem(HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.LEFT))

    #Engineering Bay
    AnitPersonnelMinefield = (HD2.Sentry, 'M-AP', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.UP, HD2.RIGHT))
    IncendiaryMines = (HD2.Sentry, 'M-Inc', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.LEFT, HD2.DOWN))
    AntiTankMines = (HD2.Sentry, 'M-AT', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.UP, HD2.UP))
    GasMines = (HD2.Sentry, 'M-Gas', lambda: HD2.stratagem(HD2.DOWN, HD2.LEFT, HD2.LEFT, HD2.RIGHT))

    #Robotics Workshop
    MachineGun = (HD2.Sentry, 'S-MG', lambda: HD2.stratagem(HD2.DOWN,HD2.UP,HD2.RIGHT,HD2.RIGHT,HD2.UP))
    Gatling = (HD2.Sentry, 'S-Gat', lambda: HD2.stratagem(HD2.DOWN,HD2.UP,HD2.RIGHT,HD2.LEFT))
    Mortar = (HD2.Sentry, 'MS-Mor', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.RIGHT, HD2.DOWN))
    AutoCannon = (HD2.Sentry, 'S-AC', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.UP, HD2.LEFT, HD2.UP))
    Rocket = (HD2.Sentry, 'S-Roc', lambda: HD2.stratagem(HD2.DOWN,HD2.UP,HD2.RIGHT,HD2.RIGHT,HD2.LEFT))
    MortarEMS = (HD2.Sentry, 'MS-EMS', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.RIGHT))

    # Warbonds
    AntiTankEmplacement = (HD2.Sentry, 'E-AT', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.RIGHT, HD2.RIGHT, HD2.RIGHT))
    Flame = (HD2.Sentry, 'S-FLAM', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.UP))
    Laser = (HD2.Sentry, 'S-LAS', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.RIGHT))
    MortarGas = (HD2.Sentry, 'MS-Gas', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.LEFT))

class Orbitals(HD2):
    # Orbital Cannons
    Gatling = (HD2.Orbital, 'O-Gat', lambda: HD2.stratagem(HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.UP, HD2.UP))
    Airburst = (HD2.Orbital , 'O-Air', lambda: HD2.stratagem(HD2.RIGHT, HD2.RIGHT, HD2.RIGHT))
    Barrage_120mm = (HD2.Orbital , 'O-120', lambda: HD2.stratagem(HD2.RIGHT, HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.DOWN))
    Barrage_380mm = (HD2.Orbital , 'O-380', lambda: HD2.stratagem(HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.UP, HD2.LEFT, HD2.DOWN, HD2.DOWN))
    Walking = (HD2.Orbital , 'O-Walk', lambda: HD2.stratagem(HD2.RIGHT, HD2.DOWN, HD2.RIGHT, HD2.DOWN, HD2.RIGHT, HD2.DOWN))
    Laser = (HD2.Orbital , 'O-Las', lambda: HD2.stratagem(HD2.RIGHT, HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.DOWN))
    Barrage_Napalm = (HD2.Orbital , 'O-Nap', lambda: HD2.stratagem(HD2.RIGHT, HD2.RIGHT, HD2.DOWN, HD2.LEFT, HD2.RIGHT, HD2.UP))
    RailCannon = (HD2.Orbital , 'O-Rail', lambda: HD2.stratagem(HD2.RIGHT, HD2.UP, HD2.DOWN, HD2.DOWN, HD2.RIGHT))
 
    # Bridge
    Precision = (HD2.Orbital, 'O-Prec', lambda: HD2.stratagem(HD2.RIGHT, HD2.RIGHT, HD2.UP))
    Gas = (HD2.Orbital , 'O-Gas', lambda: HD2.stratagem(HD2.RIGHT, HD2.RIGHT, HD2.DOWN, HD2.RIGHT))
    EMS = (HD2.Orbital , 'O-EMS', lambda: HD2.stratagem(HD2.RIGHT, HD2.RIGHT, HD2.LEFT, HD2.DOWN))
    Smoke = (HD2.Orbital , 'O-Smk', lambda: HD2.stratagem(HD2.RIGHT, HD2.RIGHT, HD2.DOWN, HD2.UP))

class Missions(HD2):
    Resupply = (HD2.Mission, 'Resup', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.UP, HD2.RIGHT))
    SOS = (HD2.Mission, 'SOS', lambda: HD2.stratagem(HD2.UP, HD2.DOWN, HD2.RIGHT, HD2.UP))
    Reinforce = (HD2.Mission, 'Reinf', lambda: HD2.stratagem(HD2.UP, HD2.DOWN, HD2.RIGHT, HD2.LEFT, HD2.UP))
    Hellbomb = (HD2.Mission, 'Hell', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.LEFT, HD2.DOWN, HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.UP))
    SSSD = (HD2.Mission, 'SSSD', lambda: HD2.stratagem(HD2.DOWN, HD2.DOWN, HD2.DOWN, HD2.UP, HD2.UP))
    SeismicProbe = (HD2.Mission, 'S-Prb', lambda: HD2.stratagem(HD2.UP, HD2.UP, HD2.LEFT, HD2.RIGHT, HD2.DOWN, HD2.DOWN))
    UploadData = (HD2.Mission, 'Up-D', lambda: HD2.stratagem(HD2.LEFT, HD2.RIGHT, HD2.UP, HD2.UP, HD2.UP))
    EagleReArm = (HD2.Mission, 'ERA', lambda: HD2.stratagem(HD2.UP, HD2.UP, HD2.LEFT, HD2.UP, HD2.RIGHT))
    IlluminationFlare = (HD2.Mission, 'I-Flr', lambda: HD2.stratagem(HD2.RIGHT, HD2.RIGHT, HD2.LEFT, HD2.LEFT))
    SEAFArtillery = (HD2.Mission, 'SEAF', lambda: HD2.stratagem(HD2.RIGHT, HD2.UP, HD2.UP, HD2.DOWN))
    SuperEarthFlag = (HD2.Mission, 'Flag', lambda: HD2.stratagem(HD2.DOWN, HD2.UP, HD2.DOWN, HD2.UP))

class Eagles(HD2):
    Strafing = (HD2.Eagle, 'E-Strf', lambda: HD2.stratagem(HD2.UP, HD2.RIGHT, HD2.RIGHT))
    Airstrike = (HD2.Eagle, 'E-Air', lambda: HD2.stratagem(HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.RIGHT))
    ClusterBomb = (HD2.Eagle, 'E-Cstr', lambda: HD2.stratagem(HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.DOWN, HD2.RIGHT))
    Napalm = (HD2.Eagle, 'E-Nap', lambda: HD2.stratagem(HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.UP))
    Smoke = (HD2.Eagle, 'E-Smk', lambda: HD2.stratagem(HD2.UP, HD2.RIGHT, HD2.UP, HD2.DOWN))
    Rockets_110mm = (HD2.Eagle, 'E-110', lambda: HD2.stratagem(HD2.UP, HD2.RIGHT, HD2.UP, HD2.LEFT))
    Bomb_500kg = (HD2.Eagle, 'E-500', lambda: HD2.stratagem(HD2.UP, HD2.RIGHT, HD2.DOWN, HD2.DOWN, HD2.DOWN))

class Functions(HD2):
    ArmDropHellbomb = (HD2.Function, 'D-Hell', lambda: [HD2.FIVE, HD2.SHORT_DELAY, -HD2.FIVE, HD2.SHORT_DELAY] + HD2.inv_back)
    DropStratagem = (HD2.Function, 'D_Strat', lambda: HD2.inv_stratagem)
    DropBackpack = (HD2.Function, 'D_Back', lambda: HD2.inv_back)
    DropSamples = (HD2.Function, 'D_Samp', lambda: HD2.inv_samples)

    C4_Swap_Fire = (HD2.Function, 'C4-F', lambda: HD2.keypress(HD2.WW_LEFT))
    OneTwo_Swap_Fire = (HD2.Function, '1-2-F', lambda: HD2.keypress(HD2.WW_LEFT))
    Var_Swap_Fire = (HD2.Function, 'Var-F', lambda: HD2.keypress(HD2.WW_LEFT))
    Stoker_Swap_Fire = (HD2.Function, 'Stok-F', lambda: HD2.keypress(HD2.WW_LEFT))
    Left_Swap = (HD2.Function, 'Lft-S', lambda: HD2.keypress(HD2.WW_LEFT))

    WW_UP = (HD2.Function, 'WW-U', lambda: HD2.keypress(HD2.WW_UP))
    WW_DOWN = (HD2.Function, 'WW-D', lambda: HD2.keypress(HD2.WW_DOWN))
    WW_LEFT = (HD2.Function, 'WW-L', lambda: HD2.keypress(HD2.WW_LEFT))
    WW_RIGHT = (HD2.Function, 'WW-R', lambda: HD2.keypress(HD2.WW_RIGHT))