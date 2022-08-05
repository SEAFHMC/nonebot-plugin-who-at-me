from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    """
    who-at-me的超时时间, 单位为天
    """

    reminder_expire_time: int = 3
