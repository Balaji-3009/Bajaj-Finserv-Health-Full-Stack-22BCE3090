from pydantic import BaseModel
from typing import List

class InputBase(BaseModel):
    data: List[str]