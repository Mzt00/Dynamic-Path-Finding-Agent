import random
def dynamic_obstacles(grid, current_path, agent_pos, goal, rows, cols, spawn_chance=0.10):
    if random.random() < spawn_chance:
        obs = (random.randint(0, rows-1), random.randint(0, cols-1))
        if obs != agent_pos and obs != goal and obs not in grid.walls:
            grid.toggle_wall(obs)
            if obs in current_path:
                return True, obs
            return False, obs
            
    return False, None

