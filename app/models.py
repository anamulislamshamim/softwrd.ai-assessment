from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId

# # Custom ObjectId type for MongoDB
# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate

#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid ObjectId')
#         return ObjectId(v)

# # Employee Model
# class Employee(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     name: str
#     email: str

#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}

# # Vehicle Model
# class Vehicle(BaseModel):
#     id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
#     vehicle_id: str
#     driver_id: str

#     class Config:
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
#         json_encoders = {ObjectId: str}

# Allocation Model
# Pydantic model for validation
class Allocation(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: datetime

    # class Config:
    #     allow_population_by_field_name = True
    #     arbitrary_types_allowed = True
    #     json_encoders = {ObjectId: str}
