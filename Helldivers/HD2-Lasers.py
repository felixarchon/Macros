#Macropad, Hotkeys - Helldivers 2 - Early Bug Solo Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
guard = GuardDogs()
back = Backpacks()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Lasers',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.LaserCannon,
        support.QuasarCannon,
        guard.Rover,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,        
        sentry.EMS,

        # 3rd row ----------
        orbital.Laser,
        orbital.RailCannon,
        sentry.Tesla,
        
       # 4th row ----------
        mission.Resupply,
        sentry.Mortar,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}