from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user = "phuser"
db_pw = "1q2w3e4r"
db_host = "localhost"
db_port = "3306"
db_name = "ph_db"

db_query = f"mysql+mysqlconnector://{db_user}:{db_pw}@{db_host}:{db_port}/{db_name}"

engine = create_engine(
    db_query, pool_recycle=14400
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
