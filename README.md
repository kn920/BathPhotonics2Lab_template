# Bath Photonics 2 Lab Template

Experiment notebook template for the Photonics 2 Lab, Department of Physics, University of Bath.  

## Overview

This template shows how to use the modular **puzzlepiece** GUI module to control devices and automate experiments in a Jupyter notebook.  
It contains basic, prewritten experiment code for standard measurement routines. It works together with user-defined pieces to communicate with hardware and perform measurements. This template is designed for use in the Bath Photonics 2 Lab.  

## Standard Routine (Bath Photonics 2 Lab)  

1. (_Not necessary every time_) Sync the repository with GitHub to get the latest version of the template.  

2. Duplicate the template folder and rename it (e.g., `<Date>_<Title_of_the_experiment>`).  

3. In this folder, open Windows PowerShell by pressing `Shift` + right-click, and selecting **Open PowerShell window here**.  

4. (_If a virtual environment is required_) Activate the virtual environment (e.g., `venv`, located in `C:/lab_automation/venv/`) by running:  
   ```powershell
   C:/lab_automation/venv/Scripts/Activate.ps1
   ```

   **Or**, if you have a PowerShell profile shortcut set up, simply run:  
   ```powershell
   venv
   ```

5. Open Jupyter Lab with:  
   ```powershell
   jupyter lab
   ```

6. In Jupyter Lab, open the experiment notebook by right-clicking `experiment_notebook.py` and selecting **Open With → Notebook**.  

7. To initialise the notebook GUI, run **Sections 00** and **Section 01**. Device initialisation can then be done either by running **Section 02** or manually with the GUI. Measurements can be automated using the code in **Section 03** and onward. Users are free to write additional code (and more sections) to control devices or perform other measurements.  

## Related Projects  
[**BathPhotonics2Lab_pieces**](https://github.com/kn920/BathPhotonics2Lab_pieces/tree/main) - Pieces for device communication and experiment automation.
