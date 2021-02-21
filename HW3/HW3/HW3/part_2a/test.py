import cv2
image=cv2.imread("Mario_big.png",0)
imC = cv2.applyColorMap(image, cv2.COLORMAP_AUTUMN)
cv2.imshow("ColourMap",imC)

cv2.waitKey(0)