import cv2
import numpy as np

# 이미지 로드
image = cv2.imread('mission/01.png')

# 노이즈 제거 (Gaussian Blur)
denoised = cv2.GaussianBlur(image, (5, 5), 0)

# 샤프닝 필터 생성
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])

# 샤프닝 적용
sharpened = cv2.filter2D(denoised, -5, sharpening_kernel)

# 밝기 조정 (알파는 대비, 베타는 밝기)
alpha = 5.0  # 대비 조절
beta = -500 # 밝기 조절 (값을 낮추면 어두워짐)
adjusted = cv2.convertScaleAbs(sharpened, alpha=alpha, beta=beta)

# 처리된 이미지 저장
cv2.imwrite('mission_001.jpg', sharpened)