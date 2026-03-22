# Macros
These macros are for a [Macropad](https://www.adafruit.com/product/5128), using the [Hotkeys](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/Macropad_Hotkeys) library.

To use, copy the needed library classes to the `lib` folder of the Macropad (after installing Hotkeys or a Hotkey varient on it).

Copy the relevant macro files to the `macro` folder of the Macropad.

For help with Circuit Python, visit [Adafruit](https://learn.adafruit.com/welcome-to-circuitpython).
Want the files smaller? Look into using [mpy-cross](https://learn.adafruit.com/welcome-to-circuitpython/library-file-types-and-frozen-libraries#what-is-an-mpy-file-3117820)

# General

coming soon

# Guild Wars 2

coming soon

# Helldivers

Inspired by the [macros](https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad) posted on Adafruit.

## Setup

Place the [HD2_Stratagem_List_v2.py](/lib/HD2_Stratagem_List_v2.py) in the `lib` folder of the Hotkeys code, on the Macropad.

Individual macro files to be used should be placed in the `macros` folder of the Hotkeys code.

The included macro files are just examples of how to write your own macros using the `HD2_Stratagem_List_v2.py` Library. The concept behind the example files is that each file is a potential and flexible loadout for a given situation and several macros can be loaded and navigated through at need, depending on the situation or loadout being used.

# Visual Studio

coming soon

# Customize
To make a macro file, do the following basics:
```
# Import the relevant library file and needed classes
from HD2_Stratagem_List_v2 import SupportWeapons, Orbitals, Sentries, Missions, Functions, Backpacks

# Setup any custom-to-the-macro variables
none = (0x000000, '', [])

# Add 4 + 1 rows of things (or leave them blank with a "none")
app = {
    'name' : 'HD2 - Appropriators',
    'macros' : [
        # COLOR     LABEL       KEY SEQUENCE
        # 1st row ----------
        SupportWeapons.C4,        
        SupportWeapons.Spear,
        Backpacks.Warp,        

        # 2nd row ----------
        Sentries.MachineGun,
        Sentries.AutoCannon,
        Orbitals.Precision,

        # 3rd row ----------
        SupportWeapons.Commando,
        SupportWeapons.ExpendableAntiTank,        
        Orbitals.Laser,
       
        # 4th row ----------
        Missions.Resupply,
        Functions.Left_Swap,
        Missions.Reinforce,
        
        # Encoder button ---
        none,
    ]
}
```

# Updates Notes
- 3/22/2026: Stoker, Readme, Appropriators
- 3/17/2026: Updated HD2 library to match changes in the March 13th, 2026 Patch
  - Added B/FLAM-80 Cremator as Cremetor
  - Updated the OneTwo and C4 Swap functions
  - Renamed EMS Mortar from EMS to MortarEMS
  - Added Gas Mortar as MortarGas 

