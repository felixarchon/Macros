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
    'name' : 'HD2 - Grp Illum Gas',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.LaserCannon,        
        guard.DogBreath,
        support.QuasarCannon,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        orbital.Precision,

        # 3rd row ----------
        orbital.RailCannon,
        orbital.Gatling,        
        eagle.Bomb_500kg,
        
        # 4th row ----------
        mission.Resupply,
        guard.Rover,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}