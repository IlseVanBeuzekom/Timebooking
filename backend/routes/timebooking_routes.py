from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..models.timebooking import TimeBookingDB, TimeBookingCreate, TimeBookingResponse, TimeBookingUpdate
from ..services.timebooking_service import TimeBookingService
from ..repositories.timebooking_repository import TimeBookingRepository
from ..config.database import get_db

router = APIRouter(prefix="/timebookings", tags=["TimeBookings"])

def get_timebooking_service(db: Session = Depends(get_db)) -> TimeBookingService:
    timebooking_repository = TimeBookingRepository(db)
    return TimeBookingService(timebooking_repository)

@router.post("/", response_model=TimeBookingResponse)
async def create_timebooking( timebooking: TimeBookingCreate, timebooking_service: TimeBookingService = Depends(get_timebooking_service) ):
    try:
        return timebooking_service.create_timebooking(timebooking)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/{date}", response_model=List[TimeBookingResponse])
async def get_timebookings_by_date(date: str, timebooking_service: TimeBookingService = Depends(get_timebooking_service)):
    try:
        return timebooking_service.get_timebookings_by_date(date)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))