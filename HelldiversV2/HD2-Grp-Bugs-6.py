#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Orbitals, Missions, Backpacks, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Bugs 6',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.AutoCannon,
        Backpacks.Warp,
        SupportWeapons.QuasarCannon,

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.AutoCannon,
        Orbitals.Laser,

        # 3rd row ----------
        Orbitals.Barrage_120mm,
        Orbitals.RailCannon,
        Eagles.Bomb_500kg,
        
        # 4th row ----------
        Missions.Resupply,
        SupportWeapons.RecoillessRifle,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}