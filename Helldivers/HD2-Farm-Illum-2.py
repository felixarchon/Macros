#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Eagles

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
eagle = Eagles()
guard = GuardDogs()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Farm Illum 2',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.Stallwart,
        guard.Rover,
        support.MachineGun,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.Gatling,
        support.LaserCannon,

        # 3rd row ----------
        orbital.Precision,
        orbital.Airburst,
        eagle.Airstrike,        
        
        # 4th row ----------
        mission.Resupply,
        back.Warp,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}