***Softwrd Assessment for Junior Software Engineer (Backend) position***

**Ambiguity with Requirements**
For example: 

Vehicle Allocation Logic:
The description mentions that "a vehicle can be allocated only once on any specific day," but it could clarify how to handle attempts to allocate the same vehicle by different employees on the same day.

CRUD Operations:
The requirement specifies "create, update, and delete" operations for vehicle allocation. It would be helpful to specify the conditions under which each operation can be performed, such as:
Can an allocation be updated after the allocation date?
Is there a limit to how many times an allocation can be updated?
What happens if an employee tries to delete an allocation after the allocation date?


***Technologies:***
FastAPI, MongoDB, Docker

***Optimization for Millions Users***
1. Redis: Used Redis for caching and reduces database operations
2. Motor: Async MongoDB Operations: Motor is an asynchronous MongoDB driver for Python that should replace Pymongo in high-load systems. Pymongo is synchronous, meaning every database call will block until it completes, slowing down the system under heavy loads.

***Further Optimization Ideas***
1. Concurrency and Worker Scaling: With FastAPI, you can use Uvicorn with multiple workers to scale horizontally, allowing the system to handle more concurrent requests. In a production environment, you can use something like Gunicorn to manage Uvicorn processes. command: uvicorn app.main:app --workers 4 --host 0.0.0.0 --port 8000
2. MongoDB Sharding: As the dataset grows, MongoDB’s sharding will become essential. Sharding enables horizontal scaling of the database by distributing data across multiple machines. For example, you could shard on allocation_date or vehicle_id to split the data logically across multiple servers.
3. Proper Database Indexing: Ensure that MongoDB collections have the proper indexes on fields used frequently in queries: 1. vehicle_id 2. allocation_date 3. employee_id 
For example: db.allocations.create_index([("vehicle_id", 1), ("allocation_date", 1)])
4. Horizontally scale the application using Kubernetes for auto-scaling during peak traffic.

***Unit Test:***
I tried to write unit test. You will find it inside /app/tests/test_main.py file. Since, I used moto (Async MongoDB Operation) that's why it become a little hard to write unit test now. Because I have not enough time to debug it and write proper test for async operation. But I will be able to learn in depth if I will get the opportunity. 

***Run the Application***
1. In local machine: Navigate to /app and run the following command: <br>
 a. pip install -r requirements.txt</br>
 b. uvicorn main:app --reload </br>
 c. Don't forget to run your Radis server
2. Using Docker: Navigate root folder where docker-compose exist and run the following command: 
<br>a. run your docker engine first
<br>b. docker-compose up --build<br> 

***swagger documentation:***
Please run the application first. 
Link: http://localhost:8000/docs <br>


***Some of my words*** <br>
Alghough I've good experience in Python. In my current company I worked with Django. I never worked with FastAPI before. Since I have full time job. So, I did not get enough time to learn FastAPI. But still I tried to fulfill your assessment requirements and tried to scall the solution for millions of users. I can assure you If I will get the opportunity I will be one of your best employee. My professional dream is to become a software engineer at Google. Thank you very much for considering my application. 