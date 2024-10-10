import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Data model for the incoming JSON data
class LocationData(BaseModel):
    id: str
    name: str
    longitude: float
    latitude: float
    floor: int

# In-memory storage for received data (you can replace this with a database in the future)
location_data_store = []

@app.post("/submit-data")
async def submit_data(data: LocationData):
    try:
        # Append the data to the in-memory list
        location_data_store.append(data)

        # Return a success response
        return {"message": "Data received successfully"}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/get-data")
async def get_data():
    # Return the in-memory data as JSON
    return location_data_store

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
