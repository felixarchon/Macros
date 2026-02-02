#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Bugs Gas',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.ExpendableAntiTank,
        Backpacks.Warp,
        SupportWeapons.QuasarCannon,

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.AutoCannon,
        Orbitals.Laser,

        # 3rd row ----------
        Orbitals.RailCannon,
        Orbitals.Barrage_120mm,        
        Eagles.Bomb_500kg,
        
        # 4th row ----------
        Missions.Resupply,
        GuardDogs.DogBreath,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}