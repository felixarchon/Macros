from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks, Eagles

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
eagle = Eagles()
guard = GuardDogs()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Special',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.GrenadeLauncher,
        back.Warp,
        support.LaserCannon,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.Gatling,
        orbital.Laser, #Special Here

        # 3rd row ----------
        orbital.Gatling,
        orbital.Precision,
        eagle.Strafing,
        
        # 4th row ----------
        mission.Resupply,
        guard.Rover,
        eagle.Airstrike,
        
        # Encoder button ---
        none,
    ]
}