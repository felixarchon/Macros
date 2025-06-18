from adafruit_hid.keycode import Keycode

# This file goes in the root directory (same as code.py)
class HD2_Base:
    #Timings
    @property
    def START_INPUT_DELAY(self): 
        return 0.5    
    @property
    def KEY_DELAY(self): 
        return 0.1

    #Stratagem Keys
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
    def Exo(self):
        return 0x000020
    @property
    def Sentry(self):
        return 0x002000
    @property
    def Orbital(self):
        return 0x200000
    @property
    def Eagle(self):
        return 0x200000
    @property
    def Mission(self):
        return 0x302000

    def stratagem(self, *argv):
        keys = [self.START_INPUT, self.START_INPUT_DELAY]

        for key in argv:
            keys += [key, self.KEY_DELAY, -key, self.KEY_DELAY]

        return keys
    
# COLOR     LABEL       KEY SEQUENCE

class SupportWeapons(HD2_Base):
    def __init__(self):
        super().__init__()
    
    @property
    def MachineGun(self): 
        return (self.Support, 'MG', self.stratagem(self.DOWN,self.LEFT,self.DOWN,self.UP,self.RIGHT))
    
    @property
    def HeavyMachineGun(self):
        return (self.Support, 'HMG', self.stratagem(self.DOWN, self.LEFT, self.UP, self.DOWN, self.DOWN))

    @property
    def AutoCannon(self):
        return (self.Support, 'AC', self.stratagem(self.DOWN,self.LEFT,self.DOWN,self.UP,self.UP,self.RIGHT))

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
    def Railgun(self):
        return (self.Support, 'Rail', self.stratagem(self.DOWN, self.RIGHT, self.DOWN, self.UP, self.LEFT, self.RIGHT))
    
    @property
    def Spear(self):
        return (self.Support, 'Spear', self.stratagem(self.DOWN, self.DOWN, self.UP, self.DOWN, self.DOWN))

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

    @property
    def AirburstRocketLauncher(self):
        return (self.Support, 'ARL', self.stratagem(self.DOWN, self.UP,self.UP,self.LEFT,self.RIGHT))

    @property
    def Commando(self):
        return (self.Support, 'Cmmdo', self.stratagem(self.DOWN,self.LEFT,self.UP,self.DOWN,self.RIGHT))


class GuardDogs(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def Rover(self):
        return (self.Guard, 'L-Grd', self.stratagem(self.DOWN,self.UP,self.LEFT,self.UP,self.RIGHT,self.RIGHT))

    @property
    def GuardDog(self):
        return (self.Guard, 'M-Grd', self.stratagem(self.DOWN, self.UP, self.LEFT, self.UP, self.RIGHT, self.DOWN))


class Backpacks(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def Supply(self):
        return (self.Backpack, 'Pack', self.stratagem(self.DOWN,self.LEFT,self.DOWN,self.UP,self.UP,self.DOWN))

    @property
    def Jump(self):
        return (self.Backpack, 'Jump', self.stratagem(self.DOWN, self.UP, self.UP, self.DOWN, self.UP))

    @property
    def BallisticShield(self):
        return (self.Backpack, 'B-Shld', self.stratagem(self.DOWN, self.LEFT, self.DOWN, self.DOWN, self.UP, self.LEFT))
    
    @property
    def ShieldGenerator(self):
        return (self.Backpack, 'B-Gen', self.stratagem(self.DOWN, self.UP, self.LEFT, self.RIGHT, self.LEFT, self.RIGHT))



class Vehicles(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def PatriotExosuit(self):
        return (self.Exo, 'Exo', self.stratagem(self.LEFT, self.DOWN, self.RIGHT, self.UP, self.LEFT, self.DOWN, self.DOWN))


class Sentries(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def MachineGun(self):
        return (self.Sentry, 'S-MG', self.stratagem(self.DOWN,self.UP,self.RIGHT,self.RIGHT,self.UP))

    @property
    def Gatling(self):
        return (self.Sentry, 'S-Gat', self.stratagem(self.DOWN,self.UP,self.RIGHT,self.LEFT))

    @property
    def AutoCannon(self):
        return (self.Sentry, 'S-AC', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.UP, self.LEFT, self.UP))

    @property
    def Rocket(self):
        return (self.Sentry, 'S-Roc', self.stratagem(self.DOWN,self.UP,self.RIGHT,self.RIGHT,self.LEFT))

    @property
    def HeavyMachineGunEmplacement(self):
        return (self.Sentry, 'E-HMG', self.stratagem(self.DOWN, self.UP, self.LEFT, self.RIGHT, self.RIGHT, self.LEFT))

    @property
    def Shield(self):
        return (self.Sentry, 'Shld', self.stratagem(self.DOWN, self.DOWN, self.LEFT, self.RIGHT, self.LEFT, self.RIGHT))

    @property
    def Tesla(self):
        return (self.Sentry, 'Tsla', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.UP, self.LEFT, self.RIGHT))

    @property
    def AnitPersonnelMinefield(self):
        return (self.Sentry, 'M-AP', self.stratagem(self.DOWN, self.LEFT, self.UP, self.RIGHT))

    @property
    def IncendiaryMines(self):
        return (self.Sentry, 'M-Inc', self.stratagem(self.DOWN, self.LEFT, self.LEFT, self.DOWN))

    @property
    def Mortar(self):
        return (self.Sentry, 'S-Mor', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.RIGHT, self.DOWN))

    @property
    def EMS(self):
        return (self.Sentry, 'S-EMS', self.stratagem(self.DOWN, self.UP, self.RIGHT, self.DOWN, self.RIGHT))


class Orbitals(HD2_Base):
    def __init__(self):
        super().__init__()

    @property
    def Barrage_120mm(self):
        return (self.Orbital , 'O-120', self.stratagem(self.RIGHT, self.RIGHT, self.DOWN, self.LEFT, self.RIGHT, self.DOWN))

    @property
    def Precision(self):
        return (self.Orbital, 'O-Prec', self.stratagem(self.RIGHT, self.RIGHT, self.UP))
    
    @property
    def Gatling(self):
        return (self.Orbital, 'O-Gat', self.stratagem(self.RIGHT, self.DOWN, self.LEFT, self.UP, self.UP))

    @property
    def Barrage_380mm(self):
        return (self.Orbital , 'O-380', self.stratagem(self.RIGHT, self.DOWN, self.UP, self.UP, self.LEFT, self.DOWN, self.DOWN))

    @property
    def Airburst(self):
        return (self.Orbital , 'O-Air', self.stratagem(self.RIGHT, self.RIGHT, self.RIGHT))

    @property
    def Walking(self):
        return (self.Orbital , 'O-Walk', self.stratagem(self.RIGHT, self.DOWN, self.RIGHT, self.DOWN, self.RIGHT, self.DOWN))

    @property
    def Laser(self):
        return (self.Orbital , 'O-Las', self.stratagem(self.RIGHT, self.DOWN, self.UP, self.RIGHT, self.DOWN))

    @property
    def RailCannon(self):
        return (self.Orbital , 'O-Rail', self.stratagem(self.RIGHT, self.UP, self.DOWN, self.DOWN, self.RIGHT))

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
        return (self.Mission, 'Strf', self.stratagem(self.UP, self.RIGHT, self.RIGHT))

    @property
    def Airstrike(self):
        return (self.Mission, 'Air', self.stratagem(self.UP, self.RIGHT, self.DOWN, self.RIGHT))

    @property
    def ClusterBomb(self):
        return (self.Mission, 'Clstr', self.stratagem(self.UP, self.RIGHT, self.DOWN, self.DOWN, self.RIGHT))

    @property
    def Napalm(self):
        return (self.Mission, 'Nap', self.stratagem(self.UP, self.RIGHT, self.DOWN, self.UP))

    @property
    def Smoke(self):
        return (self.Mission, 'Smk', self.stratagem(self.UP, self.RIGHT, self.UP, self.DOWN))

    @property
    def Rockets_110mm(self):
        return (self.Mission, 'R-110', self.stratagem(self.UP, self.RIGHT, self.UP, self.LEFT))

    @property
    def Bomb_500kg(self):
        return (self.Mission, 'B-500', self.stratagem(self.UP, self.RIGHT, self.DOWN, self.DOWN, self.DOWN))

















