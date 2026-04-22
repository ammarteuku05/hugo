# ==============================
# Stage 1: Build dependencies
# ==============================
FROM python:3.11-alpine AS build-stage

WORKDIR /app

# Only install what's needed to compile Python packages
RUN apk add --no-cache gcc musl-dev python3-dev

COPY requirements.txt .
# Install into a custom location so we can copy cleanly
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ==============================
# Stage 2: Production runtime
# ==============================
FROM python:3.11-alpine

# Prevents Python from writing pyc files or buffering output
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

# Copy only the installed packages from the build stage (no compilers)
COPY --from=build-stage /install /usr/local

# Copy project files (cache-bust: v2 - updated repository schema)
COPY app/ ./app/
COPY glenigan_takehome_FS.db ./glenigan_takehome_FS.db

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup \
    && chown -R appuser:appgroup /app
USER appuser

EXPOSE 8000

CMD ["python", "app/main.py"]
