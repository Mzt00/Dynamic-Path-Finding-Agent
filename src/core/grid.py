import random

class Grid:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        #here a grid is being initialized
        #0 means empty, and 1 means wall
        self.nodes = set()
        
    def is_in_bounds(self,pos):
        (r,c)=pos
        return 0<=r < self.rows and 0<= c < self.cols
    
    def is_passable(self):
        return self.pos not in walls 
    
    def get_neighbours(self,pos):
        (r, c) = pos
        #8 way movemnet up/down/left/right/diagonals 
        #has been implemented
        temp = [(r,c+1),(r,c-1),(r+1,c),(r-1,c),(r-1,c-1),(r-1,c+1),(r+1,c+1),(r+1,c-1)]
        #temp stores all the possible neigbours a position can have
        neighbours = [p for p in temp if self.is_in_bounds(p) and self.is_passable(p)]
        return neighbours 
    def generate_walls(self,density=0.2):
        #density referss to amount of grid
        #(out of 1) will be the walls
        #by default it is 20%
        self.walls.clear()  
        self.nodes = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                if random.random()< density:
                    self.walls.add(r,c)
                    self.nodes[r][c]=1
                    
    def toggle_walls(self,pos):
        #this function would allow a user
        #to add/remove a wall
        if pos in self.walls:
            self.walls.remove(pos)
            self.nodes[pos[0][pos[1]]] = 0
        else:
            self.nodes[pos[0][pos[1]]] = 1
                