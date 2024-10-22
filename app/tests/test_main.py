import sys
import os
# Add the directory containing `main.py` to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
# from main import app  # Import the FastAPI app from main.py
from main import app

import pytest
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_allocation():
    allocation_data = {
        "employee_id": "emp1",
        "vehicle_id": "veh1",
        "allocation_date": datetime.now().isoformat()
    }
    
    response = client.post("/allocations/", json=allocation_data)
    assert response.status_code == 200
    assert response.json()["employee_id"] == allocation_data["employee_id"]