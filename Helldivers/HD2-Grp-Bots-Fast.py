#Macropad, Hotkeys - Helldivers 2 - Early Automaton Group Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, Backpacks, Eagles

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
eagle = Eagles()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Grp Bots Fast',
    'macros' : [
        # 1st row ----------
        support.ExpendableAntiTank,
        support.Commando,
        back.ShieldGenerator,

        # 2nd row ----------
        sentry.Rocket,
        sentry.AutoCannon,
        support.ExpendableNapalm,

        # 3rd row ----------
        orbital.RailCannon,
        orbital.Precision,
        eagle.Bomb_500kg,

        # 4th row ----------
        mission.Resupply,
        support.MissleSilo,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}