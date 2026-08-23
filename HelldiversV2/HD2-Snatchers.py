#Macropad, Hotkeys - Helldivers 2 - Appropriators Build alpha
from HD2_Stratagem_List_v2 import SupportWeapons, Orbitals, Sentries, Missions, Functions, Backpacks, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Snatchers',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.C4,        
        SupportWeapons.WASP,
        Backpacks.Warp,        

        # 2nd row ----------
        SupportWeapons.Railgun,
        Sentries.AutoCannon,
        Orbitals.Precision,

        # 3rd row ----------
        Orbitals.Barrage_Napalm,
        Eagles.Napalm,        
        Orbitals.Laser,
       
        # 4th row ----------
        Missions.Resupply,
        SupportWeapons.ExpendableNapalm,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}