import cv2

def copyVideo():
    video = cv2.VideoCapture(r'.\LR1\src\video.mp4', cv2.CAP_ANY)
    ok, vid = video.read()

    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # type: ignore
    video_writer = cv2.VideoWriter("./LR1/Output/video_copy.mp4", fourcc, 25, (w, h))
    while (True):
        ok, vid = video.read()
        if not ok: break

        video_writer.write(vid)

    cv2.destroyAllWindows()

copyVideo()
