from pydantic import BaseModel
from datetime import datetime

class AllocationCreate(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: datetime

class AllocationUpdate(BaseModel):
    vehicle_id: str

class AllocationResponse(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: datetime
