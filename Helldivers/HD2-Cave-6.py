#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Missions, GuardDogs, Backpacks, Vehicles, Eagles, Orbitals

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
guard = GuardDogs()
veh = Vehicles()
eagle = Eagles()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Cave 6',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.LaserCannon,
        back.Warp,
        support.Speargun,

        # 2nd row ----------
        sentry.MachineGun,
        eagle.Rockets_110mm,
        guard.DogBreath,

        # 3rd row ----------
        veh.EmancipatorExosuit,
        orbital.RailCannon,
        eagle.Bomb_500kg,
        
        # 4th row ----------
        mission.Resupply,
        back.Supply,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}