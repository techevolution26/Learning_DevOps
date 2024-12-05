# Use the latest stable Python image from Docker Hub
FROM python:latest

# Set the working directory in the container
WORKDIR /app

COPY ./app /app

# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app

# Create a virtual environment
RUN python -m venv /venv

# Upgrade pip inside the virtual environment (optional)
RUN /venv/bin/pip install --upgrade pip

# Install dependencies inside the virtual environment
RUN /venv/bin/pip install -r requirements.txt

# Make port 5000 available to the world outside the container
EXPOSE 5000

# Set environment variables
ENV PATH="/venv/bin:$PATH"
ENV NAME World

# Run the application
CMD ["python", "app.py"]
