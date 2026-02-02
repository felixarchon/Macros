#Macropad, Hotkeys - Helldivers 2 - Early Bug Solo Build
from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Orbitals, Missions, Backpacks

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Defense',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        Backpacks.ShieldGenerator,
        SupportWeapons.AutoCannon,
        Sentries.HeavyMachineGunEmplacement,

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.AutoCannon,
        Sentries.AntiTankEmplacement,

        # 3rd row ----------
        Orbitals.RailCannon,
        Sentries.AntiTankMines,
        Sentries.Rocket,

        # 4th row ----------
        Missions.Resupply,
        Sentries.Shield,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}