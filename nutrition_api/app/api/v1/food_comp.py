from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.models.food_composition import FoodComposition, FoodCompositionBase, FoodCompositionUpdate, FoodCompositionCreate
from app.repositories import food_comp_crud
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import Annotated, List
import logging


router = APIRouter()
logger = logging.getLogger("sakak")


@router.get(
    "/search", 
    status_code=status.HTTP_200_OK, 
    response_model=List[FoodCompositionBase],
    summary="""전체 식품영양성분 목록에서 식품이름 혹은 연도(YYYY), 지역/제조사, 식품코드로 식품데이터를 찾는다."""
)
async def search_food_composition_items(
    food_name: Annotated[str | None, Query(max_length=50, example="닭갈비")] = None,
    research_year: Annotated[str | None, Query(regex=r'\d{4}', strict=True, example="2024")] = None,
    maker_name: Annotated[str | None, Query(max_length=50, example="전국(대표)")] = None,
    food_cd: Annotated[str | None, Query(max_length=7, example="D000000")] = None,
    skip: int=0, 
    limit: int=100,
    db: Session = Depends(get_db),
):
    logger.info("search food composition items in condition")
    return await food_comp_crud.get_food_compositions_by_condition(
        db,
        food_name=food_name,
        research_year=research_year,
        maker_name=maker_name,
        food_cd=food_cd,
        skip=skip,
        limit=limit
    )


@router.post(
    "/",
    response_model=FoodCompositionBase,
    status_code=status.HTTP_201_CREATED,
    summary="새로운 식품영양정보를 추가한다."
)
async def create_food_composition(
    food_composition_new=FoodCompositionCreate,
    db: Session = Depends(get_db)
):
    logger.info("create a food composition item")
    target = food_comp_crud.get_food_compositions_by_food_cd(db, food_cd=food_composition_new.food_cd)
    if target:
        raise HTTPException(status_code=400, detail="이미 존재하는 식품코드입니다.")
    food_composition = FoodComposition(**food_composition_new.dict())
    created_food_composition = food_comp_crud.create(db, new_obj=food_composition)
    return created_food_composition


@router.put(
    "/{food_cd}",
    status_code=status.HTTP_200_OK,
    summary="식품코드로 해당 영양정보를 업데이트한다."
)
async def update_food_composition(
    food_composition_in: FoodCompositionUpdate,
    food_cd: Annotated[str, Query(max_length=7, example="D000000")],
    db: Session = Depends(get_db)
):
    logger.info("update food composition items by food_cd")
    target = food_comp_crud.get_food_compositions_by_food_cd(db, food_cd=food_cd)
    if not target:
        raise HTTPException(status_code=404, detail="존재하지 않는 식품 영양정보입니다.")
    update_data = food_composition_in.dict(exclude_unset=True)
    return await food_comp_crud.update_food_composition(db, fc_obj=target, update_obj=update_data)


@router.delete(
    "/{food_cd}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="식품코드로 해당 영양정보를 삭제한다."
)
async def delete_food_compostion(
    food_cd: Annotated[str, Query(max_length=7, example="D000000")], 
    db: Session = Depends(get_db)
):
    logger.info("delete food composition items by food_cd")
    target = food_comp_crud.get_food_compositions_by_food_cd(db, food_cd=food_cd)
    if not target:
        raise HTTPException(status_code=404, detail="존재하지 않는 식품 영양정보입니다.")
    food_comp_crud.delete_food_composition_by_food_cd(db, food_cd=food_cd)
    return None
