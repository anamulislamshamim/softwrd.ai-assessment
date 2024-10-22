import motor.motor_asyncio
from datetime import datetime
from bson import ObjectId
import models

moto_client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
moto_db = moto_client.vehicle_allocation_system

# client = MongoClient("mongodb://localhost:27017/")
# db = client.vehicle_allocation_system

# Async function for allocating a vehicle
async def allocate_vehicle(data):
    # Check if vehicle is already allocated for the day
    response = await moto_db.allocations.find_one({
        "vehicle_id": data["vehicle_id"],
        "allocation_date": data["allocation_date"]
    })
    if response:
        raise ValueError("Vehicle already allocated for this day")
    
    # Insert the allocation into the database
    await moto_db.allocations.insert_one(data)
    return data 

async def update_allocation(allocation_id, data):
    # Ensure we don't update past allocations
    allocation = await moto_db.allocations.find_one({"_id": allocation_id})
    if allocation and allocation["allocation_date"] <= datetime.now():
        raise ValueError("Cannot update past allocations")
    await moto_db.allocations.update_one({"_id": ObjectId(allocation_id)}, {"$set": data})
    data = await moto_db.allocations.find_one({"_id": ObjectId(allocation_id)})
    return data

async def delete_allocation(allocation_id):
    allocation = await moto_db.allocations.find_one({"_id": ObjectId(allocation_id)})
    if allocation and allocation["allocation_date"] <= datetime.now():
        raise ValueError("Cannot delete past allocations")
    return moto_db.allocations.delete_one({"_id": ObjectId(allocation_id)})

async def get_allocation_history(employee_id=None, vehicle_id=None, date_range=None):
    query = {}
    if employee_id:
        query["employee_id"] = employee_id
    if vehicle_id:
        query["vehicle_id"] = vehicle_id
    if date_range:
        query["allocation_date"] = {"$gte": date_range[0], "$lte": date_range[1]}
        
    cursor = moto_db.allocations.find(query)
    allocations = []
    async for allocation in cursor:
        allocations.append(models.Allocation(**allocation))
    
    return allocations