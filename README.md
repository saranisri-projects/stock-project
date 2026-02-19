Stock Education Platform

Full-stack stock analysis tool built with:

- FastAPI (Backend)
- React (Frontend)
- Twelve Data API
- Predictive trendline analysis

## How to Run

### Backend
cd backend
python -m uvicorn app.main:app --reload

### Frontend
cd frontend
npm install
npm run dev

## Environment Variables

Create a `.env` file in backend:

TWELVE_DATA_API_KEY=your_api_key_here
