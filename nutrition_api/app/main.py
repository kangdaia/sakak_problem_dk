from fastapi import FastAPI
import logging.config


logger = logging.getLogger("Nutrition Information API")
logger.info("START Application")


# Tags for representative endpoints
tags = [
    {
        "name": "users",
        "description": "Operations with users.",
    },
    {
        "name": "items",
        "description": "Manage items.",
        "externalDocs": {
            "description": "Items external docs - This is only for an example",
            "url": "https://anywhere.your.external.docs.is",
        },
    },
]


# Define Fast api and description
app = FastAPI(
    title="Nuturition Info API",
    description="This is an api for sakak coding test.",
    version="0.0.1",
    openapi_tags=tags,
)


# This path is for health check or test
@app.get("/")
async def root():
    return {"CONNECT"}
