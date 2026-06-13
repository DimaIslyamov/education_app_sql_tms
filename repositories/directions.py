"""Репозиторий учебных направлений."""

from typing import Optional

from database.connection import Database
from models.entities import Direction
from repositories.base import require_lastrowid
from repositories.interfaces import IDirectionRepository


class DirectionRepository(IDirectionRepository):
    """CRUD-операции для направлений."""

    def __init__(self, db: Database) -> None:
        self._db = db

    def add(self, direction: Direction) -> int:
        """Добавить направление."""
        cursor = self._db.execute(
            "INSERT INTO directions (name, description) VALUES (?, ?)",
            (direction.name, direction.description),
        )
        return require_lastrowid(cursor)

    def get_by_id(self, direction_id: int) -> Optional[Direction]:
        """Получить направление по ID."""
        row = self._db.fetchone(
            "SELECT id, name, description FROM directions WHERE id = ?",
            (direction_id,),
        )
        if row is None:
            return None
        return Direction(id=row["id"], name=row["name"], description=row["description"])

    def get_all(self) -> list[Direction]:
        """Получить все направления."""
        rows = self._db.fetchall(
            "SELECT id, name, description FROM directions ORDER BY name",
        )
        return [
            Direction(id=row["id"], name=row["name"], description=row["description"])
            for row in rows
        ]

    def update(self, direction: Direction) -> bool:
        """Обновить направление."""
        if direction.id is None:
            return False
        cursor = self._db.execute(
            "UPDATE directions SET name = ?, description = ? WHERE id = ?",
            (direction.name, direction.description, direction.id),
        )
        return cursor.rowcount > 0

    def delete(self, direction_id: int) -> bool:
        """Удалить направление."""
        cursor = self._db.execute(
            "DELETE FROM directions WHERE id = ?",
            (direction_id,),
        )
        return cursor.rowcount > 0


if __name__ == "__main__":
    with Database() as db:
        repo = DirectionRepository(db)
        dir1 = Direction(id=None, name="прога")
        repo.add(dir1)
