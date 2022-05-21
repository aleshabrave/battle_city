from dataclasses import dataclass

from app.domain.interfaces.entity import Entity
from app.domain.interfaces.living import Living


@dataclass
class Block(Living, Entity):
    """Класс блока."""
