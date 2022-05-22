from dataclasses import dataclass

from app.domain.interfaces.entity import Entity
from app.domain.interfaces.living import Living


@dataclass(unsafe_hash=True)
class Block(Living, Entity):
    """Класс блока."""
