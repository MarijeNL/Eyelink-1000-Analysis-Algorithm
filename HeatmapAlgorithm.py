import matplotlib.pyplot as plt
import numpy as np

advanced_users = ['sub_10.asc', 'sub_16.asc']
novice_users = ['sub_11.asc', 'sub_12.asc', 'sub_13.asc', 'sub_14.asc', 'sub_15.asc']

def heatmap(advanced_users, novice_users):
    total_advanced = []
    total_novice = []
    trialIndex_advanced = []
    trialIndex_novice = []
    
    for file in advanced_users:
        for line in open(file):
            if ('!MODE RECORD') in line:        
                total_advanced.append(line.split())
            elif ('EFIX') in line:
                total_advanced.append(line.split())
            elif ('ESACC') in line:
                total_advanced.append(line.split())
  
    for file in novice_users:
        for line in open(file):
            if ('!MODE RECORD') in line:        
                total_novice.append(line.split())
            elif ('EFIX') in line:
                total_novice.append(line.split())
            elif ('ESACC') in line:
                total_novice.append(line.split())

    for element in total_advanced:
        if ('MSG' == element[0]):
            trialIndex_advanced.append(total_advanced.index(element))
            
    for element in total_novice:
        if ('MSG' == element[0]):
            trialIndex_novice.append(total_novice.index(element))

    coordsx_novice = []
    coordsy_novice = []
    coordsx_advanced = []
    coordsy_advanced = []

    for element in total_novice:
        if ('EFIX' in element[0]):
            coordsx_novice.append(element[5])
            #coordsy_novice.append(abs(float(element[6]) - 1460))
            coordsy_novice.append(element[6])
            
    for element in total_advanced:
        if ('EFIX' in element[0]):
            coordsx_advanced.append(element[5])
            coordsy_advanced.append(element[6])

    x_novice = np.array(coordsx_novice)
    y_novice = np.array(coordsy_novice)
    x_advanced = np.array(coordsx_advanced)
    y_advanced = np.array(coordsy_advanced)
    
    plt.hexbin(x_novice.flatten(), y_novice.flatten(), gridsize=150,extent=(0,2560,0,1440))
    plt.title("Heatmap novice participant group")
    plt.xlabel('Width screen')
    plt.ylabel('Height screen')
    plt.xticks([0,500,1000,1500,2000,2560], [0,500,1000,1500,2000,2560])
    plt.yticks([0,200,400,600,800,1000,1200,1460],[0,200,400,600,800,1000,1200,1460])
    plt.gca().invert_yaxis() # Invert the y-axis for correct representation of gaze location
    plt.axis([700,1700,1000,0])
    plt.colorbar()
    plt.savefig('heatmap_novice.png')
    plt.show()
    
    plt.hexbin(x_advanced.flatten(), y_advanced.flatten(), gridsize=150,extent=(0,2560,0,1440))
    
    plt.title("Heatmap advanced participant group")
    plt.xlabel('Width screen')
    plt.ylabel('Height screen')
    plt.xticks([0,500,1000,1500,2000,2560], [0,500,1000,1500,2000,2560])
    plt.yticks([0,200,400,600,800,1000,1200,1460],[0,200,400,600,800,1000,1200,1460])
    plt.gca().invert_yaxis() # Invert the y-axis for correct representation of gaze location
    plt.axis([700,1700,1000,0])
    plt.colorbar()
    plt.savefig('heatmap_advanced.png')
    plt.show()
    
heatmap(advanced_users, novice_users)
