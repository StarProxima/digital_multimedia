import cv2
import numpy as np

def gauss(x, y, omega, a, b):
    omegaIn2 = 2 * omega ** 2
    m1 = 1/(np.pi * omegaIn2)
    m2 = np.exp(-((x-a) ** 2 + (y-b) ** 2)/omegaIn2)
    return m1*m2

def gaussBlur(img, size, deviation):
    kernel = np.ones((size, size))
    a = b = (size+1) // 2

    for i in range(size):
        for j in range(size):
            kernel[i, j] = gauss(i, j, deviation, a, b)

    print(kernel)

    sum = 0
    for i in range(size):
        for j in range(size):
            sum += kernel[i, j]
    for i in range(size):
        for j in range(size):
            kernel[i, j] /= sum
    print(kernel)

    blur = img.copy()
    sx = size // 2
    sy = size // 2
    for i in range(sx, blur.shape[0]-sx):
        for j in range(sy, blur.shape[1]-sy):
            value = 0
            for k in range(-(size//2), size//2+1):
                for l in range(-(size//2), size//2+1):
                    value += img[i + k, j + l] * kernel[(size//2) + k,  (size//2) + l]
            blur[i, j] = value

    return blur


def lr3():
    img = cv2.imread("LR3/img.jpg", cv2.IMREAD_GRAYSCALE)
    cv2.imshow('img', img)

    deviation = 5
    size = 3
    blur1 = gaussBlur(img, size, deviation)
    cv2.imshow(f'size: {size}, deviation: {deviation}', blur1)

    deviation = 10
    size = 7
    blur2 = gaussBlur(img, size, deviation)
    cv2.imshow(f'size: {size}, deviation: {deviation}', blur2)

    blurOpenCV = cv2.GaussianBlur(img, (size, size), deviation)
        
    cv2.imshow(f'OpenCV - size: {size}, deviation: {deviation}', blurOpenCV)
    cv2.waitKey(0)

lr3()
