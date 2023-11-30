# Use the official Python image as a parent image
FROM python:3.11.3-slim

# Set the working directory within the container
WORKDIR /app

# Create a directory for storing documents
RUN mkdir /app/documents

# Copy the .env file containing the API Key into the container 
COPY ./.env /app/.env

# Copy the banner image into the Docker container
COPY ./main.jpg /app/main.jpg

# Copy your FastAPI application code into the container
COPY ./app.py /app/app.py

# Copy the requirements.txt file into the container
COPY ./requirements.txt /app/requirements.txt

# Install the Python dependencies
RUN pip install -r /app/requirements.txt

# Adjust permissions on the /app directory
RUN chmod -R 777 /app

# Expose port 7860 for the FastAPI application
EXPOSE 7860

# Command to start the Streamlit app
CMD ["streamlit", "run", "--server.port", "7860", "app.py"]