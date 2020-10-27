import cv2
image = cv2.imread('dog_feed.jpg')

# 高度縮小為416，寬度也等比例縮小
r = 416 / image.shape[0]
dim = (int(image.shape[1] * r), 416)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (1,1), 0)
cannied = cv2.Canny(blurred,120,150,apertureSize=3) 
cv2.imshow('Input', image)
cv2.imshow('Result', cannied)
cv2.waitKey(0)
cv2.destroyAllWindows()



