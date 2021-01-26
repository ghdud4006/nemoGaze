"""
library for demonstration
"""
"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import dlib
import datetime as pydatetime
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
face_detector = dlib.get_frontal_face_detector()
# get a new frame
while True:
    # We get a new frame from the webcam

    _, frame = webcam.read()

    #print("in")
    
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_start_time = pydatetime.datetime.now().timestamp()
    face_end_time = 0.1;
    gaze_start_time = 0.1;
    gaze_end_time = 0.1;
    face_detection_time = ""

    faces = face_detector(frame2)

    right_cnt=0
    left_cnt=0
    center_cnt=0
    text=""
    focusing=0

    if faces:
        face_end_time = pydatetime.datetime.now().timestamp()
        face_detection_time = str(face_end_time - face_start_time)
        
        gaze_start_time = pydatetime.datetime.now().timestamp()
        for face in faces:

            #if face:
                #print("face found")
    
            gaze.refresh(frame, face)

            frame = gaze.annotated_frame()

            #for each people
            if gaze.is_blinking():
               text = "Blinking"
            elif gaze.is_right():
               text = "Looking right"
               right_cnt+=1
            elif gaze.is_left():
               text = "Looking left"
               left_cnt+=1
            elif gaze.is_center():
               text = "Looking center"
               center_cnt+=1
            elif gaze.is_up():
               text = "Looking up"
            elif gaze.is_down():
               text = "Looking down"

            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()

        focusing=0

        # if(text=="Blinking"):
        #     text="Blinking"
        if(right_cnt>left_cnt and right_cnt>center_cnt):
            cv2.rectangle(frame, (0, 0),  (640, 1080), (0, 0, 255), 3)
            text = "Looking right"
            focusing=right_cnt
        elif(left_cnt>right_cnt and left_cnt>center_cnt):
            cv2.rectangle(frame, (640, 0),  (1280, 1080), (0, 0, 255), 3)
            #cv2.rectangle(frame, (1280, 0),  (1920, 1080), (0, 0, 255), 3)
            text = "Looking left"
            focusing=left_cnt
        elif(center_cnt>right_cnt and center_cnt>left_cnt):
            #cv2.rectangle(frame, (640, 0),  (1280, 1080), (0, 0, 255), 3)
            text = "Looking center"
            focusing=center_cnt
        else:
            text = "None"


    else:
        gaze.refresh(frame,None)
        frame = gaze.annotated_frame()


    cv2.putText(frame, "Current people: " + str(focusing), (90, 200), cv2.FONT_HERSHEY_DUPLEX, 1.6, (255, 255, 255), 2)
    cv2.putText(frame, text, (500, 600), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 0, 240), 2)
    cv2.imshow("NemoGaze", frame)
    
    gaze_end_time = pydatetime.datetime.now().timestamp()
    gaze_detection_time = str(gaze_end_time - gaze_start_time)

    if cv2.waitKey(1) == 27:
        break
