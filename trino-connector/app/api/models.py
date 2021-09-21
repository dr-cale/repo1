# Here we put FastAPI models
from typing import List, Optional
from pydantic import BaseModel


class QueryModel(BaseModel):
    trinoCatalog: str
    trinoSchema: str
    table: str
    firstname: Optional[str] = None




