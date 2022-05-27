from dataclasses import dataclass
from typing import Optional

from app.domain.utils import Size, Vector


@dataclass
class Entity:
    """Абстрактный класс сущности."""

    name: str
    position: Optional[Vector]
    size: Optional[Size]
