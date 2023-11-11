from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import databases
import sqlalchemy
import redis

# DB settings
DATABASE_URL = "postgresql://appple:poklmnji@localhost/fastapicache"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("content", sqlalchemy.String),
)

# connection Redis
redis_cache = redis.StrictRedis(host="localhost", port=6379, db=0)

app = FastAPI()


class NoteCreate(BaseModel):
    content: str