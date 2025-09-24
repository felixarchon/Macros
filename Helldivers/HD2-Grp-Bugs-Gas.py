#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Vehicles, Eagles

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
vehicle = Vehicles()
eagle = Eagles()
guard = GuardDogs()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Bugs Gas',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.ExpendableAntiTank,
        back.Warp,
        support.QuasarCannon,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        orbital.Laser,

        # 3rd row ----------
        orbital.RailCannon,
        orbital.Barrage_120mm,        
        eagle.Bomb_500kg,
        
        # 4th row ----------
        mission.Resupply,
        guard.DogBreath,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}