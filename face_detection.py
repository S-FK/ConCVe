import cv2
import time
import os
while (1):
    cap = cv2.VideoCapture(0)
    cap.set(3,640) #width=640
    cap.set(4,480) #height=480
    ret, frame = cap.read()
    if ret == True:

# Display the resulting frame
        cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    if cap.isOpened():
        _,frame = cap.read()
        cap.release() #releasing camera immediately after capturing picture
        if _ and frame is not None:
            cv2.imwrite('img.jpg', frame)
            cv2.destroyAllWindows()
    cap.release()
    os.remove("output.txt")
    temp = os.system("python tan.py img.jpg >> output.txt")
    print(temp)
    file = open("output.txt" , "r" )
    file_content = file.read()
    tofind1 = "man"
    tofind2 = "woman"

    if tofind1 in str(file_content) and tofind2 in str(file_content):
        result = open('result.txt' , "w+")
        result.write("Danger")

  
