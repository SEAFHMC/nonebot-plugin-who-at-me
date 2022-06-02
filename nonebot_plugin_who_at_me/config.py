from pydantic import BaseModel, Extra
from typing import List


class Config(BaseModel, extra=Extra.ignore):
    at_reminder: List[str] = []
