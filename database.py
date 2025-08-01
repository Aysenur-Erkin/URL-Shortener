from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./urls.db"
engine = create_engine(DATABASE_URL, echo=False)

def init_db() -> None:
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
