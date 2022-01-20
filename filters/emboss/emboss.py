from PIL import Image, ImageFilter

def blur(path: str):
    img = Image.open(path)
    img = img.filter(ImageFilter.EMBOSS)
    img.save("output_image.jpg")

blur("input_image.jpg")