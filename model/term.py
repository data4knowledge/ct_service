from typing import List
from pydantic import BaseModel

class Term(BaseModel):
  uuid: str
  uri: str
  label: str
  identifier: str
  notation: str
  alt_label: List[str]
  pref_label: str
  definition: str