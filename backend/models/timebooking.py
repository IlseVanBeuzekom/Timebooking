from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date
from pydantic import BaseModel

Base = declarative_base()

class TimeBookingDB(Base):
    __tablename__ = 'timebookings'

    id = Column(Integer, primary_key=True, index=True)
    project_naam = Column(String)
    ticket_nummer = Column(String, nullable=False)
    beschrijving = Column(String)
    date = Column(Date, index=True)
    start_tijd = Column(DateTime, default=datetime.utcnow)
    eind_tijd = Column(DateTime, default=datetime.utcnow)
    duratie = Column(Integer)

# Pydantic schemas
class TimeBookingBase(BaseModel):
    project_naam: str
    ticket_nummer: str
    beschrijving: str
    date: date
    start_tijd: datetime
    eind_tijd: datetime
    duratie: int

class TimeBookingCreate(TimeBookingBase):
    pass

class TimeBookingUpdate(TimeBookingBase):
    pass    

class TimeBookingResponse(TimeBookingBase):
    id: int

    class Config:
        from_attributes = True