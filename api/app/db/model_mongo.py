from typing import List, Union

from pydantic import BaseModel


class Signal(BaseModel):
    key: str
    moment: str
    data: dict

