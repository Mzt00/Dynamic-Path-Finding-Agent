import pygame
import sys
import random
from src.core.grid import Grid
from src.gui.renderer import Renderer
from src.algorithms.a_star import a_star_search
from src.algorithms.gbfs import gbfs_search
from src.algorithms.heuristics import manhattan, euclidean
from src.core.dynamic import dynamic_obstacles
from src.core.agent import Agent

def main():
    pygame.init()

    rows = cols = 25
    width = height = 600
    grid = Grid(rows, cols)
    renderer = Renderer(width, height, rows, cols)

    start = (2, 2)
    goal = (rows - 2, cols - 2)
    agent = Agent(start)

    current_algo = a_star_search
    current_heuristic = manhattan
    visited = []
    dynamic_mode = False
    clock = pygame.time.Clock()

    print("--- RAHBAR Operating Instructions ---")
    print("SPACE: Start Search/Move | R: Randomize Map | D: Toggle Dynamic Mode")
    print("1: A* | 2: GBFS | M: Manhattan | E: Euclidean | C: Clear All")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if pygame.mouse.get_pressed()[0]:
                m_pos = pygame.mouse.get_pos()
                c = m_pos[0] // renderer.cell_size
                r = m_pos[1] // renderer.cell_size
                if grid.is_in_bounds((r, c)) and (r, c) not in [start, goal]:
                    grid.toggle_walls((r, c))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: current_algo = a_star_search
                if event.key == pygame.K_2: current_algo = gbfs_search
                if event.key == pygame.K_m: current_heuristic = manhattan
                if event.key == pygame.K_e: current_heuristic = euclidean
                if event.key == pygame.K_d: dynamic_mode = not dynamic_mode
                
                if event.key == pygame.K_r:
                    grid.generate_random_walls(density=0.25)
                    visited, agent.pos, agent.path, agent.is_moving = [], start, [], False

                if event.key == pygame.K_c:
                    grid.walls.clear()
                    grid.nodes = [[0 for _ in range(cols)] for _ in range(rows)]
                    visited, agent.pos, agent.path, agent.is_moving = [], start, [], False

                if event.key == pygame.K_SPACE:
                    if not agent.is_moving:
                        temp = current_algo(grid, agent.pos, goal, current_heuristic)
                        agent.set_path(temp["path"])
                        visited = temp["visited"]
                        agent.is_moving = True

                        algo_name = "A*" if current_algo == a_star_search else "GBFS"
                        h_name = "Manhattan" if current_heuristic == manhattan else "Euclidean"
                        status = "DYNAMIC" if dynamic_mode else "STATIC"
                        title = f"RAHBAR | {algo_name}+{h_name} | {status} | Visited: {len(visited)} | Cost: {temp['cost']:.2f} | Time: {temp['time']:.2f}ms"
                        pygame.display.set_caption(title)

        if agent.is_moving:
            reached_goal = agent.move()

            if dynamic_mode:
                is_blocked, obs, pos = dynamic_obstacles(grid, agent.path, agent.pos, goal, rows, cols)

                if is_blocked:
                    new_plan = current_algo(grid, agent.pos, goal, current_heuristic)
                    agent.set_path(new_plan["path"])
                    visited.extend(new_plan["visited"])

            if reached_goal:
                agent.is_moving = False

        renderer.draw_grid(grid, path=agent.path, visited=visited)
        agent.draw(renderer.screen, renderer.cell_size)

        pygame.display.update()
        clock.tick(12)

if __name__ == "__main__":
    main()