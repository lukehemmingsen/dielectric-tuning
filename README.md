# dielectric-tuning

The scripts provided through this project are all Python scripts which run correctly using Python 2.7.3 (imported via the command 'module load python/2.7.3').
If Python 2.7.3 is loaded correctly and the splineplot and generateFiles modules are correctly present alongside their respective *-plot.py script then all modules will be loaded correctly bar one: matplotlib (needed to generate graphs).
To import matplotlib the command 'module load python/2.7.3-matplotlib' is to be typed in.

In the case of the init-plot.py script, this script must be run on the headnode (first 'module load qchem') and must be placed into a folder containing target .xyz files.
Conversely, kev-plot.py must run through a submission script with an alternate build of qchem loaded into it.

water-plot.py is flexible and can be run either through the headnode or through a submission script, although the latter is recommended.

Enjoy!
