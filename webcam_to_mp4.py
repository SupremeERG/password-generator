import cv2
from datetime import date, datetime
import time
frames = 0
try:
    # Specify resolution
    resolution = (640, 480)
    
    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")
    
    # Specify name of Output file
    today = date.today()
    current_time = datetime.now().strftime("%H_%M")
    filename = f"{today}@{current_time}.avi"
    fps = 30.0
    
    
    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    img = cv2.VideoCapture(1)
    startTime = time.time()
    while True:
        if frames == 1000:
            break
        ret,frame = img.read()
        #cv2.imshow("webcam_viewer", frame)
        # Write it to the output file
        out.write(frame)
        frames += 1
        print(frames)
    sleep(1000)
    out.release()
    cv2.destroyAllWindows()
except Exception as e:
    print(e)
    input("just wait")