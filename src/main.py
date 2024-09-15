from fastapi import FastAPI
from support_cases.infrastructure.support_cases_routes import support_cases_router
from tracking.infrastructure.tracking_routes import tracking_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Support Case Tracking API"}

app.include_router(support_cases_router, prefix="/support_cases")
app.include_router(tracking_router, prefix="/tracking")
