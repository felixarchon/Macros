#Macropad, Hotkeys - Helldivers 2 - Eradicate Build
from HD2_Stratagem_List import SupportWeapons, Orbitals, Missions, Backpacks, Eagles

support = SupportWeapons()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
eagle = Eagles()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Eradicate',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.AutoCannon,
        back.Warp,
        support.QuasarCannon,

        # 2nd row ----------
        orbital.Precision,
        eagle.Bomb_500kg,
        support.RecoillessRifle,
        # 3rd row ----------
        orbital.Gatling,
        orbital.Gas,
        orbital.Barrage_120mm,
        
        # 4th row ----------
        mission.Resupply,
        back.ShieldGenerator,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}