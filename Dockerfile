# Small base image (very important for <200MB)
FROM python:3-alpine

# Make Python output show immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create required output folder inside container
RUN mkdir -p /home/data/output

# Copy your two text files into /home/data inside container
COPY data/ /home/data/

# Copy your python script into container
COPY scripts/script.py /scripts/script.py

# Run script automatically when container starts
CMD ["python", "/scripts/script.py"]