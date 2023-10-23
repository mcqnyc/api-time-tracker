import os
import databases
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = "sqlite:///data.db"

metadata = sqlalchemy.MetaData()

task_table = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.Integer),
    sqlalchemy.Column("description", sqlalchemy.String(256)),
    sqlalchemy.Column("start_time", sqlalchemy.DateTime),
    sqlalchemy.Column("end_time", sqlalchemy.DateTime),
)

# engine = sqlalchemy.create_engine(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
database = databases.Database(DATABASE_URL)
