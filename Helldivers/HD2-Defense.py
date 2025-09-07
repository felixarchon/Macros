#Macropad, Hotkeys - Helldivers 2 - Early Bug Solo Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, Backpacks

support = SupportWeapons()
back = Backpacks()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Defense',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        back.ShieldGenerator,
        support.AutoCannon,
        sentry.HeavyMachineGunEmplacement,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        sentry.AntiTankEmplacement,

        # 3rd row ----------
        orbital.RailCannon,
        sentry.AntiTankMines,
        sentry.Rocket,

        # 4th row ----------
        mission.Resupply,
        sentry.Shield,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}