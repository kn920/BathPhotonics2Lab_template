# # Photonics 2 Lab - Experiment Notebook

# # Experiment plans
#
# * ^^Note down the plans of the experiment^^

# # 00 - Import libraries, setup tools, and functions

# +
# %gui qt
import puzzlepiece as pzp

# Puzzlepieces
from puzzlepiece.pieces import scan_value, plotter
from puzzlepiece.extras import ipython_shims
from BathPhotonics2Lab_pieces import Andor, Spot_laser, Spot_trigger, NIDAQ, AOM, LL

# Measurement function
import measurement_functions as mf

# General libraries
from tqdm.notebook import tqdm
import numpy as np
# %matplotlib qt
import matplotlib.pyplot as plt
import datetime
import os
import datasets as ds


# -
# Experiment detail dropdowns (add to the options only if always use)
class Sample(pzp.Piece):
    def define_params(self):
        pzp.param.text(self, "date", datetime.date.today().strftime('%Y%m%d'))(None)
        pzp.param.dropdown(self, "sample", "Rh6G flim")(["Rh6G flim"])
        pzp.param.dropdown(self, "part", "Flat")(["Flat"])
        pzp.param.spinbox(self, "i", 0)(None)


# # 01 - Create the Puzzlepiece window

# +
# Make the app window (Puzzle)
# Remember to change the debug flag as needed

shell = get_ipython()
puzzle = pzp.Puzzle(shell.kernel.app, "DMD scan", debug=False)

folder = puzzle.add_folder(0, 0, 3, 3)
folder.add_piece('Andor', Andor.Piece)
folder.add_piece('Plotter', plotter.Piece)
puzzle.add_piece('Sample', Sample, 3, 0, 1, 1)
puzzle.add_piece('NIDAQ', NIDAQ.Piece, 0, 4, 1, 1)
puzzle.add_piece('Spot laser', Spot_laser.Piece, 1, 4, 1, 1)
puzzle.add_piece('Spot trigger', Spot_trigger.Piece, 2, 4, 1, 1)
puzzle.add_piece('AOM', AOM.Piece, 3, 4, 1, 1)
puzzle.add_piece('LL', LL.Piece, 3, 2, 1, 1)
# puzzle.add_piece('Thorlabs PM', ThorlabsPM.Piece, 3, 3, 1, 1)

puzzle.show()
mf.puzzle = puzzle
# -

# # 02 - Device initialisation

# +
# Andor initialisation (First manually connect to Andor)

# puzzle['Andor:slit_width'].set_value(30)        # micrometers

puzzle['Andor:exposure'].set_value(100)        # milliseconds
puzzle['Andor:grating'].set_value('02 - 600 lpmm, 500nm')
puzzle['Andor:centre'].set_value(0)            # nanometers
puzzle['Andor:temp_status'].get_value()
puzzle['Andor:autolevel'].set_value(True);


# +
# Laser initialisation
## NIDAQ
puzzle['NIDAQ:connected'].set_value(True)

## Spot laser
puzzle['Spot laser:COM'].get_value()
puzzle['Spot laser:COM'].set_value('COM3')
puzzle['Spot laser:connected'].set_value(True)

## Spot trigger
puzzle['Spot trigger:counter'].set_value('CTR0')
puzzle['Spot trigger:PFI port'].set_value('PFI12')
puzzle['Spot trigger:Rep rate'].set_value(1.0)

## AOM
puzzle['AOM:AO port'].set_value('AO0')
puzzle['AOM:mod_in'].set_value(0.0);        # Voltage

# -

# Note: Andor slit centre = 503 px

# # 03 - LL Module

# +
# %%pzp_script
# Set sample & measurement details
set:Sample:date:20250722
set:Sample:sample:SAMPLE
set:Sample:part:PART

# Set scan parameters
set:LL:start:0
set:LL:end:5
set:LL:N:40

# Set i value - for filename
set:Sample:i:1

####################
# Set filename & run
set:LL:filename:data/DATA_{Sample:date}_{Sample:sample}_{Sample:part}_{Sample:i;:02d}.ds
# -

# %%play_notification_sound
# Run LL scan
puzzle['LL'].actions['Scan']()
mf.plot_ll_result()


