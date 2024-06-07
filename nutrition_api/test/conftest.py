import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.session import Base, get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./test/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Create a new database session with a rollback at the end of the test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def test_client(db_session):
    """Create a test client that uses the override_get_db fixture to return a session."""

    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def food_comp_test_obj():
    return {
        "id": "D000001-1234",
        "food_code": "D000001",
        "group_name": "음식",
        "food_name": "닭갈비",
        "research_year": 2019,
        "maker_name": "테스트 제조사",
        "ref_name": "테스트 출처",
        "serving_size": 100.0,
        "calorie": 250.0,
        "carbohydrate": 30.0,
        "protein": 10.0,
        "province": 5.0,
        "sugars": 15.0,
        "salt": 1.0,
        "cholesterol": 0.5,
        "saturated_fatty_acids": 1.0,
        "trans_fat": 0.0
    }

@pytest.fixture()
def food_comp_test_obj_update():
    return {
        "id": "D000001-1234",
        "research_year": 2022,
        "calorie": 300.0,
        "food_name": "업데이트된 닭갈비"
    }
