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


def generate_art(path: str):
    print("Generating Art!")
    actual_size = 128
    scale_factor = 2
    image_size = actual_size * scale_factor
    image_bg_colour = (0, 0, 0)
    start_colour = random_colour()
    end_colour = random_colour()
    padding = 16 * scale_factor 
    image = Image.new("RGB", size=(image_size, image_size), color=image_bg_colour)

    # drawing interface
    draw = ImageDraw.Draw(image)
    points = []

    # generating the points
    for _ in range(10):
        random_xy = (random.randint(padding, image_size - padding), random.randint(padding, image_size - padding))
        points.append(random_xy)

    # finding corner points
    min_x = min([j[0] for j in points])
    max_x = max([j[0] for j in points])
    min_y = min([j[1] for j in points])
    max_y = max([j[1] for j in points])

    # centering the image
    x_distance = min_x - (image_size - max_x)
    y_distance = min_y - (image_size - max_y)
    for i, point in enumerate(points):
        points[i] = (point[0] - x_distance // 2, point[1] - y_distance // 2)

    # draw the lines
    thickness = 0

    for i, point in enumerate(points):

        # overlay canvas to make it look better
        overlay_image = Image.new("RGB", size=(image_size, image_size), color=image_bg_colour)
        overlay_draw = ImageDraw.Draw(overlay_image)

        point_1 = point
        if i == len(points) - 1:
            point_2 = points[0]
        else:
            point_2 = points[i + 1]
        line_xy = (point_1, point_2)
        colour_factor = i / (len(points) - 1)
        line_colour = fade_colour(start_colour, end_colour, colour_factor)
        thickness += scale_factor
        overlay_draw.line(line_xy, fill=line_colour, width=thickness)
        image = ImageChops.add(image, overlay_image)

    image = image.resize((actual_size, actual_size), resample=Image.ANTIALIAS)
    image.save(path)



if __name__ == "__main__":
    generate_art("test_image.png")