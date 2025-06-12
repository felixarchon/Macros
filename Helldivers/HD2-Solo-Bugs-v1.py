#Macropad, Hotkeys - Helldivers 2 - Early Bug Solo Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
guard = GuardDogs()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Solo Bug Runs',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.MachineGun,
        support.RecoillessRifle,
        guard.Rover ,

        # 2nd row ----------
        sentry.AutoCannon,
        sentry.MachineGun,
        sentry.Rocket,

        # 3rd row ----------
        orbital.Barrage_120mm,
        orbital.Precision,
        orbital.Barrage_380mm,
        # 4th row ----------
        mission.Resupply,
        support.Commando,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}