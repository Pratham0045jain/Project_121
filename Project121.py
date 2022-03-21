import cv2
import time
import numpy as np

""" fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,500))
 """
cam = cv2.VideoCapture(0) 
# 0 stands for the default camera of system

time.sleep(2)
bg = cv2.imread("E:/Python/Class97/download (4).jpg")


while True:
    ret, frame = cam.read()

    # cvtColor change the color from rgb to hsv
    frame = cv2.resize(frame, (640, 480))
    bg = cv2.resize(bg, (640, 480))

    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])
       
    mask = cv2.inRange(frame, l_black, u_black )
    result = cv2.bitwise_and(frame, frame, mask = mask)

    print(result)
    f = frame - result
    print(f)
    f = np.where(f == 0, bg, f)

    cv2.imshow("magic cloak", frame)
    cv2.imshow("background", f)

    if cv2.waitKey(1) & 0xFF == ord("q") :
        break

cam.release()
cv2.destroyAllWindows()