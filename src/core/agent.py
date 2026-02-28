import pygame
class Agent:
    def __init__(self,start_pos):
        self.pos = start_pos 
        self.path = []
        self.is_moving = False
        
    def set_path(self, path):
        self.path = list(path)

        if self.path and self.path[0] == self.pos:
            self.path.pop(0)
        self.is_moving = bool(self.path)
        
    def move(self):
        if self.path:
            self.pos = self.path.pop(0)
            if not self.path:
                self.is_moving = False
                return True 
        return False
    
    def draw(self, screen, cell_size):
        r, c = self.pos
        center = (
        c * cell_size + cell_size // 2,
        r * cell_size + cell_size // 2
        )

        pygame.draw.circle(screen, (0, 0, 255), center, cell_size // 3)
        
    
