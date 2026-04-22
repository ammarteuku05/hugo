# Glenigan Project API (Backend)
## Setup & Installation

1. **Prerequisites**:
   - Python 3.8+
   - pip

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Service

Start the FastAPI server using Uvicorn:
```bash
export PYTHONPATH=$PYTHONPATH:.
python3 app/main.py
```
The API will be available at `http://localhost:8000`.

> [!TIP]
> Run `python3 scripts/seed_db.py` before starting the service if you need to recreate sample data.

## Running Tests

The backend uses `pytest` and `pytest-cov` for testing and coverage.

1. **Install Test Dependencies**:
   ```bash
   pip install pytest pytest-cov httpx
   ```

2. **Run Tests**:
   ```bash
   export PYTHONPATH=$PYTHONPATH:.
   python3 -m pytest --cov=app tests/ --cov-report=term-missing
   ```

## API Endpoints


- `GET /projects`: List construction projects.
  - Query Params:
    - `area`: Filter by region.
    - `keyword`: Search project names.
    - `page`: Pagination page number.
    - `per_page`: Records per page.
- `GET /`: Health check.

## Docker Usage

1. **Build the Image**:
   ```bash
   docker build -t glenigan-backend .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 8000:8000 -v glenigan_data:/app/data -e DATABASE_PATH=/app/data/glenigan_takehome_FS.db glenigan-backend
   ```
