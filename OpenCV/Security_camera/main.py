import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()                                           #ret = retrive
    ret, frame2 = cam.read()                                           #ret = retrive
    diff = cv2.absdiff(frame1, frame2)                                 #difference bitween two frames
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)                      #gray scale conversion
    blur = cv2.GaussianBlur(gray, (5, 5), 0)                           #bluring the gray scale
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)        #thresh hold value for sharpenning,reduce noises
    dilated = cv2.dilate(thresh, None, iterations=3)                   #make it big
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  #boundary of th moving object
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c)<5000:                                    #neglect small movement things
            continue
        x, y, w, h =cv2.boundingRect(c)                                #w=width, h= height
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.PlaySound('intruder_alert.wav', winsound.SND_ASYNC)   #make noise when a big moving object found
    if cv2.waitKey(10) == ord('q'):     #q = quit
        break
    cv2.imshow('Ronok_Cam', frame1)
