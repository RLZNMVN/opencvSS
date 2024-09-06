#이미지 불러오기는 동일, 출력>>cv2 대신 matplotlib
#opencv와 matplotlib 차이 이해

import cv2
import sys
from matplotlib import pyplot as plt

fileName = 'data/cat.jpg'

img = cv2.imread(fileName)

if img is None:
    sys.exit("image load is failed")
    

plt.imshow(img)
plt.show()