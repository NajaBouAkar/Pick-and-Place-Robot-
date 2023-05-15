#Import necessary modules
from cvzone.HandTrackingModule import HandDetector
import cv2
from final_project.msg import hand
import rospy
#Open the default camera
cap = cv2.VideoCapture(0)
#Create a hand detector with a maximum of one hand and a detection confidence of 0.7
detector = HandDetector(maxHands=1, detectionCon=0.7)
#Create a publisher to publish messages of type 'hand' on the 'hand_fingers' topic
pub=rospy.Publisher('hand_fingers', hand, queue_size=10)
#Initialize the Ros node with the name 'hand_node'
rospy.init_node('hand_node', anonymous=True)


#Continously read frames from the camera and process them 
while True:
    #Read a frame from the camera
    success, img = cap.read()
    #Find hands in the image using the hand detector
    hands, img = detector.findHands(img)
    #If at least one hand is detected
    if hands:
        #Determine which fingers are up on the detected hand
        fingers = detector.fingersUp(hands[0])
        print(fingers)
        #Publish a message with the finger state corresponding to the hand posture
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
    

    #Display the final image on a window with the title "Image"
    cv2.imshow("Image", img)
    #Wait for a key press event for 1 millisecond and store the pressed key value in'key' variable 
    key = cv2.waitKey(1)
    #if the key pressed is 'q' break out from the while loop
    if key == ord('q'):  
        break
#Release the video capture object
cap.release()
#Close all the windows opened by opencv
cv2.destroyAllWindows()