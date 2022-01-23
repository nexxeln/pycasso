import random
import colorsys
from PIL import Image, ImageDraw, ImageChops

def random_colour():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]

    return tuple(rgb)

def fade_colour(start_colour, end_colour, factor: float):
    reciprocal = 1 - factor
    return (
        int(start_colour[0] * reciprocal + end_colour[0] * factor),
        int(start_colour[1] * reciprocal + end_colour[1] * factor),
        int(start_colour[2] * reciprocal + end_colour[2] * factor)
    )

def generate_octagon_art(path: str):
    print("Generating Octagon Art!")
    actual_size = 512
    scale_factor = 1
    image_size = actual_size * scale_factor
    image_bg_colour = (0, 0, 0)
    start_colour = random_colour()
    end_colour = random_colour()
    padding = 16 * scale_factor 
    image = Image.new("RGB", size=(image_size, image_size), color=image_bg_colour)

    # drawing interface
    draw = ImageDraw.Draw(image)
    point = (256, 256)


    for i in range(9):

        # overlay canvas to make it look better
        rotate = i * 150
        overlay_image = Image.new("RGB", size=(image_size, image_size), color=image_bg_colour)
        overlay_draw = ImageDraw.Draw(overlay_image)
        bounding_circle_xy = point
        colour_factor = i / (9 - 1)
        line_colour = fade_colour(start_colour, end_colour, colour_factor)
        overlay_draw.regular_polygon((bounding_circle_xy, 50), n_sides=8, rotation=rotate, outline=line_colour)
        image = ImageChops.add(image, overlay_image)

    image = image.resize((actual_size, actual_size), resample=Image.ANTIALIAS)
    image.save(path)    

if __name__ == "__main__":
    for i in range(10):
        generate_octagon_art(f"octagon_examples/image_{i}.png")