#Macropad, Hotkeys - Helldivers 2 - Farming Build
from HD2_Stratagem_List import SupportWeapons, Sentries, Orbitals, Missions, GuardDogs, Backpacks

support = SupportWeapons()
sentry = Sentries()
orbital = Orbitals()
mission = Missions()
back = Backpacks()
guard = GuardDogs()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Cave 2',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        support.LaserCannon,
        guard.Rover,
        support.QuasarCannon,

        # 2nd row ----------
        sentry.MachineGun,
        sentry.Gatling,
        guard.DogBreath,

        # 3rd row ----------
        back.Supply,
        support.RecoillessRifle,
        guard.KNine,
        
        # 4th row ----------
        mission.Resupply,
        support.GrenadeLauncher,
        mission.Reinforce,
        
        # Encoder button ---
        none,
    ]
}