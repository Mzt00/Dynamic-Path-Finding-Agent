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
    selected_algo = "A*"
    selected_distance = "Manhattan"
    visited = []
    dynamic_mode = False
    clock = pygame.time.Clock()
    metrics = {"visited": 0, "cost": 0, "time": 0}
    print(" RAHBARرہبر Operating Instructions ")
    print("SPACE: Start Search/Move | R: Randomize Map | D: Toggle Dynamic Mode")
    print("1: A* | 2: GBFS | M: Manhattan | E: Euclidean | C: Clear All")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for name, rect in renderer.buttons.items():
                    if rect.collidepoint(pos):

                        if name in ["A*", "GBFS"]:
                            selected_algo = name

                        elif name in ["Manhattan", "Euclidean"]:
                            selected_distance = name

                        elif name == "Dynamic":
                            dynamic_mode = not dynamic_mode

                        elif name == "Clear":
                            grid.walls.clear()
                            grid.nodes = [[0 for _ in range(cols)] for _ in range(rows)]
                            visited, agent.pos, agent.path, agent.is_moving = [], start, [], False

                        elif name == "Start" and not agent.is_moving:

                            algo_func = a_star_search if selected_algo == "A*" else gbfs_search
                            heuristic = manhattan if selected_distance == "Manhattan" else euclidean

                            temp = algo_func(grid, agent.pos, goal, heuristic)
                            agent.set_path(temp["path"])
                            visited = temp["visited"]
                            agent.is_moving = True

                            metrics["visited"] = len(temp["visited"])
                            metrics["cost"] = temp["cost"]
                            metrics["time"] = temp["time"]

                c = pos[0] // renderer.cell_size
                r = pos[1] // renderer.cell_size
                if grid.is_in_bounds((r, c)) and (r, c) not in [start, goal]:
                    grid.toggle_walls((r, c))

            if pygame.mouse.get_pressed()[0] and not event.type == pygame.MOUSEBUTTONDOWN:
                m_pos = pygame.mouse.get_pos()
                c = m_pos[0] // renderer.cell_size
                r = m_pos[1] // renderer.cell_size
                if grid.is_in_bounds((r, c)) and (r, c) not in [start, goal]:
                    grid.toggle_walls((r, c))

        reached_goal = False

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

        renderer.draw_panel(selected_algo, selected_distance, dynamic_mode)

        agent.draw(renderer.screen, renderer.cell_size)

        pygame.display.update()
        clock.tick(12)

if __name__ == "__main__":
    main()