from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from support_cases.infrastructure.support_cases_routes import support_cases_router
from tracking.infrastructure.tracking_routes import tracking_router
from shared.infrastructure.http_error_handler import HTTPErrorHandler

app = FastAPI()

app.title = "Support Cases Tracking API"
app.description = "Support Cases Tracking API enables support case traceability"
app.version = "0.1.0"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app.add_middleware(HTTPErrorHandler)

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Support Cases Tracking API"}

app.include_router(support_cases_router, prefix="/support_cases", tags=["Support Cases"])
app.include_router(tracking_router, prefix="/tracking", tags=["Tracking"])
