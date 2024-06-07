import logging
from typing import Optional

from app.models.food_composition import FoodComposition, FoodCompositionCreate
from sqlalchemy.orm import Session


logger = logging.getLogger("sakak")


def get_food_compositions_by_food_cd(db: Session, food_cd: str):
    return db.query(FoodComposition).filter(FoodComposition.food_cd == food_cd).first()


async def get_food_compositions_by_condition(
    db: Session,
    food_name: Optional[str],
    research_year: Optional[str],
    maker_name: Optional[str],
    food_cd: Optional[str],
    skip: int = 0,
    limit: int = 100,
):
    query = db.query(FoodComposition)
    if food_name:
        query = query.filter(FoodComposition.food_name == food_name)
    if research_year:
        query = query.filter(FoodComposition.research_year == int(research_year))
    if maker_name:
        query = query.filter(FoodComposition.maker_name == maker_name)
    if food_cd:
        query = query.filter(FoodComposition.food_cd == food_cd)
    result = query.offset(skip).limit(limit).all()
    return result if result else []


async def create_food_composition(db: Session, new_obj: FoodCompositionCreate):
    db_food_composition = FoodComposition(**new_obj.model_dump())
    db.add(db_food_composition)
    db.commit()
    db.refresh(db_food_composition)
    return db_food_composition


async def update_food_composition(db: Session, fc_obj: FoodComposition, update_obj: dict):
    for key, value in update_obj.items():
        setattr(fc_obj, key, value)
    db.add(fc_obj)
    db.commit()
    db.refresh(fc_obj)
    return fc_obj


async def delete_food_composition_by_food_cd(db: Session, food_composition: FoodComposition):
    db.delete(food_composition)
    db.commit()
