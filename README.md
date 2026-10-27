# Macros
These macros are for a [Macropad](https://www.adafruit.com/product/5128), using the [Hotkeys](https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/main/Macropad_Hotkeys) library.

To use, copy the needed library classes to the `lib` folder of the Macropad (after installing Hotkeys or a Hotkey varient on it).

Copy the relevant macro files to the `macro` folder of the Macropad.

For help with Circuit Python, visit [Adafruit](https://learn.adafruit.com/welcome-to-circuitpython).
Want the files smaller? Look into using [mpy-cross](https://learn.adafruit.com/welcome-to-circuitpython/library-file-types-and-frozen-libraries#what-is-an-mpy-file-3117820)



## General

### HotKeys Code Changes (use yield)
Due to the size in memory of Macros this project is undertaking and the number of macros the project owner wishes to be on the macropad, a small change has been made to the base code.py of HotKeys. If you don't wish to change HotKeys, the old methods remain and are simply commented out. Remove the `yield`-based methods and uncomment the old ones.

For the `yield`-based methods add the following code to your base code.py file:
Inside the main while statement add the below code after:   `sequence = apps[app_index].macros[key_number][2]`

```python
    # --- ADDED: Execute callable/lambda to instantiate fresh generator ---
    if callable(sequence):
        sequence = sequence()
```
and before the code:    `if pressed:`
If you don't want to change your code.py, remove the yield-based methods and uncomment the others, then remove the `lambda:` from each stratagem. `lambda:` is supposed to allow more macros  (more memory efficient).

Example:
```python
    MachineGun = (HD2.Support, 'MG', lambda: HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.DOWN,HD2.UP,HD2.RIGHT))
```
should change to 
```python
    MachineGun = (HD2.Support, 'MG', HD2.stratagem(HD2.DOWN,HD2.LEFT,HD2.DOWN,HD2.UP,HD2.RIGHT))
```

## Guild Wars 2

coming soon

## Helldivers

Inspired by the [macros](https://adafruit-playground.com/u/squid_jpg/pages/easy-helldivers-ii-stratagem-macros-for-rp2040-macropad) posted on Adafruit.

### Setup

Place the [HD2_Stratagem_List_v2.py](/lib/HD2_Stratagem_List_v2.py) in the `lib` folder of the Hotkeys code, on the Macropad.

Individual macro files to be used should be placed in the `macros` folder of the Hotkeys code.

The included macro files are just examples of how to write your own macros using the `HD2_Stratagem_List_v2.py` Library. The concept behind the example files is that each file is a potential and flexible loadout for a given situation and several macros can be loaded and navigated through at need, depending on the situation or loadout being used.

## Visual Studio

coming soon

## Customize
To make a macro file, do the following basics:
```python
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

## Updates Notes
- 10/26/2026: Sped up Guild Wars emotes and Readme updates
- 10/25/2026: HD2: Added Scope of Authority stratagems
- 9/30/2026: HD2: Comm Wheel macros
- 9/26/2026: Library files converted to yield statements
- 3/22/2026: Stoker, Readme, Appropriators
- 3/17/2026: Updated HD2 library to match changes in the March 13th, 2026 Patch
  - Added B/FLAM-80 Cremator as Cremetor
  - Updated the OneTwo and C4 Swap functions
  - Renamed EMS Mortar from EMS to MortarEMS
  - Added Gas Mortar as MortarGas 

