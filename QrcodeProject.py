import cv2
import numpy as np
from pyzbar.pyzbar import decode
import os
# need zbar tools for ubuntu: sudo apt-get install -y zbar-tools

# img = cv2.imread('images/1.png') # reading the image
cap = cv2.VideoCapture(0) # select camera
cap.set(3,640) # set width id and width
cap.set(4,480) # height id and height

with open('myDataFile.txt') as f:
    myDataList = f.read().splitlines() # read all the data and add one item to the list

counter_a = 0
counter_u = 0

while True:
    success, img = cap.read() # get image
    for barcode in decode(img): # find barcode using decode function
        myData = barcode.data.decode('utf-8') # decoding the data to get the output as string
        #print(myData) #printing out the data

        if myData in myDataList:
            myOutput = "Authorized"
            myColor = (0,255,0)
            counter_a+=1
            if counter_a < 2:
            	os.system("spd-say UserAuthorized")
            	
        else:
            myOutput = "Un-Authorized"
            myColor = (0,0,255)
            counter_u+=1
            if counter_u < 2:
            	os.system("spd-say UserUnAuthorized")
            	



        # draw polygon box aroung qrcode
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,myColor,5) # image, points, closed = True, color, Thickness

        # if we have an angle on our image the text will rotate, we want a text that stay constant
        # so we can use the top point of the rectangle
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,myColor,2) # points, font,scale, color,thickness



    cv2.imshow('Result',img) # title and image
    cv2.waitKey(1) # wait for 1 millisecond

    if cv2.waitKey(10) == ord('q'):
        break

cap.release() # Release the screen
cv2.destroyAllWindows() # destroy all screens


#https://www.youtube.com/watch?v=SrZuwM705yE