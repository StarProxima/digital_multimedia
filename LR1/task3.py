import cv2

cap = cv2.VideoCapture(r'.\LR1\src\video.mp4', cv2.CAP_ANY)

while True:
    ok, frame = cap.read()

    if not ok: break

    frame = cv2.cvtColor(cv2.resize(frame, (320, 180)), cv2.COLOR_HLS2RGB)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break
