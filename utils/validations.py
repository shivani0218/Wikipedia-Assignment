from pydantic import BaseModel
from typing import Optional

class WordFrequencyParams(BaseModel):
    topic: Optional[str]
    n: Optional[str]
    namespace_filter: Optional[list]=None
