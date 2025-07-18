#Macropad, Hotkeys - Helldivers 2 - Mission Stratagems
from HD2_Stratagem_List import Missions

mission = Missions()

none = (0x000000, '', [])

app = {
    'name' : 'HD2 - Missions',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        mission.Hellbomb,
        mission.SSSD,
        mission.SeismicProbe,

        # 2nd row ----------
        mission.UploadData,
        mission.EagleReArm,        
        mission.IlluminationFlare,

        # 3rd row ----------
        mission.SEAFArtillery,
        mission.SuperEarthFlag,
        none,
        
       # 4th row ----------
        none,
        none,
        none,
        
        # Encoder button ---
        none,
    ]
}