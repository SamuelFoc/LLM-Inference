# Use a Python base image with GPU support (if needed)
FROM nvidia/cuda:11.8.0-base-ubuntu22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip git curl && \
    apt-get clean

# Set Python as the default
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install Python libraries
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose API port
EXPOSE 5000

# Set working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Run FastAPI server
CMD ["uvicorn", "run_model:app", "--host", "0.0.0.0", "--port", "5000"]
