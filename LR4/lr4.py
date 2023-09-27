import cv2
import numpy as np

window_index = 0


def show_image(name, img):
    global window_index
    name += ' #' + str(window_index)
    cv2.imshow(name, img)
    cv2.moveWindow(name, window_index %
                   5 * img.shape[1], window_index // 5 * (img.shape[0] + 30))
    window_index += 1


def task1(img, standard_deviation, kernel_size):
    imgBlurByCV2 = cv2.GaussianBlur(
        img, (kernel_size, kernel_size), standard_deviation)
    show_image('', imgBlurByCV2)
    return imgBlurByCV2


def task2(img, matr_gradient, img_angles):
    img_gradient_to_print = img.copy()
    max_gradient = np.max(matr_gradient)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_gradient_to_print[i][j] = (
                float(matr_gradient[i][j])/max_gradient)*255
    show_image('', img_gradient_to_print)

    img_angles_to_print = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_angles_to_print[i][j] = img_angles[i][j]/7*255
    show_image('', img_angles_to_print)


def task3(img, matr_gradient, img_angles):
    img_border_not_filtered = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            angle = img_angles[i][j]
            gradient = matr_gradient[i][j]
            if (i == 0 or i == img.shape[0] - 1 or j == 0 or j == img.shape[1] - 1):
                img_border_not_filtered[i][j] = 0
            else:
                x_shift = 0
                y_shift = 0
                if (angle == 0 or angle == 4):
                    x_shift = 0
                elif (angle > 0 and angle < 4):
                    x_shift = 1
                else:
                    x_shift = -1

                if (angle == 2 or angle == 6):
                    y_shift = 0
                elif (angle > 2 and angle < 6):
                    y_shift = -1
                else:
                    y_shift = 1

                is_max = gradient >= matr_gradient[i+y_shift][j +
                                                              x_shift] and gradient >= matr_gradient[i-y_shift][j-x_shift]
                img_border_not_filtered[i][j] = 255 if is_max else 0
    show_image('', img_border_not_filtered)
    return img_border_not_filtered


def task4(img, matr_gradient, img_border_not_filtered, bound_path):
    max_gradient = np.max(matr_gradient)
    lower_bound = max_gradient/bound_path
    upper_bound = max_gradient - max_gradient/bound_path
    img_border_filtered = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            gradient = matr_gradient[i][j]
            if (img_border_not_filtered[i][j] == 255):
                if (gradient >= lower_bound and gradient <= upper_bound):
                    flag = False
                    for k in range(-1, 2):
                        for l in range(-1, 2):
                            if (flag):
                                break
                            if (img_border_not_filtered[i+k][j+l] == 255 and matr_gradient[i+k][j+l] >= lower_bound):
                                flag = True
                                break
                    if (flag):
                        img_border_filtered[i][j] = 255
                elif (gradient > upper_bound):
                    img_border_filtered[i][j] = 255

    show_image('', img_border_filtered)


def lr4(path, standard_deviation, kernel_size, bound_path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    img = task1(img, standard_deviation, kernel_size)

    gx = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]
    gy = [[-1, -2, -1],
          [0, 0, 0],
          [1, 2, 1]]

    img_gx = convolution(img, gx)
    img_gy = convolution(img, gy)

    matr_gradient = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matr_gradient[i][j] = img[i][j]

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matr_gradient[i][j] = np.sqrt(
                img_gx[i][j] ** 2 + img_gy[i][j] ** 2)

    img_angles = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_angles[i][j] = get_angle_number(img_gx[i][j], img_gy[i][j])

    task2(img, matr_gradient, img_angles)

    img_border_not_filtered = task3(img, matr_gradient, img_angles)

    task4(img, matr_gradient, img_border_not_filtered, bound_path)


def convolution(img, kernel):
    kernel_size = len(kernel)
    x_start = kernel_size // 2
    y_start = kernel_size // 2
    matr = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            matr[i][j] = img[i][j]

    for i in range(x_start, len(matr)-x_start):
        for j in range(y_start, len(matr[i])-y_start):
            val = 0
            for k in range(-(kernel_size//2), kernel_size//2+1):
                for l in range(-(kernel_size//2), kernel_size//2+1):
                    val += img[i + k][j + l] * kernel[k +
                                                      (kernel_size//2)][l + (kernel_size//2)]
            matr[i][j] = val

    return matr


def get_angle_number(x, y):

    if x != 0:
        tg = y/x
    else:
        tg = 3

    if (x < 0):
        if (y < 0):
            if (tg > 2.414):
                return 0
            elif (tg < 0.414):
                return 6
            elif (tg <= 2.414):
                return 7
        else:
            if (tg < -2.414):
                return 4
            elif (tg < -0.414):
                return 5
            elif (tg >= -0.414):
                return 6
    else:
        if (y < 0):
            if (tg < -2.414):
                return 0
            elif (tg < -0.414):
                return 1
            elif (tg >= -0.414):
                return 2
        else:
            if (tg < 0.414):
                return 2
            elif (tg < 2.414):
                return 3
            elif (tg >= 2.414):
                return 4


if __name__ == "__main__":
    # task('LR4/img.jpg', 1, 3, 15)
    lr4('LR4/img.jpg', 10, 3, 15)
    lr4('LR4/img.jpg', 10, 11, 6)
    lr4('LR4/img.jpg', 100, 33, 55)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
