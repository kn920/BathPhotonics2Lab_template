# Bath Photonics 2 Lab Template

Experiment notebook template for the Photonics 2 Lab, Department of Physics, University of Bath.  

## Overview

This template show how to use the modular **puzzlepiece** GUI module to allow control of device and experiment automation in a jupyter notebook.  
This template contains the most basic, prewritten experiment codes for standard measurement rountines. It work together with the user-defined pieces to communicate with the hardware and perform measurements. These template is designed for the use in Bath Photonics 2 Lab.  

## Standard routine (Bath Photonics 2 Lab)  

1. (_Not neccessarly everytime_) Sync the repository with Github for the latest version of template.

2. Duplicate the template folder and rename it (e.g., `<Date>_<Title_of_the_experiment>`)

2. In this folder, open Windows PowerShell by `Shift`+`right click`, and select `Open PowerShell window here`.

3. (_If vritual environment required_) Activate the vritual environment (e.g., venv, located in `C:/lab_automation/venv/`) by 
```
C:/lab_automation/venv/Scripts/Activate.ps1
```

**Or**

Run the shortcut
```
venv
```
if the shortcut is set.

4. Open Jupyter lab with 
```
Jupyter lab
```

5. Open the experiment notebook by right-click the  `experiment_notebook.py` and select `Open With -> Notebook`.

6. To initalise the notebook GUI, run section 00 and 01. The device initialisation can then be done either by running section 02 or manually with the GUI. The measurement can be automated with the code in section 03 and onward. User are free to write any code to control the devices or perform other measurements. 

## Related Projects  
[**BathPhotonics2Lab_pieces**](https://github.com/kn920/BathPhotonics2Lab_pieces/tree/main)