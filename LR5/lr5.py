import cv2
import numpy as np


def task(name, kernel_size, deviation, min_tresh, min_s):
    video = cv2.VideoCapture(r'.\LR5\vid.mov', cv2.CAP_ANY)
    fourcc = cv2.VideoWriter.fourcc(*'mp4v')
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_writer = cv2.VideoWriter('./LR5/motion' + name + '.mp4', fourcc, 25, (w, h))

    prev_img = None
    img = None

    while True:
        if not img is None:
            prev_img = img.copy()
        is_ok, frame = video.read()
        if not is_ok:
            break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(
            img, (kernel_size, kernel_size), deviation)

        if not prev_img is None:
            diff = cv2.absdiff(img, prev_img)
            thresh = cv2.threshold(
                diff, min_tresh, 255, cv2.THRESH_BINARY)[1]
            contours, _ = cv2.findContours(
                thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            for contour in contours:
                s = cv2.contourArea(contour)
                if s > min_s:
                    video_writer.write(frame)
                    break
                
    video_writer.release()


if __name__ == '__main__':
    task('1', 3, 50, 60, 10)
    task('2', 9, 80, 60, 20)
    task('3', 13, 90, 40, 20)
