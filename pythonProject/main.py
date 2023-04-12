import cv2
import numpy as np
image = cv2. imread ("wizzy.jpg ")

gray = cv2.cvtcolor (image, cv2.COLOR_BRG2GRAY)
gray= cv2. medianBlur(gray,5)
edges =cv2.adaptiveThrshold(gray,255,
                            cv2.ADAPTIVE_TRHESH_MEAN_C,
                            cv2.Thresh_BINARY,9,9)
color= cv2.bilateralFilter(image,9,250,250)
cartoon=cv2. bitwise_and(color,mask=edges)
cv2.imshow("image",image)
cv2.imshow("edges", edges)
cv2.imshow("Cartoon",cartoon)
cv2.waitkey(0)
cv2.destroyAllwindows()
