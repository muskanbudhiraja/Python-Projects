from fastapi import APIRouter

healthCheck=APIRouter()

@healthCheck.get("/health")
def CheckHealthStatus():
    return {"message": "Running Perfect!"}