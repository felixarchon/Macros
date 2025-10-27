#Macropad, Hotkeys - Helldivers 2 - Early Bug Solo Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, Backpacks, Functions
from adafruit_hid.mouse import Mouse
from adafruit_hid.keycode import Keycode

M_UP = {'y':-300}
M_DOWN = {'y':300}
M_LEFT = {'x':-300}
M_RIGHT = {'x':300}
M_CLICK = {'buttons':Mouse.LEFT_BUTTON}

support = SupportWeapons()
back = Backpacks()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
function = Functions()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Hellbomb',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.ExpendableAntiTank,
        support.Commando,
        support.PortableHellbomb,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        function.ArmDropHellbomb,

        # 3rd row ----------
        support.ExpendableNapalm,
        support.Railgun,
        eagle.Strafing,

        # 4th row ----------
        mission.Resupply,
        orbital.Walking,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}