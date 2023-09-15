import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ok, frame = cap.read()
    if not ok: break
        
    cv2.imshow("camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
