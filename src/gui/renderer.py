import pygame 
WHITE  = (255, 255, 255) # Empty
BLACK  = (0, 0, 0) # Wall
GREEN  = (0, 255, 0)# Final Path
RED    = (255, 0, 0)# Visited Nodes
YELLOW = (255, 255, 0)# Frontier
BLUE   = (0, 0, 255)# Start/Goal

class Renderer:
    def __init__(self,width,height,rows,cols):
        self.cell_size = width // cols
        self.screen = pygame.display.set_mode((width,height + 100))
        pygame.display.set_caption("RAHBARرہبر")
    
    def draw_grid(self,grid,path=[],visited=[]):
        self.screen.fill(WHITE)
        #draw visited nodes
        for node in visited:
            r, c = node
            pygame.draw.rect(self.screen, RED, (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size))
            #draw walls
        for r in range(grid.rows):
            for c in range(grid.cols):
                if grid.nodes[r][c] == 1:
                    pygame.draw.rect(self.screen, BLACK, (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size))
                    #draw path
        for node in path:
            r, c = node
            pygame.draw.rect(self.screen, GREEN, (c * self.cell_size, r * self.cell_size, self.cell_size, self.cell_size))
        #draw grid lines
        for i in range(grid.cols + 1):
            pygame.draw.line(self.screen, BLACK, (i * self.cell_size, 0), (i * self.cell_size, grid.rows * self.cell_size))
        for i in range(grid.rows + 1):
            pygame.draw.line(self.screen, BLACK, (0, i * self.cell_size), (grid.cols * self.cell_size, i * self.cell_size))

        pygame.display.update()
