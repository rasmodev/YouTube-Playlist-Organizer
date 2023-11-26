# Use the official Python image as a parent image
FROM python:3.11.3-slim

# Set the working directory within the container
WORKDIR /app

# Copy your FastAPI application code into the container
COPY ./app.py /app

# Copy the .env file containing the API Key into the container 
COPY ./.env /app

# Copy the requirements.txt file into the container
COPY ./requirements.txt /app

# Install the Python dependencies
RUN pip install -r /app/requirements.txt

# Expose port 7860 for the FastAPI application
EXPOSE 7860

# Command to start the Streamlit app
CMD ["streamlit", "run", "--server.port", "7860", "app.py"]
