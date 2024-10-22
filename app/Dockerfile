# Step 1: Set the base image to Python 3.9-slim
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the rest of the application code from the current directory
COPY . /app

# Step 4: Install the required Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Specify the command to run the FastAPI app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
