from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.projects import router as projects_router

app = FastAPI(title="Glenigan Project API")

# Add CORS support
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins for the assessment task
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(projects_router, prefix="/projects", tags=["projects"])

@app.get("/")
def read_root():
    return {"message": "Glenigan Project API is running. Use /projects to access data."}

if __name__ == "__main__":


    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
