#Macropad, Hotkeys - Helldivers 2 - Appropriators Build alpha
from HD2_Stratagem_List_v2 import SupportWeapons, Orbitals, Sentries, Missions, Functions, Backpacks

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Appropriators',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.C4,        
        SupportWeapons.Spear,
        Backpacks.Warp,        

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.AutoCannon,
        Orbitals.Precision,

        # 3rd row ----------
        SupportWeapons.Commando,
        SupportWeapons.ExpendableAntiTank,        
        Orbitals.Laser,
       
        # 4th row ----------
        Missions.Resupply,
        Functions.Left_Swap,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}