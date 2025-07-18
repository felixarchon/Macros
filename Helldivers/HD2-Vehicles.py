#Macropad, Hotkeys - Helldivers 2 - Vehicles 
from HD2_Stratagem_List import Vehicles

vehicle = Vehicles()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Vehicles',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        vehicle.PatriotExosuit,
        vehicle.EmancipatorExosuit,
        vehicle.FastReconVehicle,

        # 2nd row ----------
        none,
        none,
        none,

        # 3rd row ----------
        none,
        none,
        none,
        # 4th row ----------
        none,
        none,
        none,
        
        # Encoder button ---
        none,
    ]
}