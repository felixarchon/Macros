#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Eagles

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
eagle = Eagles()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Farm Illum 2',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.Stallwart,
        back.Warp,
        support.MachineGun,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.Gatling,
        back.Supply,

        # 3rd row ----------
        orbital.Airburst,
        eagle.Airstrike,
        orbital.RailCannon,
        
        # 4th row ----------
        mission.Resupply,
        support.LaserCannon,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}