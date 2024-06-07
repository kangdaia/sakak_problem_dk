from sqlalchemy import Column, Integer, String, Float
from app.db.session import Base
from pydantic import BaseModel, Field, field_validator
from typing import Optional

class FoodComposition(Base):
    __tablename__ = 'food_compositions'
    id = Column(String, primary_key=True)
    food_code = Column(String)
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
    food_code: Optional[str] = Field(None, description="식품코드")
    group_name: Optional[str] = Field(None, description="식품군")
    food_name: Optional[str] = Field(None, description="식품이름")
    research_year: Optional[int] = Field(None, description="조사년도")
    maker_name: Optional[str] = Field(None, description="지역/제조사")
    ref_name: Optional[str] = Field(None, description="자료출처")
    serving_size: Optional[float] = Field(None, description="1회 제공량")
    calorie: Optional[float] = Field(None, description="열량(kcal)(1회제공량당)")
    carbohydrate: Optional[float] = Field(None, description="탄수화물(g)(1회제공량당)")
    protein: Optional[float] = Field(None, description="단백질(g)(1회제공량당)")
    province: Optional[float] = Field(None, description="지방(g)(1회제공량당)")
    sugars: Optional[float] = Field(None, description="총당류(g)(1회제공량당)")
    salt: Optional[float] = Field(None, description="나트륨(g)(1회제공량당)")
    cholesterol: Optional[float] = Field(None, description="콜레스테롤(g)(1회제공량당)")
    saturated_fatty_acids: Optional[float] = Field(None, description="포화지방산(g)(1회제공량당)")
    trans_fat: Optional[float] = Field(None, description="트랜스지방(g)(1회제공량당)")

    class Config:
        from_attributes = True

    @field_validator('research_year')
    def validate_research_year(cls, value):
        if int(value) is not None and (int(value) < 1900 or int(value) > 2100):
            raise ValueError('research_year must be between 1900 and 2100')
        return value


class FoodCompositionCreate(FoodCompositionBase):
    food_code: str

class FoodCompositionUpdate(FoodCompositionBase):
    pass
