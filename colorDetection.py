import imutils #resize
import cv2

redLower=(95,49,100)  #change (hue,saturation,brightness) for different color detection
redUpper=(154,255,255)

camera=cv2.VideoCapture(0)

while True:
    (grabbed,frame)=camera.read()

    frame=imutils.resize(frame,width=1000)  #resizing

    blurred=cv2.GaussianBlur(frame,(11,11),0) #smoothening

    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,redLower,redUpper) #Mask the Blue color
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)

    contour=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)[-2]   #contour value identification
    center=None


    if len(contour)>0:
        c=max(contour,key=cv2.contourArea)
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"])) #formula for creating center point on contours

        if radius>10:
            cv2.circle(frame,(int(x),int(y)),int(radius),
                              (0,255,255),2)
            cv2.circle(frame,center,5,(0,0,255),-1)

            if radius>250:
                print("stop")
            else:
                if (center[0]<150):
                    print("Right")
                elif(center[0]>450):
                    print("Left")
                elif(radius<250):
                    print("front")
                else:
                    print("Stop")
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        print("Thank YOU")
        break

camera.release()
cv2.destroyAllWindows()






                    
    
