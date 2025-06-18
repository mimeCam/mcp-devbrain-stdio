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

# Expose the port your application listens on (if any, adjust as needed)
# For a FastMCP server, it might be listening on a specific port.
# If you know the port, please let me know, otherwise, I'll omit this or add a placeholder.
# EXPOSE 8000

# Define environment variable
ENV PYTHONPATH=/app/src

# Run the application
# Corrected entry point: src/server.py
CMD ["python", "src/server.py"]