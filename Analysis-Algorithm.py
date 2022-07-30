import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Store the name of the video stimuli within videofile define the name of the out (self-chosen name)
videofile = "niveau3_brexit.mp4"
outputname = "output_brexit.mp4"

# Change value of this variable to select other files during the analysis
filename = 'sub_13.asc' 

def handRecognition(videofile, outputname):
    coords = []  
    video = videofile

    cap = cv2.VideoCapture(video) 

    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS) 
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(outputname, fourcc, fps, (int(w),int(h)))

    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
      while cap.isOpened():
        success, image = cap.read()
        if not success:
          print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.
          break

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                coords.append(hand_landmarks)
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
        # Flip the image horizontally for a selfie-view display.
            out.write(image) #added
            cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    out.release()
    cap.release()
    
def showMovements(coords, videofile):
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
    
    plt.title("Movements of the hands in "+str(videofile))
    plt.xlabel("Video duration")
    plt.ylabel("Value of the x coordinate")
    plt.xlim(0,1500)
    plt.ylim(0,1)
    
    plt.plot(frames, mark4, label = "Landmark 4")
    plt.plot(frames, mark8, label = "Landmark 8")
    plt.plot(frames, mark12, label = "Landmark 12")
    plt.plot(frames, mark16, label = "Landmark 16")
    plt.plot(frames, mark20, label = "Landmark 20") 
    
    plt.show()   

def heatmap(filename, movementType):
    total = []
    trialIndex = []

    for line in open(filename):
        if ('!MODE RECORD') in line:        
            total.append(line.split())
        elif ('EFIX') in line:
            total.append(line.split())
        elif ('ESACC') in line:
            total.append(line.split())

    for element in total:
        if ('MSG' == element[0]):
            trialIndex.append(total.index(element))

    # Define the fixations per trial
    trial1 = total[trialIndex[0]:trialIndex[1] - 1]
    trial2 = total[trialIndex[1]:trialIndex[2] - 1]
    trial3 = total[trialIndex[2]:trialIndex[3] - 1]
    trial4 = total[trialIndex[3]:trialIndex[4] - 1]
    trial5 = total[trialIndex[4]:trialIndex[5] - 1]
    trial6 = total[trialIndex[5]:trialIndex[6] - 1]
    trial7 = total[trialIndex[6]:trialIndex[7] - 1]
    trial8 = total[trialIndex[7]:trialIndex[8] - 1]
    trial9 = total[trialIndex[8]:trialIndex[9] - 1]
    trial10 = total[trialIndex[9]:]

    coordsx = []
    coordsy = []

    for element in trial10:
        if ('EFIX' in element[0]):
            coordsx.append(element[5])
            coordsy.append(element[6])

    xtest = np.array(coordsx)
    ytest = np.array(coordsy)

    x = xtest.flatten()
    y = ytest.flatten()

    # Create heatmap
    plt.hexbin(x, y, gridsize=150, extent=(0,2560,0,1440))
    plt.savefig('heatmap.png')
    plt.title("Heatmap "+str(file))
    plt.xlabel('Width screen')
    plt.ylabel('Height screen')
    plt.xticks([0,500,1000,1500,2000,2560], [0,500,1000,1500,2000,2560])
    plt.yticks([0,200,400,600,800,1000,1200,1460],[0,200,400,600,800,1000,1200,1460])
    plt.colorbar()
    plt.show() 
    
handRecognition(videofile, outputname)
showMovements(coords, videofile)
heatmap(filename)
