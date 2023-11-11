from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import databases
import sqlalchemy

# DB settings
DATABASE_URL = "postgresql://apple:poklmnji@localhost/fastapicache"
database = databases.Database(DATABASE_URL)

app = FastAPI()

class NoteCreate(BaseModel):
    content: str

notes = sqlalchemy.Table(
    "notes",
    sqlalchemy.MetaData(),
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("content", sqlalchemy.String),
)

#api development

@app.get("/notes/", response_model=list)
async def read_notes(skip: int = 0, limit: int = 10):
    query = notes.select().offset(skip).limit(limit)
    result = await database.fetch_all(query)
    return result

@app.post("/notes/", response_model=dict)
async def create_note(note: NoteCreate):
    query = notes.insert().values(content=note.content)
    last_record_id = await database.execute(query)
    return {"id": last_record_id, **note.dict()}
