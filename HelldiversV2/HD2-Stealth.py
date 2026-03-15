#Macropad, Hotkeys - Helldivers 2 - C4 Build
from HD2_Stratagem_List_v2 import SupportWeapons, Missions, Backpacks, Eagles, Functions

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Stealth',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.C4,
        SupportWeapons.Speargun,
        SupportWeapons.MissleSilo,

        # 2nd row ----------
        SupportWeapons.PortableHellbomb,
        Backpacks.Supply,
        none,

        # 3rd row ----------
        Eagles.Bomb_500kg,
        none,
        none,
       
        # 4th row ----------
        Missions.Resupply,
        Functions.C4_Swap_Fire,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}