#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Vehicles, Eagles

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
vehicle = Vehicles()
eagle = Eagles()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Disposables',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.Commando,
        back.Warp,
        support.ExpendableAntiTank,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        back.Supply,

        # 3rd row ----------
        orbital.Airburst,
        orbital.Barrage_120mm,
        eagle.Bomb_500kg,
        
        # 4th row ----------
        mission.Resupply,
        orbital.Walking,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}