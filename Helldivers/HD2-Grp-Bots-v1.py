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
    'name' : 'HD2 - Grp Bot Runs',
    'macros' : [
        # 1st row ----------
        support.QuasarCannon,
        support.Spear,
        back.ShieldGenerator,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        sentry.EMS,

        # 3rd row ----------
        orbital.RailCannon,
        orbital.Barrage_380mm,
        eagle.Bomb_500kg,

        # 4th row ----------
        mission.Resupply,
        eagle.Rockets_110mm,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}