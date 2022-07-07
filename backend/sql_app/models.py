import enum
from sqlalchemy import Enum, ForeignKey, PrimaryKeyConstraint, String, Date, Column, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from database import Base
# class IPOType(enum.Enum):
#     MAINLINE = "mainline"
#     SME = "sme"

class IPO(Base):
    __tablename__ = "ipo_listing"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, unique=True)
    open_date = Column(Date)
    close_date = Column(Date)
    lot_size = Column(String)
    issue_price = Column(String)
    cost_of_one_lot = Column(String)
    ipo_type = Column(String)