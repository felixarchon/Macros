#Macropad, Hotkeys - Helldivers 2 - Early Terminid Group Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs

support = SupportWeapons()
guard = GuardDogs()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Bug Runs',
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
        sentry.MachineGun,

        # 4th row ----------
        mission.Resupply,
        support.Commando,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}