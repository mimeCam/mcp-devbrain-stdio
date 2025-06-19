# Use an official Python runtime as a base image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Define environment variable
ENV PYTHONPATH=/app/src

# Run the application
ENTRYPOINT ["python", "src/mcp_server/server.py"]
