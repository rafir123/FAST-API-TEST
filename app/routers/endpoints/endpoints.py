from fastapi import APIRouter, Query
from app.services.services import fetch_vehicle_data

router = APIRouter()

@router.get("/test_connection")
async def test_connection():
    return {"message": "Connection test successful!"}

@router.get("/vehicles", summary="Get vehicle count and average electric range by make for a given model year")
def get_vehicle_info_by_model_year(model_year: int = Query(..., description="Vehicle model year to filter")):
    # Fetch data from the API via services function
    vehicle_data = fetch_vehicle_data()

    # Filter data by model year
    filtered_data = vehicle_data[vehicle_data["model_year"] == str(model_year)]

    # Group data by vehicle make and aggregate
    if not filtered_data.empty:
        aggregated_data = (
            filtered_data.groupby("make")
            .agg(
                vehicle_count=("make", "size"),
                average_electric_range=("electric_range", "mean")
            )
            .reset_index()
        )
        # Return as JSON
        return aggregated_data.to_dict(orient="records")
    else:
        return {"message": "No data found for the specified model year"}