
import time
from src.utils.priority_queue import PriorityQueue
def reconstruct_path(came_from,start,goal):
    if goal not in came_from:
            return []
    current = goal
    path = []
    while current!=start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

def gbfs_search(grid,start,goal,heuristic_ref):
    #heuristic_ref refers to either
    #euclidian distance or manhattan distance
    start_time=time()
    frontier = PriorityQueue()
    frontier.put(start,0)
    came_from = {start: None}
    cost_so_far = {start: 0}
    visited_nodes = []
    while not frontier.empty():
        current = frontier.get()
        #current is g(n)
        visited_nodes.append(current)
        if current == goal:
            break
    for next_node in grid.getneighbours(current):
        new_cost = cost_so_far[current]+1
        if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
            cost_so_far = new_cost
            #only check the heuristic
            priority = heuristic_func(next_node, goal)
            frontier.put(next_node,priority)
            came_from[next_node] = current
    execution_time = (time.time() - start_time)*1000
    path = reconstruct_path(came_from,start,goal)
    return {
        "path": path,
        "visited": visited_nodes,
        "cost": len(path) if path else 0,
        "time": execution_time
    }

   

        
    
    
    
 
