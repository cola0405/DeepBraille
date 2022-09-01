import cv2
import numpy as np


def read_img(img):
    (_, thresh) = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    kernel_2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))    # 形态学处理:定义矩形结构
    closed_2 = cv2.erode(thresh, kernel_2, iterations=2)            # 闭运算：迭代2次

    kernel_5 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))    # 形态学处理:定义矩形结构
    closed_5 = cv2.erode(thresh, kernel_5, iterations=5)            # 闭运算：迭代5次


    cv2.imshow('original_img', img)
    cv2.imshow("closed_2",closed_2)
    cv2.imshow("closed_5",closed_5)
    cv2.waitKey(0)
    return closed_2,closed_5


def project_img(image):
    height, width = image.shape[:2]
    print("image.shape",image.shape)

    # 垂直投影：统计并存储每一列的黑点数
    vertical = np.zeros(width,dtype=np.int32)
    for x in range(0, width):
        for y in range(0, height):
            if image[y, x] == 0:
                vertical[x]+=1

    # 水平投影  #统计每一行的黑点数
    horizontal = np.zeros(height,dtype=np.int32)
    for y in range(0, height):
        for x in range(0, width):
            if image[y, x] == 0:
                horizontal[y] += 1


    # 创建空白图片，绘制垂直投影图
    emptyImage = np.zeros((height, width, 3), np.uint8)
    for x in range(0, width):
        for y in range(0, vertical[x]):
            b = (255, 255, 255)
            emptyImage[y, x] = b

    # 绘制水平投影图
    emptyImage1 = np.zeros((height, width, 3), np.uint8)
    for y in range(0, height):
        for x in range(0, horizontal[y]):
            b = (255, 255, 255)
            emptyImage1[y, x] = b

    cv2.imshow('chuizhi', emptyImage)
    cv2.imshow('shuipin', emptyImage1)
    cv2.waitKey(0)



if __name__ == '__main__':
    img = cv2.imread('../img/wan.png')
    print("img",img.shape)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    retval, threshold_img = cv2.threshold(gray_img, 200, 255, cv2.THRESH_TOZERO)
    retval, threshold_img = cv2.threshold(threshold_img, 200, 255, cv2.THRESH_BINARY)
    dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 8))

    # 获得胀化后的图像
    dilate_img = cv2.dilate(threshold_img, dilate_kernel)
    # closed_2, closed_5 = read_img(img)
    project_img(dilate_img)
    # project_img(closed_5)
    cv2.destroyAllWindows()
