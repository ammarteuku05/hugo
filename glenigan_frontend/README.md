# Glenigan Project Frontend
## Docker Usage

1. **Build the Image**:
   ```bash
   docker build -t glenigan-frontend .
   ```

2. **Run the Container**:
   ```bash
   docker run -p 8080:80 -e BACKEND_URL=http://your-api-url:8000 glenigan-frontend
   ```
   *Note: Using the Docker Compose file in the root is recommended for full stack deployment.*

## Setup & Running

### 1. Build (Transpile TypeScript)
If you have `tsc` installed, you can compile the source:
```bash
npm install
npm run build
```
```
Note: A pre-compiled `dist/app.js` is included for convenience.

### 2. Running Tests
The frontend uses `Jasmine` as the test framework and `Karma` as the test runner.

1. **Install Test Dependencies**:
   ```bash
   npm install
   ```

2. **Run Tests**:
   ```bash
   npm test
   ```

### 3. Serving the Frontend
Since the frontend is a static web application, you can serve it using any web server. Examples:

**Using Python's built-in server:**
```bash
python3 -m http.server 8080
```

**Using Node.js `live-server`:**
```bash
npx live-server
```

### 4. API Connection
By default, the frontend expects the backend API to be available at `http://0.0.0.0:8000/projects`. You can update the `API_BASE_URL` in `src/app.ts` if your backend is running on a different address.