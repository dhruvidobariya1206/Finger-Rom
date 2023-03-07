print("in hcd")


import mediapipe as mp
import cv2
import numpy as np
import os.path
import db_conn
import sys

# import uuid
# import os
# import face_recognition
# from datetime import datetime
# import HandTrackingModule as htm

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


user = sys.argv[1]
print(user)


# from matplotlib import pyplot as plt

'''
'''

hnd = mp_hands.HandLandmark


joint_list = [
                [hnd.INDEX_FINGER_TIP,hnd.INDEX_FINGER_DIP,hnd.INDEX_FINGER_PIP,hnd.INDEX_FINGER_MCP,hnd.WRIST],
                [hnd.MIDDLE_FINGER_TIP,hnd.MIDDLE_FINGER_DIP,hnd.MIDDLE_FINGER_PIP,hnd.MIDDLE_FINGER_MCP,hnd.WRIST] ,
                [hnd.RING_FINGER_TIP,hnd.RING_FINGER_DIP,hnd.RING_FINGER_PIP,hnd.RING_FINGER_MCP,hnd.WRIST],
                [hnd.PINKY_TIP,hnd.PINKY_DIP,hnd.PINKY_PIP,hnd.PINKY_MCP,hnd.WRIST],
                [hnd.THUMB_TIP,hnd.THUMB_IP,hnd.THUMB_MCP,hnd.THUMB_CMC]
              ]
index_angles = {"INDEX_FINGER_TIP" : 0,"INDEX_FINGER_PIP" : 0,"INDEX_FINGER_MCP":0}
middle_angles = {"MIDDLE_FINGER_TIP":0,"MIDDLE_FINGER_PIP":0,"MIDDLE_FINGER_MCP":0}
ring_angles = {"RING_FINGER_TIP":0,"RING_FINGER_PIP":0,"RING_FINGER_MCP":0}
pinky_angles = {"PINKY_TIP":0,"PINKY_PIP":0,"PINKY_MCP":0}
thumb_angles = {"THUMB_TIP":0,"THUMB_IP":0,"THUMB_MCP":0}

def draw_finger_angles(image, results, joint_list):
    
    # Loop through hands
    for hand in results.multi_hand_landmarks:
        #Loop through joint sets 
        k=0
        for joint in joint_list:
            # print(k)
            try:
                a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y]) # First coord
                b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y]) # Second coord
                c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y]) # Third coord
                radians = np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
                angle = np.abs(radians*180.0/np.pi)
                angle = 180-angle
                if angle < 0.0:
                    angle = -1*angle
                # cv2.putText(image, str(round(angle, 2)), tuple(np.multiply(b, [640, 480]).astype(int)),
                #        cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2, cv2.LINE_AA)
            except:
                pass
            try:
                d = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y]) # First coord
                e = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y]) # Second coord
                f = np.array([hand.landmark[joint[3]].x, hand.landmark[joint[3]].y]) # Third coord
                radians2 = np.arctan2(f[1] - e[1], f[0]-e[0]) - np.arctan2(d[1]-e[1], d[0]-e[0])
                angle2 = np.abs(radians2*180.0/np.pi)
                angle2 = 180-angle2
                if angle2 < 0.0:
                    angle2 = -1*angle2
                # cv2.putText(image, str(round(angle2, 2)), tuple(np.multiply(e, [640, 480]).astype(int)),
                #        cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0), 2, cv2.LINE_AA)
            except:
                pass
            try:
                g = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y]) # First coord
                h = np.array([hand.landmark[joint[3]].x, hand.landmark[joint[3]].y]) # Second coord
                i = np.array([hand.landmark[joint[4]].x, hand.landmark[joint[4]].y]) # Third coord
                radians3 = np.arctan2(i[1] - h[1], i[0]-h[0]) - np.arctan2(g[1]-h[1], g[0]-h[0])
                angle3 = np.abs(radians3*180.0/np.pi)
                angle3 = 180-angle3
                if angle3 < 0.0:
                    angle3 = -1*angle3
                # cv2.putText(image, str(round(angle3, 2)), tuple(np.multiply(h, [640, 480]).astype(int)),
                #        cv2.FONT_HERSHEY_SIMPLEX,0.7, (255, 255, 0), 2, cv2.LINE_AA)
            except:
                # print("hello")
                pass
            if k == 0:
                # print("yes")
                index_angles["INDEX_FINGER_TIP"] = angle
                index_angles["INDEX_FINGER_PIP"] = angle2
                index_angles["INDEX_FINGER_MCP"] = angle3
                
            elif k== 1:
                middle_angles["MIDDLE_FINGER_TIP"] = angle
                middle_angles["MIDDLE_FINGER_PIP"] = angle2
                middle_angles["MIDDLE_FINGER_MCP"] = angle3
            elif k== 2:
                ring_angles["RING_FINGER_TIP"] = angle
                ring_angles["RING_FINGER_PIP"] = angle2
                ring_angles["RING_FINGER_MCP"] = angle3
            elif k== 3:
                pinky_angles["PINKY_TIP"] = angle
                pinky_angles["PINKY_PIP"] = angle2
                pinky_angles["PINKY_MCP"] = angle3
            elif k== 4:
                thumb_angles["THUMB_IP"] = angle
                thumb_angles["THUMB_TIP"] = angle2
                
            k+=1
            
            # markAttendanceangle(angle)
    return image

cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()
        
        # BGR 2 RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Flip on horizontal
        image = cv2.flip(image, 1)
        
        # Set flag
        image.flags.writeable = False
        
        # Detections
        results = hands.process(image)
        
        # Set flag to true
        image.flags.writeable = True
        
        # RGB 2 BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Detections
#         print(results)
        
        # Rendering results
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
                
            draw_finger_angles(image, results, joint_list)
           
            
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            # print(index_angles)
            index_angles["INDEX_FINGER_PIP"]=round(index_angles["INDEX_FINGER_PIP"],1)
            middle_angles["MIDDLE_FINGER_PIP"]=round(middle_angles["MIDDLE_FINGER_PIP"],1)
            ring_angles["RING_FINGER_PIP"]=round(ring_angles["RING_FINGER_PIP"],1)
            pinky_angles["PINKY_PIP"]=round(pinky_angles["PINKY_PIP"],1)
            thumb_angles["THUMB_IP"]=round(thumb_angles["THUMB_IP"],1)
            query_pip = f"insert into angle_pip(P_id,ind,mid,ring,little,thumb) values('{user}','{str(index_angles['INDEX_FINGER_PIP'])}','{str(middle_angles['MIDDLE_FINGER_PIP'])}','{str(ring_angles['RING_FINGER_PIP'])}','{str(pinky_angles['PINKY_PIP'])}','{str(thumb_angles['THUMB_IP'])}'"
            # print(query_pip)
            db_conn.mycursor.execute(query_pip) 

            index_angles["INDEX_FINGER_TIP"]=round(index_angles["INDEX_FINGER_TIP"],1)
            middle_angles["MIDDLE_FINGER_TIP"]=round(middle_angles["MIDDLE_FINGER_TIP"],1)
            ring_angles["RING_FINGER_TIP"]=round(ring_angles["RING_FINGER_TIP"],1)
            pinky_angles["PINKY_TIP"]=round(pinky_angles["PINKY_TIP"],1)
            thumb_angles["THUMB_TIP"]=round(thumb_angles["THUMB_TIP"],1)
            query_Tip = f"insert into angle_tip(P_id,ind,mid,ring,little,thumb) values('{user}','{str(index_angles['INDEX_FINGER_TIP'])}','{str(middle_angles['MIDDLE_FINGER_TIP'])}','{str(ring_angles['RING_FINGER_TIP'])}','{str(pinky_angles['PINKY_TIP'])}','{str(thumb_angles['THUMB_TIP'])}')"
            # print(query_Tip)
            db_conn.mycursor.execute(query_Tip)
            
            index_angles["INDEX_FINGER_MCP"]=round(index_angles["INDEX_FINGER_MCP"],1)
            middle_angles["MIDDLE_FINGER_MCP"]=round(middle_angles["MIDDLE_FINGER_MCP"],1)
            ring_angles["RING_FINGER_MCP"]=round(ring_angles["RING_FINGER_MCP"],1)
            pinky_angles["PINKY_MCP"]=round(pinky_angles["PINKY_MCP"],1)
            thumb_angles["THUMB_MCP"]=round(thumb_angles["THUMB_MCP"],1)
            query_MCP = f"insert into angle_mcp(P_id,ind,mid,ring,little,thumb) values('{user}','{str(index_angles['INDEX_FINGER_MCP'])}','{str(middle_angles['MIDDLE_FINGER_MCP'])}','{str(ring_angles['RING_FINGER_MCP'])}','{str(pinky_angles['PINKY_MCP'])}','{str(thumb_angles['THUMB_MCP'])}')"
            # print(query_MCP)
            db_conn.mycursor.execute(query_MCP)
            
            break

cap.release()
cv2.destroyAllWindows()

