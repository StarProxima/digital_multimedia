import cv2

img1 = cv2.imread(r'.\LR1\src\img1.jpeg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'.\LR1\src\img2.png',cv2.IMREAD_REDUCED_COLOR_8)
img3 = cv2.imread(r'.\LR1\src\img3.webp',cv2.IMREAD_ANYDEPTH)
cv2.namedWindow('img1', cv2.WINDOW_FREERATIO)
cv2.namedWindow('img2', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow('img3', cv2.WINDOW_NORMAL)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

