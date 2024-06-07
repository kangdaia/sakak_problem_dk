import logging

from app.models.food_composition import FoodComposition, FoodCompositionCreate
from sqlalchemy.orm import Session


logger = logging.getLogger("sakak")


def get_food_compositions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(FoodComposition).offset(skip).limit(limit).all()


async def get_food_compositions_by_condition(
    db: Session,
    food_name: str,
    research_year: str,
    maker_name: str,
    food_code: str,
    skip: int = 0,
    limit: int = 100,
):
    return (
        db.query(FoodComposition)
        .offset(skip)
        .limit(limit)
        .filter(
            FoodComposition.food_name == food_name,
            FoodComposition.research_year == research_year,
            FoodComposition.maker_name == maker_name,
            FoodComposition.food_code == food_code,
        )
        .all()
    )
