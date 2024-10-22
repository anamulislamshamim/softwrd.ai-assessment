from fastapi import FastAPI, HTTPException
import crud 
import schemas
import models
from datetime import datetime
from typing import List
import json

import redis
cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

app = FastAPI()

@app.post("/allocations/", response_model=models.Allocation)
async def create_allocation(allocation: models.Allocation):
    try:
        # Await the allocate_vehicle function
        response = await crud.allocate_vehicle(allocation.dict())
        # Ensure the response is in the correct format (e.g., dict or Allocation model)
        return models.Allocation(**response)  # Convert response to the expected model
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/allocations/{allocation_id}", response_model=models.Allocation)
async def update_allocation(allocation_id: str, allocation: models.Allocation):
    try:
        response = await crud.update_allocation(allocation_id, allocation.dict())
        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/allocations/{allocation_id}")
async def delete_allocation(allocation_id: str):
    try:
        await crud.delete_allocation(allocation_id)
        return {"msg": "Allocation deleted succesfully!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/allocations/", response_model=List[models.Allocation])
async def get_allocation_history(employee_id: str = None, vehicle_id: str = None, start_date: datetime = None, end_date: datetime = None):
    # using redis for caching and reduce database operation
    date_range = [start_date, end_date] if start_date and end_date else None
    
    date_str = "-".join(list(map(lambda x: str(x), date_range))) if date_range else ""
    
    cache_key = f"{employee_id}_{vehicle_id}_{date_str}"
    
    if cache.exists(cache_key):
        return [models.Allocation(**allocation) for allocation in json.loads(cache.get(cache_key))]
    
    results = await crud.get_allocation_history(employee_id, vehicle_id, date_range)
    results = [models.Allocation(**allocation) for allocation in results if isinstance(allocation, dict)]
    # cache the new results
    if results:
        cache.set(cache_key, json.dumps([json.loads(allocation.json()) for allocation in results]))
    
    return results
