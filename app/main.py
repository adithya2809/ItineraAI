from fastapi import FastAPI
from app.schemas import TripRequest, TripResponse
from fastapi.middleware.cors import CORSMiddleware
from app.trip_service import generate_trip_plan

app = FastAPI()


@app.post("/trip/generate/", response_model=TripResponse)
def generate_trip(trip: TripRequest):
    return generate_trip_plan(trip)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)