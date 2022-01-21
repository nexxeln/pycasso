import cv2

def sketch(path: str):
    img = cv2.imread(path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img = cv2.bitwise_not(gray_img)
    blur_img = cv2.GaussianBlur(invert_img, (21, 21), 0)
    invert_blur_img = cv2.bitwise_not(blur_img)

    sketch = cv2.divide(gray_img, invert_blur_img, scale=256.0 )
    cv2.imwrite("output_image.png", sketch)

sketch("input_image.jpg")
