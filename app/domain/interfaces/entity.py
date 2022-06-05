from dataclasses import dataclass
from typing import Optional

from app.domain.utils import Size, Vector


@dataclass
class Entity:
    """Class for entity."""

    name: str
    position: Optional[Vector]
    size: Optional[Size]
