from sqlalchemy import Column, Integer, String, Float
from db.session import Base
from pydantic import BaseModel
from typing import Optional

class FoodComposition(Base):
    __tablename__ = 'food_compositions'
    id = Column(String, primary_key=True)
    food_cd = Column(String)
    group_name = Column(String)
    food_name = Column(String)
    research_year = Column(Integer)
    maker_name = Column(String)
    ref_name = Column(String)
    serving_size = Column(Float)
    calorie = Column(Float)
    carbohydrate = Column(Float)
    protein = Column(Float)
    province = Column(Float)
    sugars = Column(Float)
    salt = Column(Float)
    cholesterol = Column(Float)
    saturated_fatty_acids = Column(Float)
    trans_fat = Column(Float)


class FoodCompositionBase(BaseModel):
    id: str
    food_cd: Optional[str]
    group_name: Optional[str]
    food_name: Optional[str]
    research_year: Optional[int]
    maker_name: Optional[str]
    ref_name: Optional[str]
    serving_size: Optional[float]
    calorie: Optional[float]
    carbohydrate: Optional[float]
    protein: Optional[float]
    province: Optional[float]
    sugars: Optional[float]
    salt: Optional[float]
    cholesterol: Optional[float]
    saturated_fatty_acids: Optional[float]
    trans_fat: Optional[float]


class FoodCompositionCreate(FoodCompositionBase):
    pass