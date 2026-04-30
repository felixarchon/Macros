from HD2_Stratagem_List_v2 import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Eagles

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Fire',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.QuasarCannon,
        GuardDogs.HotDog,
        SupportWeapons.Cremator,

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.Flame,
        SupportWeapons.Flamethrower,

        # 3rd row ----------
        Orbitals.Barrage_Napalm,
        Orbitals.RailCannon,
        Eagles.Napalm,
        
        # 4th row ----------
        Missions.Resupply,
        GuardDogs.DogBreath,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}