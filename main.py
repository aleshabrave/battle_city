from app.levels import parser

map = parser.parse_map("./levels/wall_level.txt")
print(map)
