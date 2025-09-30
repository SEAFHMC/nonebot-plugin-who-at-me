from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message
from nonebot.params import EventMessage
from .data_source import extract_member_at


async def message_at_rule(event: GroupMessageEvent, message: Message = EventMessage()) -> bool:
    # 检查是否有@消息或回复
    has_at = await extract_member_at(event.group_id, message=message)
    return bool(has_at) or bool(event.reply)  # 确保返回布尔值
