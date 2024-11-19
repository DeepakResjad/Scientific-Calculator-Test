# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY scientific_calculator.py .

# Set the default command to run the Python interpreter
CMD ["python3", "scientific_calculator.py"]
