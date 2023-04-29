# ph-backend

## Envs
- Python 3.8.12
- mysql 5.7
- Service dockerize
- DB Table은 DLL로
- Pytest TDD
- API response - custom response json, except 204
- Login Auth Method : JWT

## Arch
- src
  - models: DAO, Model 소스
  - routers: FastAPI app 구성, endpoint 구성 
  - services: 비즈니스 로직 수행
- tests: Pytest, 단위 테스트 코드

## Virtual env
~~~  
pip install pipenv  
pipenv --python 3.8.12  
pipenv sync  
./run  
~~~ 
Docker
~~~
docker build --tag ${name} .
docker run -d --name ${name} -p 8080:${service port} ${container}
~~~

