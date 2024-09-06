#파일에서 이미지 읽어 출력

import cv2
import sys
fileName = "data/cat.jpg"

#이미지를 불러오는 함수
img = cv2.imread(fileName)
print(img.shape)

#예외처리 루틴: 이미지를 읽어오지 못했을때
if img is None:
    print("img load fail")
    #프로그램 종료
    sys.exit()
    
cv2.namedWindow('img')
cv2.imshow('img', img)

cv2.imwrite('cat.png',img)
loop=True
while(loop):
    imkey = cv2.waitKey()
    print(imkey)
    if imkey == ord('q'):
        cv2.destroyAllWindows()
        loop=False