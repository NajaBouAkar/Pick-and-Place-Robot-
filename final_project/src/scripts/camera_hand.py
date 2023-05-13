from cvzone.HandTrackingModule import HandDetector
import cv2
from final_project.msg import hand
import rospy

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)
pub=rospy.Publisher('hand_fingers', hand, queue_size=10)
rospy.init_node('hand_node', anonymous=True)



while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        fingers = detector.fingersUp(hands[0])
        print(fingers)
        
        if fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            finger=hand()
            finger.thumb=True
            finger.firstfinger=False
            finger.secondfinger=False
            finger.thirdfinger=False
            finger.fourthfinger=False
            pub.publish(finger)
        elif fingers[1] == 1 and fingers[0] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            finger=hand()
            finger.thumb=False
            finger.firstfinger=True
            finger.secondfinger=False
            finger.thirdfinger=False
            finger.fourthfinger=False
            pub.publish(finger)
        
        elif fingers[2] == 1 and fingers[0] == 0 and fingers[1] == 0 and fingers[3] == 0 and fingers[4] == 0:
            finger=hand()
            finger.thumb=False
            finger.firstfinger=False
            finger.secondfinger=True
            finger.thirdfinger=False
            finger.fourthfinger=False
            pub.publish(finger)
        
        elif fingers[3] == 1 and fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[4] == 0:
            finger=hand()
            finger.thumb=False
            finger.firstfinger=False
            finger.secondfinger=False
            finger.thirdfinger=True
            finger.fourthfinger=False
            pub.publish(finger)
        
        elif fingers[4] == 1 and fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0:
            finger=hand()
            finger.thumb=False
            finger.firstfinger=False
            finger.secondfinger=False
            finger.thirdfinger=False
            finger.fourthfinger=True
            pub.publish(finger)
        
        elif fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            finger=hand()
            finger.thumb=False
            finger.firstfinger=False
            finger.secondfinger=False
            finger.thirdfinger=False
            finger.fourthfinger=False
            pub.publish(finger)
        elif fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            finger=hand()
            finger.thumb=False
            finger.firstfinger=True
            finger.secondfinger=True
            finger.thirdfinger=False
            finger.fourthfinger=False
            pub.publish(finger)
        elif fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            finger=hand()
            finger.thumb=True
            finger.firstfinger=True
            finger.secondfinger=True
            finger.thirdfinger=True
            finger.fourthfinger=True
            pub.publish(finger)
        elif fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            finger=hand()
            finger.thumb=True
            finger.firstfinger=False
            finger.secondfinger=True
            finger.thirdfinger=True
            finger.fourthfinger=True
            pub.publish(finger)    
        elif fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 1 and fingers[4] == 1:
            finger=hand()
            finger.thumb=True
            finger.firstfinger=True
            finger.secondfinger=False
            finger.thirdfinger=True
            finger.fourthfinger=True
            pub.publish(finger) 
        elif fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
            finger=hand()
            finger.thumb=False
            finger.firstfinger=True
            finger.secondfinger=False
            finger.thirdfinger=False
            finger.fourthfinger=True
            pub.publish(finger) 
    


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('q'):  # break the loop if 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()