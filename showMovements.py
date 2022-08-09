import matplotlib.pyplot as plt
import numpy as np

def showMovements(coords, videofile):
  # Marks are the tips of each finger
    mark4 = []
    mark8 = []
    mark12 = []
    mark16 = []
    mark20 = []

    frames = list(range(1,len(coords)+1))

    for coord in coords:
        coord = coord.landmark
        mark4.append(coord[4].x)
        mark8.append(coord[8].x)
        mark12.append(coord[12].x)
        mark16.append(coord[16].x)
        mark20.append(coord[20].x)

    plt.plot(frames, mark4, label = "Landmark 4")
    plt.plot(frames, mark8, label = "Landmark 8")
    plt.plot(frames, mark12, label = "Landmark 12")
    plt.plot(frames, mark16, label = "Landmark 16")
    plt.plot(frames, mark20, label = "Landmark 20")
    
    plt.xlim(0,1500)
    plt.ylim(0,1)

    plt.title("Movements of the hands in "+str(videofile))

    plt.xlabel("Video duration")
    plt.ylabel("Value of the x coordinate")

    # Hide legend
    #plt.legend(loc=(1.05,0.5))

    plt.show()
    
showMovements(coords, videofile)
