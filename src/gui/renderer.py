import pygame

class Renderer:
    def __init__(self, width, height, rows, cols):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols

        self.panel_width = 250
        self.screen = pygame.display.set_mode((width + self.panel_width, height))
        pygame.display.set_caption("RAHBARرہبر")

        self.cell_size = width // cols

        self.font = pygame.font.SysFont("consolas", 18)
        self.big_font = pygame.font.SysFont("consolas", 22, bold=True)
        self.buttons = {
            "A*": pygame.Rect(self.width + 20, 200, 200, 40),
            "GBFS": pygame.Rect(self.width + 20, 250, 200, 40),
            "Manhattan": pygame.Rect(self.width + 20, 300, 200, 40),
            "Euclidean": pygame.Rect(self.width + 20, 350, 200, 40),
            "Dynamic": pygame.Rect(self.width + 20, 400, 200, 40),
            "Clear": pygame.Rect(self.width + 20, 450, 200, 40),
        }
    def draw_grid(self, grid, path=None, visited=None):
        self.screen.fill((25, 25, 35))

        
        for r in range(self.rows):
            for c in range(self.cols):
                rect = pygame.Rect(
                    c * self.cell_size,
                    r * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )

                color = (40, 44, 60)

                if (r, c) in grid.walls:
                    color = (20, 20, 20)

                if visited and (r, c) in visited:
                    color = (90, 60, 140)

                if path and (r, c) in path:
                    color = (0, 200, 150)

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (50, 55, 75), rect, 1)

        
        panel_rect = pygame.Rect(self.width, 0, self.panel_width, self.height)
        pygame.draw.rect(self.screen, (30, 30, 45), panel_rect)

    def draw_panel(self, algo, heuristic, mode, metrics):
        x_offset = self.width + 20
        y = 30

        title = self.big_font.render("RAHBAR Control", True, (255, 255, 255))
        self.screen.blit(title, (x_offset, y))
        y += 50

        info_lines = [
            f"Algorithm: {algo}",
            f"Heuristic: {heuristic}",
            f"Mode: {mode}",
            "",
            f"Visited: {metrics['visited']}",
            f"Cost: {metrics['cost']:.2f}",
            f"Time: {metrics['time']:.2f} ms",
            "",
            "Controls:",
            "1 - A*",
            "2 - GBFS",
            "M - Manhattan",
            "E - Euclidean",
            "D - Toggle Dynamic",
            "SPACE - Run",
            "R - Random Map",
            "C - Clear"
        ]

        for line in info_lines:
            text = self.font.render(line, True, (200, 200, 220))
            self.screen.blit(text, (x_offset, y))
            y += 28
        for name, rect in self.buttons.items():
            pygame.draw.rect(self.screen, (50, 50, 80), rect)
            pygame.draw.rect(self.screen, (200, 200, 220), rect, 2)

            txt = self.font.render(name, True, (255, 255, 255))
            self.screen.blit(txt, (rect.x + 10, rect.y + 10))