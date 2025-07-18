#Macropad, Hotkeys - Helldivers 2 - Early Bot Solo Build
from HD2_Stratagem_List import SupportWeapons, Backpacks, Sentries, Orbitals, Missions, Eagles

support = SupportWeapons()
pack = Backpacks()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
eagle = Eagles()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Solo Bot Runs',
    'macros' : [
        # 1st row ----------
        support.Spear,
        support.RecoillessRifle,
        support.LaserCannon,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.AutoCannon,
        pack.ShieldGenerator,

        # 3rd row ----------
        orbital.RailCannon,
        orbital.Precision,
        eagle.Rockets_110mm,

        # 4th row ----------
        mission.Resupply,
        eagle.Bomb_500kg,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}