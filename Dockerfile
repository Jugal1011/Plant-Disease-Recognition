# Use a base image (e.g., Python, Node.js, etc.)
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install dependencies (if any)
RUN pip install -r requirements.txt

# Specify the command to run your application
CMD ["python", "app.py"]
