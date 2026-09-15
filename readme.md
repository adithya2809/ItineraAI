# ItineraAI

An AI-powered trip planner that creates personalized travel itineraries based on the user's origin, destination, trip length, group size, budget, and interests.

## Overview

ItineraAI uses the Google Gemini API to generate a structured, day-by-day trip plan with:

- transportation suggestions
- estimated costs
- activity recommendations
- budget validation
- itinerary planning tailored to user interests

The frontend is built with React, and the backend is built with FastAPI. Requests are validated with Pydantic before the trip is generated.

## Features

- Personalized itinerary generation
- Interest-based activity suggestions
- Group-aware budget calculation
- Transportation planning and cost estimation
- Frontend and backend validation
- Error handling for invalid inputs and API failures

## Tech Stack

### Frontend
- React
- Vite
- JavaScript
- CSS

### Backend
- Python
- FastAPI
- Pydantic
- Google Gemini API

## Project Structure

```text
Project_AI_TRIP_PLANNER/
├── app/
│   ├── gemini_client.py
│   ├── main.py
│   ├── schemas.py
│   └── trip_service.py
├── react-frontend/
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
├── .env
├── .gitignore
├── requirements.txt
├── readme.md
└── .venv/
```

### Key files
- [app/main.py](app/main.py): FastAPI app and route definitions
- [app/schemas.py](app/schemas.py): request and response models
- [app/gemini_client.py](app/gemini_client.py): Gemini client setup
- [app/trip_service.py](app/trip_service.py): trip generation and validation logic
- [react-frontend/src/App.jsx](react-frontend/src/App.jsx): frontend form and itinerary rendering

## Prerequisites

Before running the project, make sure you have:

- Python 3.10+
- Node.js and npm
- A Google Gemini API key

## Environment Setup

Create a `.env` file in the project root and add your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit your `.env` file to GitHub.

## Backend Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

2. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

3. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

## Frontend Setup

1. Open a new terminal and go to the frontend folder:

```bash
cd react-frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the React app:

```bash
npm run dev
```

The frontend will usually run at:

```text
http://localhost:5173
```

## API Endpoint

### Generate trip plan

```http
POST /trip/generate/
```

### Example request body

```json
{
  "origin": "Hyderabad",
  "destination": "Goa",
  "days": 3,
  "persons": 2,
  "budget": 20000,
  "interests": ["beaches", "food", "shopping"]
}
```

### Notes
- `budget` is the per-person budget.
- The backend checks the total estimated cost against the full group budget.

## How It Works

1. The user enters trip details in the React frontend.
2. The frontend validates required inputs.
3. The JSON is sent to the FastAPI backend.
4. The backend builds a Gemini prompt using the trip data.
5. Gemini returns a structured itinerary.
6. Pydantic validates the response.
7. Business rules check budget and duration constraints.
8. The final itinerary is returned to the frontend and rendered.

![Working Screenshots](./Working%20Screenshots/Screenshot%202026-09-11%20165609.png,./Working%20Screenshots\Screenshot%202026-09-11%20170334.png,./Working%20Screenshots\Screenshot%202026-09-11%20170544.png,./Working%20Screenshots\Screenshot%202026-09-11%20170820.png,./Working%20Screenshots\Screenshot%202026-09-11%20171010.png)
## Error Handling

The app handles common validation and runtime issues such as:

- empty or invalid form inputs
- trip duration above allowed limit
- total trip cost exceeding the request budget
- Gemini API or backend failure

## Future Improvements

- save trip history
- login and user accounts
- export/share trip plans
- map and weather integration
- more detailed cost breakdowns
- favorites and saved itineraries

## License

This project is for educational/demo use unless a separate license is added.
