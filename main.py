import databases
import sqlalchemy
import redis

# Настройки базы данных
DATABASE_URL = "postgresql://appple:poklmnji@localhost/fastapicache"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("content", sqlalchemy.String),
)