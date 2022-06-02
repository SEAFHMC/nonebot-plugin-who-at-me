from typing import Set, List
from nonebot.adapters.onebot.v11 import Message
from PIL import Image, ImageDraw, ImageFont
from .database import MainTable
from pathlib import Path
from .utils import DataText, draw_text


def extract_member_at(message: Message) -> Set[str]:
    """提取消息中被艾特人的QQ号
    参数:
        message: 消息对象
    返回:
        被艾特列表
    """
    return {
        segment.data["qq"]
        for segment in message
        if (segment.type == "at") and ("qq" in segment.data)
    }


boxes = [400, 400, 600, 500]


def db2image(data: List[MainTable]) -> Image.Image:
    image = Image.new("RGBA", (sum(boxes), 50 * (len(data) + 1) + 70), "white")
    # Table Head
    tabke_head = ["昵称", "群号", "时间", "消息"]
    image.alpha_composite(draw_line(tabke_head))
    draw = ImageDraw.Draw(image)
    draw.line(((0, 70), (sum(boxes), 70)), "black", width=2)
    for row, line in enumerate(data):
        img_line = draw_line(
            data=[line.operator_name, line.group_id, line.time, line.message]
        )
        image.alpha_composite(img_line, (0, (row + 2) * 50))
    return image


def draw_line(data: List) -> Image.Image:
    image = Image.new("RGBA", (sum(boxes), 50), (0, 0, 0, 0))
    font = str(Path(__file__).parent.absolute() / "STZHONGS.TTF")
    truefont = ImageFont.truetype(font=font, size=50)
    for coloum, text in enumerate(data):
        text = text if truefont.getsize(str(text))[0] <= boxes[coloum] else text[:5]
        text_overlay = Image.new("RGBA", (boxes[coloum], 50), (0, 0, 0, 0))
        write_text = DataText(int(boxes[coloum] / 2), 25, 50, text, font, anchor="mm")
        text_overlay = draw_text(text_overlay, write_text, "black")
        image.alpha_composite(text_overlay, (sum(boxes[:coloum]), 0))
    return image
