# # Photonics 2 Lab - Experiment Notebook

# # Experiment plans
#
# * _Space for notes and experiment plans_

# # 00 - Import libraries, setup tools, functions, and GUI

# +
# %gui qt
import puzzlepiece as pzp

# Puzzlepieces
from puzzlepiece.pieces import scan_value, plotter
from puzzlepiece.extras import ipython_shims
from BathPhotonics2Lab_pieces import Andor, Spot_trigger, NIDAQ, AOM, LL, Basler, SerialTerminal, ll_viewer_onsite

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

# Experiment detail dropdowns (add to the option list if frequently use)
class Sample(pzp.Piece):
    def define_params(self):
        pzp.param.text(self, "date", datetime.date.today().strftime('%Y%m%d'))(None)
        pzp.param.dropdown(self, "sample", "Rh6G flim")(["Rh6G flim"])
        pzp.param.dropdown(self, "part", "Flat")(["Flat"])
        pzp.param.spinbox(self, "i", 0)(None)

# Make the app window (Puzzle)
shell = get_ipython()

# Change the debug flag to True for debug mode
puzzle = pzp.Puzzle(shell.kernel.app, "DMD scan", debug=False)

folder = puzzle.add_folder(0, 0, 4, 4)
folder.add_piece('Andor', Andor.Piece)
folder.add_piece('Basler', Basler.LineoutPiece)
folder.add_piece('Plotter', plotter.Piece)
folder.add_piece('LL reader', ll_viewer_onsite.Piece)
puzzle.add_piece('Sample', Sample, 4, 0, 1, 1)
puzzle.add_piece('NIDAQ', NIDAQ.Piece, 1, 4, 1, 2)
puzzle.add_piece('Spot terminal', SerialTerminal.Piece, 0, 4, 1, 1)
puzzle.add_piece('Spot trigger', Spot_trigger.Piece, 3, 4, 1, 1)
puzzle.add_piece('AOM', AOM.Piece, 4, 4, 1, 2)
puzzle.add_piece('LL', LL.Piece, 4, 2, 1, 1)
# puzzle.add_piece('Thorlabs PM', ThorlabsPM.Piece, 3, 3, 1, 1)

puzzle.show()
mf.puzzle = puzzle
# -
# # 01 - Device Settings

# Andor
puzzle['Andor:grating'].set_value('02 - 600 lpmm, 500nm')
puzzle['Andor:exposure'].set_value(10)        # milliseconds
puzzle['Andor:centre'].set_value(0)            # nanometers
puzzle['Andor:slit_width'].set_value(30)        # micrometers
puzzle['Andor:temp_status'].get_value()
puzzle['Andor:autolevel'].set_value(True);


# +
## Connect to NIDAQ first
## Spot trigger
puzzle['Spot trigger:counter'].set_value('CTR0')
puzzle['Spot trigger:PFI port'].set_value('PFI12')
puzzle['Spot trigger:Rep rate'].set_value(1.0)    # kHz
puzzle['Spot trigger:pulses'].set_value(1)

## AOM
puzzle['AOM:AO port'].set_value('AO0')
puzzle['AOM:mod_in'].set_value(0.0);        # Voltage

# -

# Note: Andor slit centre = 503 px

# # 02 - LL Module
# LL measurements (power-dependent measurement) can be done either by <strong>interacting with the GUI</strong> or <strong>programmatically</strong>. \
# The cells below shows an example how to programmatically run a LL measurement.
#
# Or for <strong>a single frame acquisition</strong>, use:
# ``` python
# frame = puzzle['Andor'].get_image(signal_delay = 50, timeout_ms=5000)
# ```
# which includes a measurement sequence:\
# Ask Andor to wait for a frame &rarr; Send signal to fire laser pulses &rarr; Extract frame from Andor as ```frame```

# +
# %%pzp_script
# Set sample & measurement details
set:Sample:date:20251217
set:Sample:sample:SAMPLE_NAME
set:Sample:part:PART_NAME

# Set scan parameters
set:LL:start:0
set:LL:end:5
set:LL:N:40

# Set i value - for filename
set:Sample:i:1

####################
# Set filename (no need to change)
set:LL:filename:data/DATA_{Sample:date}_{Sample:sample}_{Sample:part}_{Sample:i;:02d}.ds

# +
# %%play_notification_sound
# ^ Comment the line above to mute the notification sound

# Run LL scan
puzzle['LL'].actions['Scan']()
mf.plot_ll_result()
# -

# --------

