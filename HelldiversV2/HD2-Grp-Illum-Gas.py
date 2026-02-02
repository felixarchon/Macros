#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Illum Gas',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.LaserCannon,        
        GuardDogs.DogBreath,
        SupportWeapons.QuasarCannon,

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.AutoCannon,
        Orbitals.Precision,

        # 3rd row ----------
        Orbitals.RailCannon,
        Orbitals.Gatling,        
        Eagles.Bomb_500kg,
        
        # 4th row ----------
        Missions.Resupply,
        GuardDogs.Rover,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}