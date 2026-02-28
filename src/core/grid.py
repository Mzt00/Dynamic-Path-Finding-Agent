import random

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.nodes = [[0 for _ in range(cols)] for _ in range(rows)]
        self.walls = set()

    def is_in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_passable(self, pos):
        return pos not in self.walls

    def get_neighbours(self, pos):
        r, c = pos

        temp = [
            (r, c+1), (r, c-1),
            (r+1, c), (r-1, c),
            (r-1, c-1), (r-1, c+1),
            (r+1, c+1), (r+1, c-1)
        ]

        neighbours = [
            p for p in temp
            if self.is_in_bounds(p) and self.is_passable(p)
        ]

        return neighbours

    def generate_walls(self, density=0.2):
        self.walls.clear()
        self.nodes = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                if random.random() < density:
                    self.walls.add((r, c))
                    self.nodes[r][c] = 1

    def toggle_walls(self, pos):
        r, c = pos

        if pos in self.walls:
            self.walls.remove(pos)
            self.nodes[r][c] = 0
        else:
            self.walls.add(pos)
            self.nodes[r][c] = 1