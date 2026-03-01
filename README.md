````markdown
# RAHBAR (رہبر) – Dynamic Path-Finding Agent

**RAHBAR** is an interactive Python-based visualization tool designed to demonstrate and compare pathfinding algorithms in both static and dynamic environments.

It allows users to visualize how different search strategies navigate a 2D grid while adapting to real-time environmental changes.

---

# Features

## Algorithm Selection
- Toggle between:
  - **A\*** (Optimal Search)
  - **Greedy Best-First Search (GBFS)**

## Dual Heuristics
- **Manhattan Distance**
- **Euclidean Distance**

## Dynamic Environments
- A **Dynamic Mode** that spawns obstacles in real-time.
- The agent automatically re-calculates its path if blocked.

## Interactive Grid
- Draw or erase walls using your mouse.
- Create custom mazes and test cases.

## Performance Metrics
Real-time tracking of:
- Visited nodes  
- Path cost  
- Execution time (in milliseconds)

---

# Installation

## Prerequisites
- Python **3.10 or higher**
- `pygame` library

## Clone the Repository

```bash
git clone https://github.com/Mzt00/Dynamic-Path-Finding-Agent
cd Dynamic-Path-Finding-Agent
````

## Install Dependencies

```bash
pip install pygame
```

---

# How to Use

Run the application:

```bash
python main.py
```

---

# Controls

| Input                | Action                                                            |
| -------------------- | ----------------------------------------------------------------- |
| **Mouse Left Click** | Toggle walls on the grid                                          |
| **Space Bar**        | Start the search and initiate agent movement                      |
| **R Key**            | Randomize map obstacles                                           |
| **D Key**            | Toggle Dynamic Mode                                               |
| **1 / 2 Keys**       | Switch between **A*** (1) and **GBFS** (2)                        |
| **M / E Keys**       | Switch between **Manhattan (M)** and **Euclidean (E)** heuristics |
| **C Key**            | Clear the grid and reset the agent                                |

---

# Technical Architecture

The project is structured into modular components for clarity and scalability.

## Core Logic

### `grid.py`

* Manages grid state
* Handles wall placement
* Validates neighbors

### `agent.py`

* Handles agent position
* Controls movement
* Stores path information

---

## Search Strategies

### `a_star.py`

Implements:

```python
f(n) = g(n) + h(n)
```

* Guarantees the shortest path.

### `gbfs.py`

Implements:

```python
f(n) = h(n)
```

* Faster but may produce sub-optimal paths.

### `heuristics.py`

* Contains Manhattan and Euclidean distance implementations.

---

## GUI and Visualization

### `renderer.py`

* Manages the Pygame window
* Draws the grid
* Renders the control panel

### `main.py`

* Entry point of the application
* Handles event loop
* Manages user interactions

---

## Utilities

### `priority_queue.py`

* A wrapper around Python’s `heapq`
* Manages node expansion based on priority

---

# Implementation Details

## A* Implementation

* Uses a priority queue
* Expands nodes based on:

```python
f(n) = g(n) + h(n)
```

* Supports **8-way movement**
* Diagonal movement cost is weighted at **1.41** for realistic distance calculation

---

## Dynamic Re-Routing

When **Dynamic Mode** is active:

1. The system checks if a newly spawned obstacle intersects the agent’s current path.
2. If blocked:

   * The agent immediately triggers a new search
   * The search starts from the agent’s current position
   * The original goal remains unchanged

This enables real-time adaptive navigation in changing environments.

---

# Purpose

RAHBAR is designed for:

* Algorithm visualization
* AI and search strategy comparison
* Academic demonstrations
* Understanding dynamic path re-planning

---

# Built With

* Python
* Pygame

```
```
