#Macropad, Hotkeys - Helldivers 2 - Blitz Build
from HD2_Stratagem_List_v2 import SupportWeapons, Orbitals, Missions, GuardDogs, Backpacks, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Blitz',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.MissleSilo,
        Backpacks.Warp,
        SupportWeapons.QuasarCannon,

        # 2nd row ----------
        Orbitals.Precision,
        Eagles.Bomb_500kg,
        GuardDogs.DogBreath,
        
        # 3rd row ----------
        Orbitals.Gatling,
        Orbitals.Gas,
        Orbitals.Barrage_120mm,
        
        # 4th row ----------
        Missions.Resupply,
        Backpacks.ShieldGenerator,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}