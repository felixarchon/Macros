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
    'name' : 'HD2 - Defense',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.HeavyMachineGun,
        back.Supply,
        guard.Rover,

        # 2nd row ----------
        sentry.AutoCannon,
        sentry.EMS,
        sentry.Mortar,

        # 3rd row ----------
        orbital.RailCannon,
        sentry.HeavyMachineGunEmplacement,
        back.ShieldGenerator,
        # 4th row ----------
        mission.Resupply,
        support.AutoCannon,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}