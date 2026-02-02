#Macropad, Hotkeys - Helldivers 2 - Early Automaton Group Build
from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Orbitals, Missions, Backpacks, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Bots Fast',
    'macros' : [
        # 1st row ----------
        SupportWeapons.ExpendableAntiTank,
        SupportWeapons.Commando,
        Backpacks.ShieldGenerator,

        # 2nd row ----------
        Sentries.Rocket,
        Sentries.AutoCannon,
        SupportWeapons.AntiMaterial,

        # 3rd row ----------
        Orbitals.RailCannon,
        Orbitals.Precision,
        Eagles.Bomb_500kg,

        # 4th row ----------
        Missions.Resupply,
        SupportWeapons.MissleSilo,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}