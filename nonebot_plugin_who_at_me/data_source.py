from typing import Set

from nonebot.adapters.onebot.v11 import Message, Bot


async def extract_member_at(
    group_id: int, message: Message, bot: Bot = None
) -> Set[str]:
    """提取消息中被艾特人的QQ号，返回集合"""
    try:
        qq_list = (
            await bot.get_group_member_list(group_id=group_id) 
            if bot is not None 
            else None
        )
        result = {
            segment.data["qq"]
            for segment in message
            if segment.type == "at" and "qq" in segment.data
        }
        if "all" in result and qq_list is not None:
            result.remove("all")
            result |= {str(member["user_id"]) for member in qq_list}
        return result
    except Exception:
        return set()  # 确保异常时返回空集合而不是None
