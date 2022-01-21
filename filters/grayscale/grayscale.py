import cv2

def grayscale(path: str):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("output_image.png", img)

grayscale("input_image.jpg")