from dataclasses import replace
import random
import qrcode
import colorsys
import numpy as np
import PIL
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer, RoundedModuleDrawer, SquareModuleDrawer, CircleModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer

def random_colour():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]

    return tuple(rgb)

def replace_colour(image, orig_colour: tuple, replacement_colour: tuple):
    data = np.array(image)
    data[(data == orig_colour).all(axis = -1)] = replacement_colour
    img = PIL.Image.fromarray(data, mode='RGB')
    return img

def random_style():
    styles = [GappedSquareModuleDrawer(), RoundedModuleDrawer(), SquareModuleDrawer(), CircleModuleDrawer(), VerticalBarsDrawer(), HorizontalBarsDrawer()]
    return random.choice(styles)

def generate_qrcode(path: str):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data("pycasso")
    qr.make(fit=True)

    img = qr.make_image(image_factory=StyledPilImage, module_drawer=random_style())

    # img = replace_colour(img, (0, 0, 0), random_colour())
    img = replace_colour(img, (255, 255, 255), random_colour())
    img.save(path)

for i in range(10):
    generate_qrcode(f"qrcode/qrcode_examples/image_{i}.png")