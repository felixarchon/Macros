#Macropad, Hotkeys - Helldivers 2 - Early Illuminate Group Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Illum Runs',
    'macros' : [
        # 1st row ----------
        support.AutoCannon,
        support.Spear,
        support.RecoillessRifle,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        sentry.Rocket,

        # 3rd row ----------
        orbital.Barrage_120mm,
        orbital.Precision,
        orbital.Gatling,

        # 4th row ----------
        mission.Resupply,
        mission.SOS,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}