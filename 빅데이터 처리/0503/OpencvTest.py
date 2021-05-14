from cv2 import cv2

# 참고 사이트
# https://github.com/ndb796/Python-Data-Analysis-and-Image-Processing-Tutorial/tree/master/06.%20OpenCV%20%EC%86%8C%EA%B0%9C%20%EB%B0%8F%20%EA%B8%B0%EB%B3%B8%20%EC%82%AC%EC%9A%A9%EB%B2%95

# imread => 이미지를 읽어 객체로 만드는 함수
# imread(file_name, flag)
# flag : 이미지 읽는 방법 설정
# - IMREAD_COLOR : 이미지 color로 읽고 투명한 부분 무시
# - IMREAD_GRAYSCALE : 이미지를 grayscale로 읽기
# - IMREAD_UNCHANGED : 이미지 color로 읽고, 투명한 부분도 읽기
img_basic = cv2.imread('cat.png',cv2.IMREAD_COLOR)

# imshow(title, image) => 이미지 화면에 출력
# - title : 윈도우 창 이름
# - image : 출력할 이미지 객체
cv2.imshow('cat',img_basic)

# waitKey => 키보드 입력 처리하는 함수
# waitKey(time) , 0일 경우 무한 대기
cv2.waitKey(0)

# imwrite(file_name, image) => 이미지를 파일로 저장하는 함수
# file_name : 저장할 이름
# image : 저장할 객체
cv2.imwrite('result1.png',img_basic)

# cv2.cvtColor(image, flag) => 이미지 색상 형태 변경 함수
img_gray = cv2.cvtColor(img_basic,cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Gra',img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png',img_gray)

# 화면의 모든 창을 닫는 함수
cv2.destroyAllWindows()