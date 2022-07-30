# Eyelink 1000 Analysis Algorithm
Self-written algorithm to show to differences in viewing behavior between groups of participants or individual participants during different video stimuli. EDF from the Eyelink 1000 need to be used. The algorithm is written in Python and can be used with Jupyter Notebook. Please note that before the algorithm can be used, all of the EDF files needs to be changed to ASC files.

---------------
## Change EDF files to ASC files
Before you can use this algorithm, all of the EDF files needs to be changed to ASC files. Otherwise the results from the experiment cannot be read. This file conversion can be done with the help of the SR Research Developer Kit (https://www.sr-support.com/thread-13.html) and the Commandprompt on your computer or laptop. Make sure that the right directory is selected within the Commandprompt and use "edf2asc <filename>.edf" to convert the file to ASC.

## Algorithm
The aim of the algorithm is to point out the viewing behavior of certain participants or a group of participants. By comparing the viewing behavior, the differences between participants or groups can be showed. It is important to note that some parts of the algorithm depend on one another and if not all of the functions are used, the algorithm can show undesired behavior. The different components of the algorithm are listed down below:
  - handRecognition: recognizes the hands within the video stimuli to define the locations of the hands
  - showMovements: function to show the amount of movements within the video stimuli (can be used to show the difficulty of certain video stimuli)
  - heatmap: function to create a heatmap with the corresponding data
  - classifier: function to classify the fixations of the participant
