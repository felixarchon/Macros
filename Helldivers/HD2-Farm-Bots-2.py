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
    'name' : 'HD2 - Farm Bots 2',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.MachineGun,
        back.Warp,
        support.QuasarCannon,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.Gatling,
        orbital.RailCannon,

        # 3rd row ----------
        orbital.Barrage_120mm,
        eagle.Bomb_500kg,
        vehicle.FastReconVehicle,
        
        # 4th row ----------
        mission.Resupply,
        orbital.Gatling,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}