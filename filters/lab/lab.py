import cv2

def lab(path: str):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    cv2.imwrite("output_image.png", img)

lab("input_image.jpg")