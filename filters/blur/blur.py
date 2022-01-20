from PIL import Image, ImageFilter

def blur(path: str, blur_intensity: float):
    img = Image.open(path)
    img = img.filter(ImageFilter.GaussianBlur(blur_intensity))
    img.save("output_image.jpg")

blur("input_image.jpg", 4)