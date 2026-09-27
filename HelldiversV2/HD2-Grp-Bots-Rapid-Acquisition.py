#Macropad, Hotkeys - Helldivers 2 - Early Automaton Group Build
from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Orbitals, Missions, Backpacks, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Bots Rapid Acq',
    'macros' : [
        # 1st row ----------
        Orbitals.Smoke,
        Sentries.Shield,
        Backpacks.ShieldGenerator,

        # 2nd row ----------
        Sentries.Rocket,
        Sentries.AutoCannon,
        SupportWeapons.ExpendableAntiTank,

        # 3rd row ----------
        Orbitals.RailCannon,
        SupportWeapons.Commando,
        Orbitals.Laser,

        # 4th row ----------
        Missions.Resupply,
        SupportWeapons.MissleSilo,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}