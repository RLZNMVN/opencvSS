import cv2

# 이미지 로드
image = cv2.imread('mission/03.png')

# 노이즈 제거 (Non-Local Means Denoising)
# h: 필터 강도, 값이 클수록 노이즈 제거가 강해짐
denoised = cv2.fastNlMeansDenoisingColored(image, None, h=10, templateWindowSize=7, searchWindowSize=21)

# 처리된 이미지 저장
cv2.imwrite('mission_003.jpg', denoised)