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
    'name' : 'HD2 - Grp Bugs 6',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.AutoCannon,
        back.Warp,
        support.QuasarCannon,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        orbital.Laser,

        # 3rd row ----------
        orbital.Barrage_120mm,
        orbital.RailCannon,
        eagle.Bomb_500kg,
        
        # 4th row ----------
        mission.Resupply,
        support.RecoillessRifle,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}