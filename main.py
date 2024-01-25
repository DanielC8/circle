#import cv and np
import cv2
import numpy as np
#Gets image
img = cv2.imread("can.jpg")
#Turns into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Gaussian Blur
gray = cv2.GaussianBlur(gray,(15,15),0)
# gets all the edges
maskedimg = cv2.Canny(gray, 20, 150)
#hough circles
circles = cv2.HoughCircles(maskedimg, cv2.HOUGH_GRADIENT, 1.5, 999, param1=120, param2=70, minRadius=0, maxRadius=0)
#loops through the circles
if circles is not None:
    circlelist = np.uint16(np.around(circles))
    #generates a circle and center dot for each circle
    for circle in circlelist[0, :]:
        x = circle[0]
        y = circle[1]
        radius = circle[2]
        #draws the circle
        cv2.circle(img, (x, y), radius, (50, 255, 20), 15)

        #draw a dot at the center
        cv2.circle(img, (x, y), 1, (50, 255, 20), 10)


#shows new image
cv2.imshow("hi",img)
cv2.imwrite("img_4.png",img)
cv2.waitKey(0)