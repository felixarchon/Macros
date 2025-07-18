#Macropad, Hotkeys - Helldivers 2 - Early Illuminate Solo Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs

support = SupportWeapons()
guard = GuardDogs()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Solo Illum Runs',
    'macros' : [
        # 1st row ----------
        support.MachineGun,
        support.LaserCannon,
        guard.Rover,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        sentry.EMS,

        # 3rd row ----------
        orbital.Barrage_120mm,
        orbital.Precision,
        orbital.RailCannon,

        # 4th row ----------
        mission.Resupply,
        support.GrenadeLauncher,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}