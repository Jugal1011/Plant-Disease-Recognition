FROM python:3.9

# Set working directory
WORKDIR /app

# Install OpenCV dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download model if needed (or skip if already in ./model/)
RUN python download_model.py

# Expose the default Flask port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
