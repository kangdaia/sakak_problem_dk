import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# CSV 파일 경로
csv_file_path = "db/sample_data.csv"  # 실제 파일 경로로 업데이트

# SQLite 데이터베이스 URL
database_url = "sqlite:///sample.db"

# SQLAlchemy 베이스 및 엔진 설정
Base = declarative_base()
engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind=engine, future=True)


class FoodComposition(Base):
    __tablename__ = "food_compositions"
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


# 테이블 생성
Base.metadata.create_all(engine)

# CSV 파일 읽기
df = pd.read_csv(csv_file_path)

# 필요한 컬럼만 선택하고, 컬럼 이름을 모델에 맞게 변경
df = df.rename(
    columns={
        "SAMPLE_ID": "id",
        "식품코드": "food_cd",
        "DB군": "group_name",
        "식품명": "food_name",
        "연도": "research_year",
        "지역 / 제조사": "maker_name",
        "성분표출처": "ref_name",
        "1회제공량": "serving_size",
        "에너지(㎉)": "calorie",
        "탄수화물(g)": "carbohydrate",
        "단백질(g)": "protein",
        "지방(g)": "province",
        "총당류(g)": "sugars",
        "나트륨(㎎)": "salt",
        "콜레스테롤(㎎)": "cholesterol",
        "총 포화 지방산(g)": "saturated_fatty_acids",
        "트랜스 지방산(g)": "trans_fat",
    }
)


# None case replacing
def convert_value(value):
    if value == "1g 미만":
        return 0
    if value == "-" or pd.isnull(value):
        return None
    try:
        return float(value)
    except ValueError:
        return value


df = df.applymap(convert_value)

# 데이터 삽입
with Session() as session:
    for index, row in df.iterrows():
        food_composition = FoodComposition(
            id=row["id"],
            food_cd=row["food_cd"],
            group_name=row["group_name"],
            food_name=row["food_name"],
            research_year=row["research_year"]
            if pd.notnull(row["research_year"])
            else None,
            maker_name=row["maker_name"],
            ref_name=row["ref_name"],
            serving_size=row["serving_size"]
            if pd.notnull(row["serving_size"])
            else None,
            calorie=row["calorie"] if pd.notnull(row["calorie"]) else None,
            carbohydrate=row["carbohydrate"]
            if pd.notnull(row["carbohydrate"])
            else None,
            protein=row["protein"] if pd.notnull(row["protein"]) else None,
            province=row["province"] if pd.notnull(row["province"]) else None,
            sugars=row["sugars"] if pd.notnull(row["sugars"]) else None,
            salt=row["salt"] if pd.notnull(row["salt"]) else None,
            cholesterol=row["cholesterol"] if pd.notnull(row["cholesterol"]) else None,
            saturated_fatty_acids=row["saturated_fatty_acids"]
            if pd.notnull(row["saturated_fatty_acids"])
            else None,
            trans_fat=row["trans_fat"] if pd.notnull(row["trans_fat"]) else None,
        )
        session.add(food_composition)
    session.commit()


print("Data has been successfully inserted into the SQLite database.")
