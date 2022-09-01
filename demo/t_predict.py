import cv2
import numpy as np
from src.utils.SimpleBrailleProcessor import BrailleProcessor

def predict():
    img = cv2.imread('img/p1.png')
    cv2.imshow("img", img)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bp = BrailleProcessor('187.h5')
    re_size = (64, 64)
    img = gray_img
    img = cv2.resize(img, re_size, interpolation=cv2.INTER_AREA)

    img = img / 255
    img = np.expand_dims(img, axis=2).astype('float32')
    bp.predict(img)
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()


if __name__ == '__main__':
    predict()