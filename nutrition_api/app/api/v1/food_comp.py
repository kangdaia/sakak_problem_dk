from fastapi import APIRouter, Depends, HTTPException
from app.models.food_composition import FoodCompositionBase
from app.repositories import food_comp_crud
from sqlalchemy.orm import Session
from db.session import get_db
from typing import List
import logging


router = APIRouter(prefix="/food_comp", tags=["food_composition"])
logger = logging.getLogger("sakak")


@router.get("/list", status_code=200, response_model=List[FoodCompositionBase])
async def get_items(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    logger.info("get all food composition items in list")
    food_data = food_comp_crud.get_food_compositions(db, skip=skip, limit=limit)
    return food_data


@router.get("/search", status_code=200, response_model=List[FoodCompositionBase])
async def search(
    food_name: str,
    research_year: str,
    maker_name: str,
    food_code: str,
    skip: int=0, 
    limit: int=100,
    db: Session = Depends(get_db),
):
    logger.info("search food composition items in condition")
    food_data = food_comp_crud.get_food_compositions_by_condition(
        db,
        food_name=food_name,
        research_year=research_year,
        maker_name=maker_name,
        food_code=food_code,
        skip=skip,
        limit=limit
    )
    return food_data
