from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()
engine = create_engine("sqlite:///team.db")
base = declarative_base()

class TeamMember(base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    level = Column(Integer)
    type = Column(String)

base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



class TeamMemberCreate(BaseModel):
    name: str
    level: int
    type: str

@app.get("/")
def greet():
    return {"message": "Hello World"}

@app.get("/team/{poke_num}")
def get_team_poke(poke_num: int):
    return {"id": poke_num, "name": "pikachu", "level": 5}

@app.post("/team")
def add_poke(poke: TeamMemberCreate, db=Depends(get_db)):
    db_poke = TeamMember(name=poke.name, level=poke.level, type=poke.type)
    db.add(db_poke)
    db.commit()
    db.refresh(db_poke)
    return db_poke  