import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.appointments import router as appointments_router

app = FastAPI(
    title="Clinic Management System API",
    description="RESTful API para la gestión de citas y terapias",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Aquí establecemos la ruta base que usted solicitó
app.include_router(appointments_router, prefix="/api/appointments", tags=["Appointments"])

@app.get("/")
def api_root():
    return {
        "service": "Clinic Management API - Active",
        "documentation": "/docs"
    }

@app.get("/health-check")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=4000, reload=True)
