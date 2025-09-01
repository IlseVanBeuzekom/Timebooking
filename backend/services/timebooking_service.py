from ..repositories.timebooking_repository import TimeBookingRepository
from ..models.timebooking import TimeBookingCreate, TimeBookingResponse
from typing import List, Optional
from datetime import date

class TimeBookingService:
    def __init__(self, timebooking_repository: TimeBookingRepository):
        self.timebooking_repository = timebooking_repository

    def create_timebooking(self, timebooking_data: TimeBookingCreate) -> TimeBookingResponse:
        db_timebooking = self.timebooking_repository.create_timebooking(timebooking_data)
        return db_timebooking
    
    def get_timebookings_by_date(self, date: date) -> List[TimeBookingResponse]:
        db_timebookings = self.timebooking_repository.get_timebooking_by_date(date)
        return db_timebookings
    
    