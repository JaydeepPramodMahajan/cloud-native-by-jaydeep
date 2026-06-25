from fastapi import FastAPI
from app.routers.tasks import router as task_router

app = FastAPI()


@app.get("/")
async def dashbord():
    return {"message": "This is the dashboard"}


@app.get("/health")
async def health_check():
    return {"Status": "Running Good"}


@app.get("/version")
async def check_version():
    return {"version": "1.0.0"}


app.include_router(task_router)  # It will add the routers in the main
