import cv2
import numpy as np

from pyzbar.pyzbar import decode

# img = cv2.imread('images/1.png') # reading the image

cap = cv2.VideoCapture(0) # select camera
cap.set(3,640) # set width id and width
cap.set(4,480) # height id and height

while True:
    success, img = cap.read() # get image
    for barcode in decode(img): # find barcode using decode function
        myData = barcode.data.decode('utf-8') # decoding the data to get the output as string
        print(myData) #printing out the data

        # draw polygon box aroung qrcode
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,(255,0,255),5) # image, points, closed = True, color, Thickness

        # if we have an angle on our image the text will rotate, we want a text that stay constant
        # so we can use the top point of the rectangle
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,255),2) # points, font,scale, color,thickness



    cv2.imshow('Result',img) # title and image
    cv2.waitKey(1) # wait for 1 millisecond
