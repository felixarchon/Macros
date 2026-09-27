#Macropad, Hotkeys - Helldivers 2 - C4 Build
from HD2_Stratagem_List_v2 import Functions, Missions

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Function Test',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        Functions.ArmDropHellbomb,
        Functions.DropStratagem,
        Functions.DropBackpack,

        # 2nd row ----------
        Functions.DropSamples,
        Functions.C4_Swap_Fire,
        Functions.OneTwo_Swap_Fire,

        # 3rd row ----------
        none,
        none,
        none,
       
        # 4th row ----------
        Missions.Resupply,
        none,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}