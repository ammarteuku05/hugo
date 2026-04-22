# Glenigan Project Frontend

## ⚡ Quick Start (Recommended: Docker)
Use the `docker-compose.yml` in the project root to run both frontend and backend together:
```bash
docker compose up --build
```
The frontend will be available at [http://localhost:8080](http://localhost:8080).

> [!NOTE]
> The `dist/` folder is **not committed to Git** — it is automatically generated inside the Docker container during the build. You do **not** need to build or commit it manually when using Docker.

---

## 🛠 Running Locally (Without Docker)

If you need to run the frontend outside of Docker, you must compile the TypeScript source first:

### 1. Install Dependencies
```bash
npm install
```

### 2. Build (Compile TypeScript → `dist/app.js`)
```bash
npm run build
```
This generates the `dist/app.js` file required by `index.html`.

### 3. Serve the Frontend
Since this is a static web app, use any local server:

**Python (built-in):**
```bash
python3 -m http.server 8080
```

**Node.js live-server:**
```bash
npx live-server
```

### 4. API Connection
For local development, the app defaults to `http://localhost:8000` when `window.API_BASE_URL` is not set. No code change is required for the standard local setup.

In Docker, `entrypoint.sh` replaces the `__BACKEND_URL_PLACEHOLDER__` token at container startup using the `BACKEND_URL` environment variable.

---

## 🧪 Running Tests
```bash
npm install
npm test
```

## 🐳 Docker Usage (Standalone)
```bash
docker build -t glenigan-frontend .
docker run -p 8080:80 -e BACKEND_URL=http://your-api-url:8000 glenigan-frontend
```