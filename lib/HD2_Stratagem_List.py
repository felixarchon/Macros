from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# This file goes in the root directory (same as code.py)
class HD2_Base:
# Timings
    @property
    def START_INPUT_DELAY(self): 
        return 0.5    
    @property
    def KEY_DELAY(self): 
        return 0.1
    @property
    def LONG_DELAY(self): 
        return 0.5    
    @property
    def SHORT_DELAY(self): 
        return 0.1  

# Stratagem Keys
    @property
    def START_INPUT(self): 
        return Keycode.CONTROL
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

# Other Keys
    @property
    def FIVE(self):
        return Keycode.FIVE
    @property
    def X(self):
        return Keycode.X
    @property
    def F21(self):
        return Keycode.F21
    @property
    def F22(self):
        return Keycode.F22
    @property
    def F23(self):
        return Keycode.F23
    @property
    def F24(self):
        return Keycode.F24

# Mouse Clicks
    def M_L_CLICK(self):
        return {'buttons':Mouse.LEFT_BUTTON}
    def M_R_CLICK(self):
        return {'buttons':Mouse.RIGHT_BUTTON}

# Mouse Directions
    def DROP_WHEEL_UP(self):
        return {'y':-300}
    def DROP_WHEEL_DOWN(self):
        return {'y':300}
    def DROP_WHEEL_LEFT(self):
        return {'x':-300}
    def DROP_WHEEL_RIGHT(self):
        return {'x':300}
    def DROP_WHEEL_UP_LEFT(self):
        return {'y':-300,'x':-300}
    def DROP_WHEEL_UP_RIGHT(self):
        return {'y':-300,'x':300}
    def DROP_WHEEL_DOWN_RIGHT(self):
        return {'y':300,'x':300}
    def DROP_WHEEL_DOWN_LEFT(self):
        return {'y':300,'x':-300}


    def EMOTE_WHEEL_UP(self):
        return {'y':-300}
    def EMOTE_WHEEL_DOWN(self):
        return {'y':300}
    def EMOTE_WHEEL_LEFT(self):
        return {'x':-300}
    def EMOTE_WHEEL_RIGHT(self):
        return {'x':300}

    def COMM_WHEEL_TOP(self):
        return {'y':-300}
    def COMM_WHEEL_BOTTOM(self):
        return {'y':300}
    def COMM_WHEEL_RIGHT(self):
        return {'x':300}
    def COMM_WHEEL_LEFT(self):
        return {'x':-300}
    def COMM_WHEEL_TOP_RIGHT(self):
        return {'y':-300, 'x':300}
    def COMM_WHEEL_TOP_LEFT(self):
        return {'y':-300, 'x':-300}
    def COMM_WHEEL_BOTTOM_RIGHT(self):
        return {'y':300,'x':300}
    def COMM_WHEEL_BOTTOM_LEFT(self):
        return {'y':300,'x':-300}


    #Colors
    @property
    def Support(self): 
        return 0x000020
    @property
    def Backpack(self): 
        return 0x000020
    @property
    def Guard(self):
        return 0x000020
    @property
    def Vehicle(self):
        return 0x000020
    @property
    def Sentry(self):
        return 0x002000
    @property
    def Orbital(self):
        return 0x200000
    @property
    def Eagle(self):
        return 0xA8422D
    @property
    def Mission(self):
        return 0x302000
    @property
    def Function(self):
        return 0xFF4400

    def stratagem(self, *argv):
        keys = [self.START_INPUT, self.START_INPUT_DELAY]

        for key in argv:
            keys += [key, self.KEY_DELAY, -key, self.KEY_DELAY]

        return keys

    def drop_back(self):
        return [self.X, self.LONG_DELAY, self.DROP_WHEEL_UP_LEFT(), self.SHORT_DELAY ,self.M_L_CLICK()]

    def drop_stratagem(self):
        return [self.X, self.LONG_DELAY, self.DROP_WHEEL_UP_RIGHT(), self.SHORT_DELAY ,self.M_L_CLICK()]

    def drop_samples(self):
        return [self.X, self.LONG_DELAY, self.DROP_WHEEL_DOWN_RIGHT(), self.SHORT_DELAY ,self.M_L_CLICK()]

    def comm_yes(self):
        return [self.X, self.LONG_DELAY, self.COMM_WHEEL_RIGHT(), self.SHORT_DELAY ,self.M_L_CLICK()]


    
# COLOR     LABEL       KEY SEQUENCE
class SupportWeapons(HD2_Base):
    def __init__(self):
        super().__init__()
    
# Patriotic Administration Center
    @property
    def MachineGun(self): 
        return (self.Support, 'MG', self.stratagem(self.DOWN,self.LEFT,self.DOWN,self.UP,self.RIGHT))

    @property
    def AntiMaterial(self):
        return (self.Support, 'AMR', self.stratagem(self.DOWN, self.LEFT, self.RIGHT, self.UP, self.DOWN))

    @property
    def Stallwart(self):
        return (self.Support, 'Stal', self.stratagem(self.DOWN, self.LEFT, self.DOWN, self.UP, self.UP, self.LEFT))

    @property
    def ExpendableAntiTank(self):
        return (self.Support, 'EAT', self.stratagem(self.DOWN, self.DOWN, self.LEFT, self.UP, self.RIGHT))

    @property
    def RecoillessRifle(self):
        return (self.Support, 'R-Rfl', self.stratagem(self.DOWN, self.LEFT, self.RIGHT, self.RIGHT, self.LEFT))
 
    @property
    def Flamethrower(self):
        return (self.Support, 'Flm', self.stratagem(self.DOWN, self.LEFT, self.UP, self.DOWN, self.UP))

    @property
    def AutoCannon(self):
        return (self.Support, 'AC', self.stratagem(self.DOWN,self.LEFT,self.DOWN,self.UP,self.UP,self.RIGHT))

    @property
    def HeavyMachineGun(self):
        return (self.Support, 'HMG', self.stratagem(self.DOWN, self.LEFT, self.UP, self.DOWN, self.DOWN))

    @property
    def AirburstRocketLauncher(self):
        return (self.Support, 'ARL', self.stratagem(self.DOWN, self.UP,self.UP,self.LEFT,self.RIGHT))

    @property
    def Commando(self):
        return (self.Support, 'Cmmdo', self.stratagem(self.DOWN,self.LEFT,self.UP,self.DOWN,self.RIGHT))

    @property
    def Railgun(self):
        return (self.Support, 'Rail', self.stratagem(self.DOWN, self.RIGHT, self.DOWN, self.UP, self.LEFT, self.RIGHT))

    @property
    def Spear(self):
        return (self.Support, 'Spear', self.stratagem(self.DOWN, self.DOWN, self.UP, self.DOWN, self.DOWN))

    @property
    def WASP(self):
        return (self.Support, 'WASP', self.stratagem(self.DOWN,self.DOWN,self.UP,self.DOWN,self.RIGHT))

# Engineering Bay
    @property
    def GrenadeLauncher(self):
        return (self.Support, 'G-Lnch', self.stratagem(self.DOWN, self.LEFT, self.UP, self.LEFT, self.DOWN))

    @property
    def LaserCannon(self):
        return (self.Support, 'LAS-C', self.stratagem(self.DOWN, self.LEFT, self.DOWN, self.UP, self.LEFT))
    
    @property
    def ArcThrower(self):
        return (self.Support, 'Arc', self.stratagem(self.DOWN, self.RIGHT, self.DOWN, self.UP, self.LEFT, self.LEFT))

    @property
    def QuasarCannon(self):
        return (self.Support, 'Qsr-C', self.stratagem(self.DOWN, self.DOWN, self.UP, self.LEFT, self.RIGHT))

# Warbonds
    @property
    def Sterilizer(self):
        return (self.Support, 'Steri', self.stratagem(self.DOWN,self.LEFT,self.UP,self.DOWN,self.LEFT))

    @property
    def PortableHellbomb(self):
        return (self.Support, 'Hell', self.stratagem(self.DOWN, self.RIGHT, self.UP, self.UP, self.UP))

    @property
    def OneTrueFlag(self):
        return (self.Support, 'Flag', self.stratagem(self.DOWN,self.LEFT,self.RIGHT,self.RIGHT,self.UP))

    @property
    def DeEscalator(self):
        return (self.Support, 'DeEs', self.stratagem(self.DOWN, self.RIGHT, self.UP, self.LEFT, self.RIGHT))

    @property
    def Epoch(self):
        return (self.Support, 'Epoch', self.stratagem(self.DOWN,self.LEFT,self.UP,self.LEFT,self.RIGHT))

    @property
    def Speargun(self):
        return (self.Support, 'Sp-Gn',self.stratagem(self.DOWN, self.RIGHT, self.DOWN, self.LEFT, self.UP, self.RIGHT))

    @property
    def ExpendableNapalm(self):
        return (self.Support, 'ENap', self.stratagem(self.DOWN, self.DOWN, self.LEFT, self.UP, self.LEFT))

    @property
    def MissleSilo(self):
        return (self.Support, 'MSilo', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.DOWN, self.DOWN))

    @property
    def Maxigun(self):
        return (self.Support, 'Maxi', self.stratagem(self.DOWN, self.LEFT, self.RIGHT, self.DOWN, self.UP, self.UP))

    @property
    def Defoliation(self):
        return (self.Support, 'Chain', self.stratagem(self.DOWN, self.LEFT, self.RIGHT, self.RIGHT, self.DOWN))

    @property
    def C4(self):
        return (self.Support, 'C4', self.stratagem(self.DOWN, self.RIGHT, self.UP, self.UP, self.RIGHT, self.UP))


class GuardDogs(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def Rover(self):
        return (self.Guard, 'Grd-L', self.stratagem(self.DOWN,self.UP,self.LEFT,self.UP,self.RIGHT,self.RIGHT))

    @property
    def GuardDog(self):
        return (self.Guard, 'Grd-M', self.stratagem(self.DOWN, self.UP, self.LEFT, self.UP, self.RIGHT, self.DOWN))

    @property
    def DogBreath(self):
        return (self.Guard, 'Grd-G', self.stratagem(self.DOWN, self.UP, self.LEFT, self.UP, self.RIGHT, self.UP))

    @property
    def KNine(self):
        return (self.Guard, 'Grd-E', self.stratagem(self.DOWN, self.UP, self.LEFT, self.UP, self.RIGHT, self.LEFT))

    @property
    def HotDog(self):
        return (self.Guard, 'Grd-F', self.stratagem(self.DOWN, self.UP, self.LEFT, self.UP, self.RIGHT, self.RIGHT))

class Backpacks(HD2_Base):
    def __init__(self):
        super().__init__()
    
    # Hanger
    @property
    def Jump(self):
        return (self.Backpack, 'Jump', self.stratagem(self.DOWN, self.UP, self.UP, self.DOWN, self.UP))

    # Engineering Bay
    @property
    def Supply(self):
        return (self.Backpack, 'Pack', self.stratagem(self.DOWN,self.LEFT,self.DOWN,self.UP,self.UP,self.DOWN))

    @property
    def BallisticShield(self):
        return (self.Backpack, 'B-Shld', self.stratagem(self.DOWN, self.LEFT, self.DOWN, self.DOWN, self.UP, self.LEFT))
    
    @property
    def ShieldGenerator(self):
        return (self.Backpack, 'B-Gen', self.stratagem(self.DOWN, self.UP, self.LEFT, self.RIGHT, self.LEFT, self.RIGHT))

    # Warbonds
    @property
    def DirectionalShield(self):
        return (self.Backpack, 'D-Shld', self.stratagem(self.DOWN, self.UP, self.LEFT, self.RIGHT, self.LEFT, self.RIGHT))


    @property
    def Hover(self):
        return (self.Backpack, 'B-Hovr', self.stratagem(self.DOWN, self.LEFT, self.RIGHT, self.DOWN, self.LEFT, self.RIGHT))

    @property
    def Warp(self):
        return (self.Backpack, 'B-Wrp', self.stratagem(self.DOWN, self.LEFT, self.RIGHT, self.DOWN, self.LEFT, self.RIGHT))

class Vehicles(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def PatriotExosuit(self):
        return (self.Vehicle, 'P-Exo', self.stratagem(self.LEFT, self.DOWN, self.RIGHT, self.UP, self.LEFT, self.DOWN, self.DOWN))

    @property
    def FastReconVehicle(self):
        return (self.Vehicle, 'Recon', self.stratagem(self.RIGHT, self.DOWN, self.LEFT, self.DOWN, self.RIGHT, self.DOWN, self.UP))

    @property
    def EmancipatorExosuit(self):
        return (self.Vehicle, 'E-Exo', self.stratagem(self.LEFT, self.DOWN, self.RIGHT, self.UP, self.LEFT, self.DOWN, self.UP))

class Sentries(HD2_Base):
    def __init__(self):
        super().__init__()
    # Bridge
    @property
    def HeavyMachineGunEmplacement(self):
        return (self.Sentry, 'E-HMG', self.stratagem(self.DOWN, self.UP, self.LEFT, self.RIGHT, self.RIGHT, self.LEFT))

    @property
    def Shield(self):
        return (self.Sentry, 'E-Shld', self.stratagem(self.DOWN, self.DOWN, self.LEFT, self.RIGHT, self.LEFT, self.RIGHT))

    @property
    def Tesla(self):
        return (self.Sentry, 'Tsla', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.UP, self.LEFT, self.RIGHT))

    @property
    def Grenadier(self):
        return (self.Sentry, 'E-Gren', self.stratagem(self.DOWN, self.RIGHT, self.DOWN, self.LEFT, self.LEFT))

    #Engineering Bay
    @property
    def AnitPersonnelMinefield(self):
        return (self.Sentry, 'M-AP', self.stratagem(self.DOWN, self.LEFT, self.UP, self.RIGHT))

    @property
    def IncendiaryMines(self):
        return (self.Sentry, 'M-Inc', self.stratagem(self.DOWN, self.LEFT, self.LEFT, self.DOWN))

    @property
    def AntiTankMines(self):
        return (self.Sentry, 'M-AT', self.stratagem(self.DOWN, self.LEFT, self.UP, self.UP))

    @property
    def GasMines(self):
        return (self.Sentry, 'M-Gas', self.stratagem(self.DOWN, self.LEFT, self.LEFT, self.RIGHT))

    #Robotics Workshop
    @property
    def MachineGun(self):
        return (self.Sentry, 'S-MG', self.stratagem(self.DOWN,self.UP,self.RIGHT,self.RIGHT,self.UP))

    @property
    def Gatling(self):
        return (self.Sentry, 'S-Gat', self.stratagem(self.DOWN,self.UP,self.RIGHT,self.LEFT))

    @property
    def Mortar(self):
        return (self.Sentry, 'S-Mor', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.RIGHT, self.DOWN))

    @property
    def AutoCannon(self):
        return (self.Sentry, 'S-AC', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.UP, self.LEFT, self.UP))

    @property
    def Rocket(self):
        return (self.Sentry, 'S-Roc', self.stratagem(self.DOWN,self.UP,self.RIGHT,self.RIGHT,self.LEFT))

    @property
    def EMS(self):
        return (self.Sentry, 'S-EMS', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.DOWN, self.RIGHT))

    # Warbonds
    @property
    def AntiTankEmplacement(self):
        return (self.Sentry, 'E-AT', self.stratagem(self.DOWN, self.UP, self.LEFT, self.RIGHT, self.RIGHT, self.RIGHT))

    @property
    def Flame(self):
        return (self.Sentry, 'S-FLAM', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.DOWN, self.UP, self.UP))

    @property
    def Laser(self):
        return (self.Sentry, 'S-LAS', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.DOWN, self.UP, self.RIGHT))

class Orbitals(HD2_Base):
    def __init__(self):
        super().__init__()

    # Orbital Cannons
    @property
    def Gatling(self):
        return (self.Orbital, 'O-Gat', self.stratagem(self.RIGHT, self.DOWN, self.LEFT, self.UP, self.UP))

    @property
    def Airburst(self):
        return (self.Orbital , 'O-Air', self.stratagem(self.RIGHT, self.RIGHT, self.RIGHT))

    @property
    def Barrage_120mm(self):
        return (self.Orbital , 'O-120', self.stratagem(self.RIGHT, self.RIGHT, self.DOWN, self.LEFT, self.RIGHT, self.DOWN))

    @property
    def Barrage_380mm(self):
        return (self.Orbital , 'O-380', self.stratagem(self.RIGHT, self.DOWN, self.UP, self.UP, self.LEFT, self.DOWN, self.DOWN))

    @property
    def Walking(self):
        return (self.Orbital , 'O-Walk', self.stratagem(self.RIGHT, self.DOWN, self.RIGHT, self.DOWN, self.RIGHT, self.DOWN))

    @property
    def Laser(self):
        return (self.Orbital , 'O-Las', self.stratagem(self.RIGHT, self.DOWN, self.UP, self.RIGHT, self.DOWN))

    @property
    def Barrage_Napalm(self):
        return (self.Orbital , 'O-Nap', self.stratagem(self.RIGHT, self.RIGHT, self.DOWN, self.LEFT, self.RIGHT, self.UP))

    @property
    def RailCannon(self):
        return (self.Orbital , 'O-Rail', self.stratagem(self.RIGHT, self.UP, self.DOWN, self.DOWN, self.RIGHT))

    # Bridge
    @property
    def Precision(self):
        return (self.Orbital, 'O-Prec', self.stratagem(self.RIGHT, self.RIGHT, self.UP))

    @property
    def Gas(self):
        return (self.Orbital , 'O-Gas', self.stratagem(self.RIGHT, self.RIGHT, self.DOWN, self.RIGHT))

    @property
    def EMS(self):
        return (self.Orbital , 'O-EMS', self.stratagem(self.RIGHT, self.RIGHT, self.LEFT, self.DOWN))

    @property
    def Smoke(self):
        return (self.Orbital , 'O-Smk', self.stratagem(self.RIGHT, self.RIGHT, self.DOWN, self.UP))

class Missions(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def Resupply(self):
        return (self.Mission, 'Resup', self.stratagem(self.DOWN, self.DOWN, self.UP, self.RIGHT))

    @property
    def SOS(self):
        return (self.Mission, 'SOS', self.stratagem(self.UP, self.DOWN, self.RIGHT, self.UP))

    @property
    def Reinforce(self):
        return (self.Mission, 'Reinf', self.stratagem(self.UP, self.DOWN, self.RIGHT, self.LEFT, self.UP))

    @property
    def Hellbomb(self): 
        return (self.Mission, 'Hell', self.stratagem(self.DOWN, self.UP, self.LEFT, self.DOWN, self.UP, self.RIGHT, self.DOWN, self.UP))

    @property
    def SSSD(self):
        return (self.Mission, 'SSSD', self.stratagem(self.DOWN, self.DOWN, self.DOWN, self.UP, self.UP))

    @property
    def SeismicProbe(self):
        return (self.Mission, 'S-Prb', self.stratagem(self.UP, self.UP, self.LEFT, self.RIGHT, self.DOWN, self.DOWN))

    @property
    def UploadData(self):
        return (self.Mission, 'Up-D', self.stratagem(self.LEFT, self.RIGHT, self.UP, self.UP, self.UP))

    @property
    def EagleReArm(self):
        return (self.Mission, 'ERA', self.stratagem(self.UP, self.UP, self.LEFT, self.UP, self.RIGHT))

    @property
    def IlluminationFlare(self):
        return (self.Mission, 'I-Flr', self.stratagem(self.RIGHT, self.RIGHT, self.LEFT, self.LEFT))

    @property
    def SEAFArtillery(self):
        return (self.Mission, 'SEAF', self.stratagem(self.RIGHT, self.UP, self.UP, self.DOWN))

    @property
    def SuperEarthFlag(self):
        return (self.Mission, 'Flag', self.stratagem(self.DOWN, self.UP, self.DOWN, self.UP))

class Eagles(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def Strafing(self):
        return (self.Eagle, 'E-Strf', self.stratagem(self.UP, self.RIGHT, self.RIGHT))

    @property
    def Airstrike(self):
        return (self.Eagle, 'E-Air', self.stratagem(self.UP, self.RIGHT, self.DOWN, self.RIGHT))

    @property
    def ClusterBomb(self):
        return (self.Eagle, 'E-Cstr', self.stratagem(self.UP, self.RIGHT, self.DOWN, self.DOWN, self.RIGHT))

    @property
    def Napalm(self):
        return (self.Eagle, 'E-Nap', self.stratagem(self.UP, self.RIGHT, self.DOWN, self.UP))

    @property
    def Smoke(self):
        return (self.Eagle, 'E-Smk', self.stratagem(self.UP, self.RIGHT, self.UP, self.DOWN))

    @property
    def Rockets_110mm(self):
        return (self.Eagle, 'E-110', self.stratagem(self.UP, self.RIGHT, self.UP, self.LEFT))

    @property
    def Bomb_500kg(self):
        return (self.Eagle, 'E-500', self.stratagem(self.UP, self.RIGHT, self.DOWN, self.DOWN, self.DOWN))

class Functions(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def ArmDropHellbomb(self):
        return(self.Function, 'D-Hell', [self.FIVE, self.SHORT_DELAY, -self.FIVE, self.SHORT_DELAY] + self.drop_back())

    @property
    def DropStratagem(self):
        return (self.Function, 'D_Strat', self.drop_stratagem())

    @property
    def DropBackpack(self):
        return (self.Function, 'D_Back', self.drop_back())

    @property
    def DropSamples(self):
        return (self.Function, 'D_Back', self.drop_samples())

    @property
    def F21(self):
        return (self.Function, 'F21', self.stratagem(self.F21))

    @property
    def F22(self):
        return (self.Function, 'F22', self.stratagem(self.F22))

    @property
    def F23(self):
        return (self.Function, 'F23', self.stratagem(self.F23))

    @property
    def F24(self):
        return (self.Function, 'F24', self.stratagem(self.F24))