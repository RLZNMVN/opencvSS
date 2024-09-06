import cv2

# 이미지 로드
image = cv2.imread('mission/05.png')

# 노이즈 제거 (Fast Non-Local Means Denoising)
denoised = cv2.fastNlMeansDenoisingColored(image, None, h=10, templateWindowSize=7, searchWindowSize=21)

# 밝기 조정 (알파는 대비, 베타는 밝기)
alpha = 1.0  # 대비 조절
beta = -20   # 밝기 조절 (값을 낮추면 어두워짐)
adjusted = cv2.convertScaleAbs(denoised, alpha=alpha, beta=beta)

# 처리된 이미지 저장
cv2.imwrite('mission_005.jpg', adjusted)