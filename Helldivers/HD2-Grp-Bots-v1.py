#Macropad, Hotkeys - Helldivers 2 - Early Automaton Group Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs

support = SupportWeapons()
guard = GuardDogs()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Bot Runs',
    'macros' : [
        # 1st row ----------
        support.AutoCannon,
        support.RecoillessRifle,
        support.HeavyMachineGun,

        # 2nd row ----------
        sentry.AutoCannon,
        sentry.Rocket,
        sentry.EMS,

        # 3rd row ----------
        orbital.Barrage_120mm,
        orbital.Precision,
        none,

        # 4th row ----------
        mission.Resupply,
        mission.SOS,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}