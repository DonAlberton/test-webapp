from fastapi import FastAPI
import asyncio
import uuid
import logging

app = FastAPI()

assets: dict[str, int] = {}

@app.get("/")
def root():
    return {"response": "Hello world!"}

@app.post("/asset")
async def create_asset() -> dict[str, int]:
    id = str(uuid.uuid4())
    assets[id] = 5

    return {"asset_id": id}

@app.get("/asset/{asset_id}")
async def get_asset(asset_id: str) -> dict:
    if assets[asset_id] <= 0:

        reponse = {
            "asset_id": asset_id,
            "status": "processed" 
        }

        logging.info(f"Asset processed: {asset_id}")

        return reponse
    
    assets[asset_id] -= 1

    return {
        "asset_id": asset_id,
        "status": "unprocessed" 
    }

