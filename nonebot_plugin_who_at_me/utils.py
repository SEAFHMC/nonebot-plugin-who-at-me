from PIL import Image, ImageFont, ImageDraw
from typing import Tuple


class DataText:
    def __init__(self, L, T, size, text, path, anchor="lt") -> None:
        self.L = L
        self.T = T
        self.text = str(text)
        self.path = path
        self.font = ImageFont.truetype(self.path, size)
        self.anchor = anchor


def write_text(
    image: Image.Image,
    font,
    text="text",
    pos=(0, 0),
    color=(255, 255, 255, 255),
    anchor="lt",
    stroke_width=0,
    stroke_fill="Black",
) -> Image.Image:
    rgba_image = image
    text_overlay = Image.new("RGBA", rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)
    image_draw.text(
        pos,
        text,
        font=font,
        fill=color,
        anchor=anchor,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )
    return Image.alpha_composite(rgba_image, text_overlay)


def draw_text(
    image,
    class_text: DataText,
    color: Tuple[int, int, int, int] = (255, 255, 255, 255),
    stroke_width=0,
    stroke_fill="Black",
) -> Image.Image:
    font = class_text.font
    text = class_text.text
    anchor = class_text.anchor
    color = color
    return write_text(
        image,
        font,
        text,
        (class_text.L, class_text.T),
        color,
        anchor,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )
