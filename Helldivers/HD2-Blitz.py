#Macropad, Hotkeys - Helldivers 2 - Blitz Build
from HD2_Stratagem_List import SupportWeapons, Orbitals, Missions, GuardDogs, Backpacks, Eagles

support = SupportWeapons()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
eagle = Eagles()
guard = GuardDogs()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Blitz',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.MissleSilo,
        back.Warp,
        support.QuasarCannon,

        # 2nd row ----------
        orbital.Precision,
        eagle.Bomb_500kg,
        guard.DogBreath,
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