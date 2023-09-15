import cv2

img1 = cv2.imread(r'.\LR1\src\img3.webp')


cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.namedWindow('img_hsv', cv2.WINDOW_NORMAL)

cv2.imshow('img', img1)

hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow('img_hsv', hsv)


cv2.waitKey(0)
cv2.destroyAllWindows()

