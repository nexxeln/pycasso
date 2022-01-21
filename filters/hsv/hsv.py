import cv2

def hsv(path: str):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imwrite("output_image.png", img)

hsv("input_image.jpg")