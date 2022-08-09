import numpy as np

screen_width = 2560
screen_height = 1460

videofiles = ['Introductie.mp4', 'niveau1_cakebakken.mp4', 'niveau1_dierentuin.mp4', 'niveau1_mijnfamilie.mp4', 'niveau2_brandmelding.mp4', 'niveau2_opheffeest.mp4','niveau2_weerbericht.mp4','niveau3_ambassades.mp4','niveau3_brexit.mp4','niveau3_socialmedia.mp4']
#videofiles = ['niveau1_cakebakken.mp4']

advanced_users = ['sub_10.asc', 'sub_16.asc']
novice_users = ['sub_11.asc', 'sub_12.asc', 'sub_13.asc', 'sub_14.asc', 'sub_15.asc']

def fixationAlgorithm(files):
    total = []
    trialIndex = []
    
    for file in files:
        for line in open(file):
            if ('!MODE RECORD') in line:        
                total.append(line.split())
            elif ('EFIX') in line:
                total.append(line.split())
            elif ('ESACC') in line:
                total.append(line.split())
    
    for element in total:
        if ('MSG' == element[0]):
            trialIndex.append(total.index(element))
            
    coords = []

    for element in total:
        if ('EFIX' in element[0]):
            coords.append((element[5],element[6]))
            
    return coords

def videofileAnalysis(videofiles):
    handcoords = []
    for file in videofiles:
        subcoords = handRecognition(file, "output.mp4")
        
        for coord in subcoords:
            coordlandmark = coord.landmark
            handcoords.append((coordlandmark[9].x, coordlandmark[9].y))
    
    return handcoords

def distance(coordinate1, coordinate2):
    return pow(pow(float(coordinate1[0]) - float(coordinate2[0]), 2) + pow(float(coordinate1[1]) - float(coordinate2[1]), 2), .5)

def smallestDistance(coordinate, coordinatelist):
    distances = []
    
    for item in coordinatelist:
        distances += [distance(coordinate, item)]
    
    #for item in range(len(coordinatelist)-1):
    #    for j in range(item+1, len(coordinatelist)):
    #        distances += [distance(coordinatelist[item],coordinatelist[j])]
    return min(distances)

def classifierAlgorithm(videofiles, fixations_advanced, fixations_novice): 
    classifierAdvanced = []
    classifierNovice = []
    
    handcoordinates = videofileAnalysis(videofiles)
    handcoordinates = np.array(handcoordinates)
    
    print("Advanced:")
    print("--------------")
    
    for fixation in fixations_advanced:
        smallest = smallestDistance(fixation, handcoordinates)
        
        fixation_convert = float(fixation[1]) / screen_height
        
        if (smallest < 500):
            classifierAdvanced.append("Hands")
        elif (fixation_convert < 0.2):
            classifierAdvanced.append("Eyes")
        elif ((fixation_convert > 0.2) & (fixation_convert < 0.3)):
            classifierAdvanced.append("Mouth")
        else:
            classifierAdvanced.append("Nothing")
    
    print("Eyes:", classifierAdvanced.count("Eyes"))
    print("Mouth:", classifierAdvanced.count("Mouth"))
    print("Hands:", classifierAdvanced.count("Hands"))
    print("Nothing:", classifierAdvanced.count("Nothing"))
    
    print("")
    print("Novice:")
    print("--------------")
    
    for fixation in fixations_novice:
        smallest = smallestDistance(fixation, handcoordinates)
        
        fixation_convert = float(fixation[1]) / screen_height
        
        if (smallest < 500):
            classifierNovice.append("Hands")
        elif (fixation_convert < 0.2):
            classifierNovice.append("Eyes")
        elif ((fixation_convert > 0.2) & (fixation_convert < 0.3)):
            classifierNovice.append("Mouth")
        else:
            classifierNovice.append("Nothing")
            
    print("Eyes:", classifierNovice.count("Eyes"))
    print("Mouth:", classifierNovice.count("Mouth"))
    print("Hands:", classifierNovice.count("Hands"))
    print("Nothing:", classifierNovice.count("Nothing"))
    
fixations_advanced = fixationAlgorithm(advanced_users)
fixations_novice = fixationAlgorithm(novice_users)
    
classifierAlgorithm(videofiles, fixations_advanced, fixations_novice)
