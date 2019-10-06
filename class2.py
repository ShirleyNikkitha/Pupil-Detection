import numpy as np
import cv2
import urllib
import time
import urllib.request
import webbrowser

# webbrowser.open('https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
camera=cv2.VideoCapture(0)
numerator=0
denominator=0
while True:
    ret, frame = camera.read()
    roi=frame
    frame=cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
        # cv2.line(frame,(x+w/2,y),(x+w/2,y+h/2),(255,0,0),1)
        # cv2.line(frame,(int(x+w/4.2),int(y+h/2.2)),(int(x+w/2.5),int(y+h/2.2)),(0,255,0),1)
        # cv2.line(frame,(int(x+w/4.2),y+h/3),(int(x+w/2.5),y+h/3),(0,255,0),1)
        # cv2.line(frame,(int(x+w/4.2),y+h/3),(int(x+w/4.2),int(y+h/2.2)),(0,255,0),1)
        # cv2.line(frame,(int(x+w/2.5),y+h/3),(int(x+w/2.5),int(y+h/2.2)),(0,255,0),1)


        d=10920.0/float(w)


        x1=int(x+w/4.2)+1
        x2=int(x+w/2.5)
        y1=int(y+h/3)+1
        y2=int(y+h/2.2)
        roi=frame[y1:y2,x1:x2]
        gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        equ = cv2.equalizeHist(gray)
        thres=cv2.inRange(equ,0,20)
        kernel = np.ones((3,3),np.uint8)

        dilation = cv2.dilate(thres,kernel,iterations = 2)

        erosion = cv2.erode(dilation,kernel,iterations = 3)


        image, contours, hierarchy = cv2.findContours(erosion,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

        if len(contours)==2 :
            numerator+=1
            # img = cv2.drawContours(roi, contours, 1, (0,255,0), 3)

            M = cv2.moments(contours[1])
            #print M['m00']
            #print M['m10']
            #print M['m01']
            if M['m00']!=0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                cv2.line(roi,(cx,cy),(cx,cy),(0,255,255),3)
                cv2.line(roi, (cx, cy), (cx, cy), (0, 255, 255), 3)
            #print cx,cy

        elif len(contours)==1:
            numerator+=1
            # img = cv2.drawContours(roi, contours, 0, (0,255,0), 3)

            #------- finding centroid of the countor ----#
            M = cv2.moments(contours[0])
            if M['m00']!=0:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                print (cx,cy)
                print(cx)
                cv2.line(roi,(cx,cy),(cx,cy),(0,0,255),3)
                cv2.line(roi, (cx, cy), (cx, cy), (0, 0, 255), 3)

                if cx > 30:
                    # print(cx)
                    # print("looking right")
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                    cv2.putText(frame, 'right', (500, 250),
                                font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
                    webbrowser.open('https://www.youtube.com/')

                # if cx== 43:
                    # webbrowser.open('https://www.tutorialspoint.com/python/python_interview_questions.htm')
                    # camera.release()
                    # print("accurracy=", (float(numerator) / float(numerator + denominator)) * 100)
                    # cv2.destroyAllWindows()

                    # break
                if cx < 10:

                    print("looking left")
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)
                    cv2.putText(frame, 'left', (100, 250),
                                font, 0.8, (0, 255, 255), 1, cv2.LINE_AA)
                if cx ==2:
                     webbrowser.open('https://www.google.com/')
                     camera.release()
                     print("accurracy=", (float(numerator) / float(numerator + denominator)) * 100)
                     cv2.destroyAllWindows()

                     break
                if cy > 20:
                       # print("looking bottop")
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 1)
                       cv2.putText(frame, 'sleep', (210, 450),
                                font, 0.8, (255, 255, 0), 1, cv2.LINE_AA)
                # if cy == 24:
                #      webbrowser.open('https://www.youtube.com/watch?v=41qgdwd3zAg&list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
                #      camera.release()
                #      print("accurracy=", (float(numerator) / float(numerator + denominator)) * 100)
                #      cv2.destroyAllWindows()
                #
                #      break

                if cy < 3:
                     print("looking top")
                     font = cv2.FONT_HERSHEY_SIMPLEX
                     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                     cv2.putText(frame, 'up', (300, 50),
                             font, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
                # if cy == 1:
                #      webbrowser.open('https://www.w3schools.com/python/')
                #      camera.release()
                #      print("accurracy=", (float(numerator) / float(numerator + denominator)) * 100)
                #      cv2.destroyAllWindows()
                #
                #      break


        else:
            denominator+=1
            #print "iris not detected"
        ran=x2-x1
        mid=ran/2



    cv2.imshow("frame",frame)
    # cv2.imshow("eye",frame)
    if cv2.waitKey(30)==27 & 0xff:
        break
camera.release()
print("accurracy=",(float(numerator)/float(numerator+denominator))*100)
cv2.destroyAllWindows()
