import time
from typing import List

import nonebot
from nonebot import on_command, on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment, MessageEvent, Message, Bot
from nonebot.exception import FinishedException, ActionFailed
from nonebot.params import EventMessage
from nonebot.permission import SUPERUSER

from .data_source import extract_member_at
from .database import MainTable
from .rule import message_at_rule
from .utils import node_custom, get_member_name

monitor = on_message(block=False, rule=message_at_rule)


async def create_record(bot: Bot, event: GroupMessageEvent, target_id):
    message = Message()
    if event.reply:
        message.append(MessageSegment.reply(event.reply.message_id))
    for segment in event.message:
        if segment.type == 'at':
            card = get_member_name(await bot.get_group_member_info(
                group_id=event.group_id,
                user_id=segment.data['qq']
            ))
            message.append(f'@{card}')
            continue
        message.append(segment)

    MainTable.create(
        operator_id=event.user_id,
        operator_name=event.sender.card or event.sender.nickname,
        target_id=target_id,
        group_id=event.group_id,
        time=str(int(time.time())),
        message=message,
        message_id=event.message_id,
    )


@monitor.handle()
async def _(bot: Bot, event: GroupMessageEvent, message=EventMessage()):
    if event.reply:
        target_id = event.reply.sender.user_id
        await create_record(bot=bot, event=event, target_id=target_id)
        raise FinishedException
    if member_at := extract_member_at(message=message):
        for target_id in member_at:
            await create_record(bot=bot, event=event, target_id=target_id)
        raise FinishedException


who_at_me = on_command("谁艾特我")


@who_at_me.handle()
async def _(bot: Bot, event: MessageEvent):
    res_list: List[MainTable] = MainTable.select().where(
        MainTable.target_id == event.user_id
    )
    message_list: List[MessageSegment] = list()
    for res in res_list:
        message_list.append(node_custom(
            content=res.message,
            user_id=res.operator_id,
            name=res.operator_name,
            time=res.time
        ))
        message_list.append(res.message)
    if isinstance(event, GroupMessageEvent):
        event: GroupMessageEvent
        await bot.call_api(
            "send_group_forward_msg",
            group_id=event.group_id,
            messages=message_list
        )
    else:
        try:
            await bot.call_api(
                "send_private_forward_msg",
                user_id=event.user_id,
                messages=message_list
            )
        except ActionFailed as e:
            if 'wording=API不存在' in (error := str(e)):
                nonebot.logger.error(f'发送合并转发失败，请确认您的协议端支持私聊合并转发！(如果使用go-cqhttp，请确保版本号不小于v1.0.0-rc2)\n{error}')
            else:
                raise e

clear_db = on_command("清除数据库", aliases={"clear_db", "db_clear"})


@clear_db.handle()
async def _(event: MessageEvent):
    MainTable.delete().where(MainTable.target_id == event.user_id).execute()
    await clear_db.finish("已清理数据库")


clear_db_all = on_command(
    "清除全部数据库", aliases={"clear_all", "db_clear --purge"}, permission=SUPERUSER
)


@clear_db_all.handle()
async def _():
    MainTable.delete().where(MainTable.target_id).execute()
    await clear_db.finish("已清理全部数据库")
