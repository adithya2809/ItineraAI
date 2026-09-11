from app.schemas import TripRequest,TripResponse
from fastapi import HTTPException,status
from app.gemini_client import client

def generate_trip_plan(trip:TripRequest):
    prompt=f"""You are an AI travel planner.

    Plan a {trip.days}-day trip from {trip.origin} to {trip.destination} including {trip.persons} person(s) in the trip.

    The traveler's budget is ₹{trip.budget} per person.The budget provided is per person. 
    Calculate the itinerary costs for the entire group of {trip.persons} people, 
    and return all transportation and activity costs as the estimated total cost for the entire group.

    Their interests are: {", ".join(trip.interests)}.

    Organize the itinerary by day, with morning,
    afternoon, and evening activities.
    For every activity, include an estimated cost in Indian rupees.
    
    Include the estimated transportation cost for traveling from the origin to the destination.
    Return the transportation details with:
    - mode of transport
    - description
    - estimated cost in Indian rupees
    Keep the itinerary realistic and concise.
    """
    try:
        response=client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config={
            "response_mime_type":"application/json",
            "response_schema":TripResponse
        }
         )
        trip_response=TripResponse.model_validate_json(response.text)
        total_cost=sum(
            activity.cost
            for day in trip_response.itinerary
            for activity in day.activities
        )
        total_cost+=trip_response.transportation.cost

        total_budget=trip.budget*trip.persons
        if total_cost > total_budget:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Generated trip exceeds the requested budget"
            )
        if trip.days > 30:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail="Trip duration cannot exceed 30 days"
            )
    except HTTPException:
        raise
    except Exception as e:
        print("Gemini Error:",e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate Trip"
        ) 
    return trip_response