from fastapi import FastAPI
import logging.config
from app.models import food_composition
from app.api.v1 import food_comp


logger = logging.getLogger("sakak")
logger.info("START Application")


# Tags for representative endpoints
tags = [
    {
        "name": "food_composition",
        "description": "manage the food composition information for various food",
    }
]


# Define Fast api and description
app = FastAPI(
    title="Nuturition Info API",
    description="This is an api for sakak coding test.",
    version="0.0.1",
    openapi_tags=tags,
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
)


app.include_router(food_comp.router, prefix="/api/v1/food_comp", tags=["food_composition"])


# This path is for health check or test
@app.get("/", summary="Health Check")
async def root():
    return {"CONNECT"}
