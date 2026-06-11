from database.connection import Database

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS directions (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL UNIQUE,
    description TEXT    NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS teachers ( 
    id	INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name	TEXT 	NOT NULL,
    last_name	TEXT	NOT NULL,
    email	    TEXT	NOT NULL,
    phone   	TEXT	NOT NULL
);
"""

def init_schema(db: Database) -> None:
    """Создать таблицы, если они ещё не существуют."""
    db.connect().executescript(SCHEMA_SQL)
    db.connect().commit()

if __name__ == "__main__":
    with Database() as db:
        init_schema(db)

