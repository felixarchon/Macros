#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Missions, GuardDogs, Backpacks, Vehicles, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Cave',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.LaserCannon,
        Backpacks.Warp,
        SupportWeapons.Speargun,

        # 2nd row ----------
        Sentries.MachineGun,
        Eagles.Rockets_110mm,
        GuardDogs.DogBreath,

        # 3rd row ----------
        Vehicles.EmancipatorExosuit,
        orbital.RailCannon,
        eagle.Bomb_500kg,
        
        # 4th row ----------
        Missions.Resupply,
        Backpacks.Supply,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}