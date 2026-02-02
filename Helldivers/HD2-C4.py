#Macropad, Hotkeys - Helldivers 2 - C4 Build
from HD2_Stratagem_List import SupportWeapons, Orbitals, Missions, GuardDogs, Backpacks, Eagles, Functions

support = SupportWeapons()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
eagle = Eagles()
guard = GuardDogs()
func = Functions()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - C4',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        func.F21,
        func.F22,
        func.F23,

        # 2nd row ----------
        func.F24,
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