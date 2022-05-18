from app.domain.level import Level
from app.levels import parser


class LevelGenerator:
    def generate(self) -> list[Level]:
        map_ = parser.parse_map("./levels/empty_level.txt")
        level = Level(map_)

        return [level]
