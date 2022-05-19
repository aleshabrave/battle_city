from app.domain.level import Level
from app.levels import parser


class LevelGenerator:
    def generate(self) -> list[Level]:
        levels = []
        for i in range(3):
            levels.append(Level(parser.parse_map(f"./levels/level_{i}.txt")))

        return levels
