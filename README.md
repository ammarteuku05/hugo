# Glenigan Project Full-Stack Deployment

## Quick Start (Docker)

1. **Prerequisites**: Ensure you have Docker and Docker Compose installed.
2. **Launch**:
   ```bash
   docker-compose up --build
   ```
3. **Access**:
   - **Frontend**: [http://localhost:8080](http://localhost:8080)
   - **Backend API**: [http://localhost:8000/projects](http://localhost:8000/projects)

## Configuration

### Changing the API URL
If you deploy the services separately and need the frontend to point to a different API address, you can change the `BACKEND_URL` environment variable in the `docker-compose.yml` file:

```yaml
frontend:
  environment:
    - BACKEND_URL=http://your-custom-ip:8000
```
The frontend image will automatically inject this URL into the application logic at startup.

## Testing
Both services include comprehensive test suites with >75% code coverage.

- **Backend**: Python `pytest` (Unit & Integration tests).
- **Frontend**: `Karma` + `Jasmine` (Unit tests with Headless Chrome).

To run tests for each service, refer to their respective READMEs.

## Sub-Projects
- [Backend Documentation](./glenigan_backend/README.md)
- [Frontend Documentation](./glenigan_frontend/README.md)

