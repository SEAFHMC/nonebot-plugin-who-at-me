from typing import List
from io import BytesIO
from nonebot import on_command, on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent, MessageSegment, MessageEvent
from nonebot.params import EventMessage
from nonebot.exception import FinishedException
from nonebot.permission import SUPERUSER
from time import strftime, localtime
from .data_source import extract_member_at, db2image
from .database import MainTable
from .rule import message_at_rule


monitor = on_message(block=False, rule=message_at_rule)


def create_record(event: GroupMessageEvent, target_id):
    message_text = event.message.extract_plain_text()
    MainTable.create(
        operator_id=event.user_id,
        operator_name=event.sender.card or event.sender.nickname,
        target_id=target_id,
        group_id=event.group_id,
        time=strftime("%Y-%m-%d %H:%M:%S", localtime(event.time)),
        message=(message_text if len(message_text) <= 10 else message_text[:10] + "…"),
        message_id=event.message_id,
    )


@monitor.handle()
async def _(event: GroupMessageEvent, message=EventMessage()):
    if event.reply:
        target_id = event.reply.sender.user_id
        create_record(event=event, target_id=target_id)
        raise FinishedException
    if menmber_at := extract_member_at(message=message):
        for target_id in menmber_at:
            create_record(event=event, target_id=target_id)
        raise FinishedException


who_at_me = on_command("谁艾特我")


@who_at_me.handle()
async def _(event: MessageEvent):
    res_list: List[MainTable] = MainTable.select().where(
        MainTable.target_id == event.user_id
    )
    image = db2image(data=res_list)
    buffer = BytesIO()
    image.save(buffer, "png")
    await who_at_me.finish(MessageSegment.image(buffer))


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
