import cv2
import numpy as np


# 이미지 불러오기
green_image = cv2.imread('data2/green.jpg')
red_image = cv2.imread('data2/red.jpg')
yellow_image = cv2.imread('data2/yellow.jpg')

# 이미지의 최소 크기로 통일
height = min(green_image.shape[0], red_image.shape[0], yellow_image.shape[0])
width = min(green_image.shape[1], red_image.shape[1], yellow_image.shape[1])

green_resized = cv2.resize(green_image, (width, height))
red_resized = cv2.resize(red_image, (width, height))
yellow_resized = cv2.resize(yellow_image, (width, height))


# 트랙바 콜백 함수
def nothing(x):
    pass

# 윈도우 생성
cv2.namedWindow('Trackbars')

# 트랙바 생성
cv2.createTrackbar('Lower_H', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('Lower_S', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Lower_V', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Upper_H', 'Trackbars', 179, 179, nothing)
cv2.createTrackbar('Upper_S', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('Upper_V', 'Trackbars', 255, 255, nothing)

while True:
    # 트랙바 위치 읽기
    lower_h = cv2.getTrackbarPos('Lower_H', 'Trackbars')
    lower_s = cv2.getTrackbarPos('Lower_S', 'Trackbars')
    lower_v = cv2.getTrackbarPos('Lower_V', 'Trackbars')
    upper_h = cv2.getTrackbarPos('Upper_H', 'Trackbars')
    upper_s = cv2.getTrackbarPos('Upper_S', 'Trackbars')
    upper_v = cv2.getTrackbarPos('Upper_V', 'Trackbars')

    # HSV 범위 설정
    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    # 이미지를 HSV로 변환
    green_hsv = cv2.cvtColor(green_resized, cv2.COLOR_BGR2HSV)
    red_hsv = cv2.cvtColor(red_resized, cv2.COLOR_BGR2HSV)
    yellow_hsv = cv2.cvtColor(yellow_resized, cv2.COLOR_BGR2HSV)

    # 색상에 대한 마스크 생성
    green_mask = cv2.inRange(green_hsv, lower_color, upper_color)
    red_mask = cv2.inRange(red_hsv, lower_color, upper_color)
    yellow_mask = cv2.inRange(yellow_hsv, lower_color, upper_color)

    # 마스크를 사용해 색상 추출
    green_result = cv2.bitwise_and(green_resized, green_resized, mask=green_mask)
    red_result = cv2.bitwise_and(red_resized, red_resized, mask=red_mask)
    yellow_result = cv2.bitwise_and(yellow_resized, yellow_resized, mask=yellow_mask)

    # 각 색상의 흰색 픽셀 개수 계산
    def count_white_pixels(mask):
        return np.sum(mask == 255)

    green_pixel_count = count_white_pixels(green_mask)
    red_pixel_count = count_white_pixels(red_mask)
    yellow_pixel_count = count_white_pixels(yellow_mask)

    # 가장 많은 픽셀을 가진 색상 결정
    def determine_dominant_color(green_count, red_count, yellow_count):
        counts = {'Green': green_count, 'Red': red_count, 'Yellow': yellow_count}
        dominant_color = max(counts, key=counts.get)
        return dominant_color

    dominant_color = determine_dominant_color(green_pixel_count, red_pixel_count, yellow_pixel_count)
    
   
    
    # 결합된 이미지 출력
    combined_image = cv2.bitwise_or(green_result, red_result)
    combined_image = cv2.bitwise_or(combined_image, yellow_result)
    cv2.imshow('Combined Traffic Lights', combined_image)

    # 색상 정보 출력
    print(f"Green pixels: {green_pixel_count}")
    print(f"Red pixels: {red_pixel_count}")
    print(f"Yellow pixels: {yellow_pixel_count}")
    print(f"Dominant Color: {dominant_color}")

    # 'q' 키를 눌러 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()