#Macropad, Hotkeys - Helldivers 2 - C4 Build
from HD2_Stratagem_List_v2 import SupportWeapons, Missions, Orbitals, Eagles, Sentries, Functions

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - C4',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.C4,
        Orbitals.Precision,
        Orbitals.Gatling,

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.AutoCannon,
        none,

        # 3rd row ----------
        Eagles.Bomb_500kg,
        none,
        none,
       
        # 4th row ----------
        Missions.Resupply,
        none,
        Missions.Reinforce,
        
        # Encoder button ---
        Functions.C4_Swap_Fire,
    ]
}