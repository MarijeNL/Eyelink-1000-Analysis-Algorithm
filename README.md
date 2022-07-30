# Eyelink-1000-Fixation-Analysis
Self-written algorithm to show to differences in viewing behavior between groups of participants or individual participants. EDF from the Eyelink 1000 need to be used. The algorithm is written in Python and can be used with Jupyter Notebook. Please note that before the algorithm can be used, all of the EDF files needs to be changed to ASC files.

---------------
## Change EDF to ASC files
Before you can use this algorithm, all of the EDF files needs to be changed to ASC files. Otherwise the results from the experiment cannot be read. This file conversion can be done with the help of the SR Research Developer Kit (https://www.sr-support.com/thread-13.html) and the Commandprompt on your computer or laptop. Make sure that the right directory is selected within the Commandprompt and use "edf2asc <filename>.edf" to convert the file to ASC.
