from fastapi import HTTPException
from typing import List
from sodapy import Socrata
import pandas as pd

client = Socrata("data.wa.gov", None)

def fetch_vehicle_data(limit=2000):
    try:
        results = client.get("f6w7-q2d2", limit=limit)
        return pd.DataFrame.from_records(results)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching data from the external API")
