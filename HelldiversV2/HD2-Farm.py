#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Farm',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.GrenadeLauncher,
        Backpacks.Warp,
        SupportWeapons.LaserCannon,

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.Gatling,
        SupportWeapons.ExpendableAntiTank,

        # 3rd row ----------
        Orbitals.Gatling,
        Orbitals.Precision,
        Eagles.Strafing,
        
        # 4th row ----------
        Missions.Resupply,
        GuardDogs.Rover,
        Eagles.Airstrike,
        
        # Encoder button ---
        none,
    ]
}