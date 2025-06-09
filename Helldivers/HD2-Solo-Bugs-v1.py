#Macropad, Hotkeys - Helldivers 2 - Early Bug Solo Build
from HD2_Stratagem_List import SupportWeapons, Backpacks, Sentries, Orbitals, Missions

support = SupportWeapons()
pack = Backpacks()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()

app = {
    'name' : 'HD2 - Solo Bug Runs',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.HeavyMachineGun,
        support.AutoCannon,
        pack.Supply,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.Gatling,
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
        (0x000000, '',          []),
    ]
}