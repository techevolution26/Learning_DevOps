# Use the latest stable Python image from Docker Hub
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Copy the requirements.txt file into the container
COPY ./requirements.txt /app

# Create a virtual environment
RUN python -m venv /app/venv

# Upgrade pip inside the virtual environment (optional but recommended)
RUN /app/venv/bin/pip install --upgrade pip

# Install dependencies inside the virtual environment
RUN /app/venv/bin/pip install -r requirements.txt

# Make port 5000 available to the world outside the container
EXPOSE 5000

# Set environment variables for the virtual environment
ENV PATH="/app/venv/bin:$PATH"
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the application
CMD ["python", "app.py"]
