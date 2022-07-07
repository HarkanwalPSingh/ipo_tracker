from datetime import date
from lib2to3.pytree import Base
from pydantic import BaseModel

class IPOBase(BaseModel):
    company : str
    open_date : date
    close_date : date
    lot_size : str
    issue_price : str
    cost_of_one_lot : str
    ipo_type : str

class IPO(IPOBase):
    id: int

    class Config:
        orm_mode = True