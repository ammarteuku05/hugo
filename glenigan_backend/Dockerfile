# Build stage (optional for dependencies if we want to be super strict, but slim is fine)
FROM python:3.11-slim

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY app/ ./app/
COPY scripts/ ./scripts/
# We copy the db only if it exists, or let compose handle it via volume
COPY glenigan.db . 

# Explicitly set PYTHONPATH
ENV PYTHONPATH=/app

# Create a non-root user and switch to it
RUN addgroup --system appgroup && adduser --system appuser --ingroup appgroup
RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000

CMD ["python", "app/main.py"]
