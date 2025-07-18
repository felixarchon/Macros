#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Vehicles, Eagles

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
vehicle = Vehicles()
eagle = Eagles()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Farm Bugs 2',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.GrenadeLauncher,
        back.Jump,
        support.QuasarCannon,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        sentry.EMS,

        # 3rd row ----------
        orbital.RailCannon,
        eagle.Bomb_500kg,
        vehicle.FastReconVehicle,
        
        # 4th row ----------
        mission.Resupply,
        support.AutoCannon,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}