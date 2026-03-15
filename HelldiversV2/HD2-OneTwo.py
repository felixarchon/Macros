#Macropad, Hotkeys - Helldivers 2 - Illuminate OneTwo Build
from HD2_Stratagem_List_v2 import SupportWeapons, GuardDogs, Orbitals, Eagles, Sentries, Missions, Functions, Backpacks

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - 1-2',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.LaserCannon,        
        GuardDogs.DogBreath,
        Backpacks.Warp,        

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.AutoCannon,
        SupportWeapons.Quasar,        

        # 3rd row ----------
        Eagles.Bomb_500kg,
        Orbitals.Precision,
        Orbitals.Laser,
       
        # 4th row ----------
        Missions.Resupply,
        Functions.OneTwo_Swap_Fire,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}