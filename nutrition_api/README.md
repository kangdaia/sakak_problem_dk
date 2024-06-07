# 식품영양성분 Rest API by FastAPI

## 실행방법

### 직접 실행방법

- `pipenv shell`
- `cd /nutrition_api`
- `python entrypoint.py`

### Docker 실행방법

#### docker image build

- `docker build -t my_fastapi_app .`

#### run docker container

- `docker run -d --name fastapi_app -p 8000:8000 my_fastapi_app`

### 테스트 코드 실행방법

- `pipenv shell`
- `cd /nutrition_api/app/test`
- `pytest`

### OpenAPI documentation
- [localhost:8000/docs](http://localhost:8000/docs) 로 접근해 확인할 수 있다

### 데이터 로드 방식

- excel 파일을 csv로 변환해서 /nutrition_api/app/db에 저장했다.
- /nutrition_api/app/loader.py를 동작시키면 sqlite db가 동일경로에 sample.db로 생성된다.
- 이미 sqlite db가 생성되어 있어 별도의 load는 필요하지 않다.
- (실행 원하면, 해당 경로에서 `python loader.py`를 실행하면 된다)

## 파일구조

```(text)
|  Dockerfile
│  entrypoint.py // 어플리케이션 uvicorn 실행 파일
│  Pipfile // python 가상환경 구성 정보 (pipenv)
│  Pipfile.lock
│  README.md
├─app //메인폴더
│  │  loader.py // db 구성 파일
│  │  main.py
│  │  sample.db
│  │  __init__.py
│  ├─api
│  │  │  __init__.py
│  │  ├─v1
│  │  │  │  food_comp.py // endpoint router 파일
│  │  │  │  __init__.py
│  ├─db
│  │  │  sample_data.csv // 주어진 excel 파일을 csv로 변환
│  │  │  session.py
│  │  │  __init__.py
│  ├─models
│  │  │  food_composition.py // 모델과 schema
│  │  │  __init__.py
│  ├─repositories
│  │  │  food_comp_crud.py // 레포지토리
│  │  │  __init__.py
└─test
    │  conftest.py
    │  test.db
    │  test_food_comp_api.py // 메인 테스트코드
    │  __init__.py
```

## 참고문서
- https://github.com/zhanymkanov/fastapi-best-practices?tab=readme-ov-file
- https://medium.com/@kacperwlodarczyk/fast-api-repository-pattern-and-service-layer-dad43354f07a
- https://lucky516.tistory.com/101
- https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
- https://velog.io/@mingming_eee/Fast-API-Day2
- https://blog.neonkid.xyz/252
- https://pytest-with-eric.com/pytest-advanced/pytest-fastapi-testing/
- https://fastapi.tiangolo.com/advanced/testing-database/