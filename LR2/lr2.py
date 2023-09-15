import cv2
import numpy as np


def lab2():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        lower_red = np.array([50, 50, 150])
        upper_red = np.array([200, 200, 255])
        mask = cv2.inRange(hsv, lower_red, upper_red)

        kernel = np.ones((5, 5), np.uint8)

        image_opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        image_closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

     
        moments = cv2.moments(mask)
        s = moments['m00']

        if s > 0:
            width = height = int(np.sqrt(s))
            c_x = int(moments["m10"] / moments["m00"])
            c_y = int(moments["m01"] / moments["m00"])

            cv2.rectangle(
                frame,
                (c_x - (width // 16), c_y - (height // 16)),
                (c_x + (width // 16), c_y + (height // 16)),
                (0, 0, 0),
                2
            )

    
        cv2.imshow('tracking', frame)
        cv2.imshow('open', image_opening)
        cv2.imshow('close', image_closing)


        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def erode(image, kernel):
    m, n = image.shape
    km, kn = kernel.shape
    hkm = km // 2
    hkn = kn // 2
    eroded = np.copy(image)

    for i in range(hkm, m - hkm):
        for j in range(hkn, n - hkn):
            eroded[i, j] = np.min(image[i - hkm:i + hkm + 1, j - hkn:j + hkn + 1][kernel == 1])

    return eroded

def dilate(image, kernel):
    m, n = image.shape
    km, kn = kernel.shape
    hkm = km // 2
    hkn = kn // 2
    dilated = np.copy(image)

    for i in range(hkm, m - hkm):
        for j in range(hkn, n - hkn):
            dilated[i, j] = np.max(image[i - hkm:i + hkm + 1, j - hkn:j + hkn + 1][kernel == 1])

    return dilated

lab2()