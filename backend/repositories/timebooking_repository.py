from datetime import date
from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.timebooking import TimeBookingDB, TimeBookingCreate, TimeBookingUpdate

class TimeBookingRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_timebooking(self, timebooking: TimeBookingCreate) -> TimeBookingDB:
        timebooking_data = timebooking.dict()

        db_timebooking = TimeBookingDB(**timebooking_data)
        self.db.add(db_timebooking)
        self.db.commit()
        self.db.refresh(db_timebooking)
        return db_timebooking
    
    def get_timebooking_by_date(self, date: date) -> List[TimeBookingDB]:
        return self.db.query(TimeBookingDB).filter(TimeBookingDB.date == date).all()