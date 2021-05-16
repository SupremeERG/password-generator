import cv2, pynput
from time import sleep
"""
cap = cv2.VideoCapture(1)
frames = 0
while True:
    frames += 1
    print(f"\r{frames} frames", end="")
    if frames == 1000:
        print("\nReached 1000 frames, quitting now")
        sleep(8)
        cap.release()
        cv2.destroyAllWindows() 
    ret,img=cap.read()
    cv2.imshow('target_webcam', img)
    k=cv2.waitKey(2)
    if k == 27:
        print(" not making sense")
        break
cap.realease()
cv2.destroyAllWindows()
"""
cams_test = 10
for i in range(0, cams_test):
    cap = cv2.VideoCapture(i)
    test, frame = cap.read()
    print("i : "+str(i)+" /// result: "+str(test))
input("\n\nwait")
#"""