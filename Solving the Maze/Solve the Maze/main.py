import numpy as np
from maze import Maze
from convert import Feasibility, find_reachable_neighbors
from PIL import Image
from draw import draw_image
from learn import train, walk
import pandas as pd


def my_print(Q):
    labels = [str(x) for x in range(Q.shape[0])]
    df = pd.DataFrame(Q, columns=labels, index=labels)
    pd.set_option('display.max_rows', None)
    print(df.to_string())


def run():
    np.random.seed(1)

    # gamma = 0.9
    # lrn_rate = 0.5
    # dimension1 = 5
    # dimension2 = 5
    dimension1 = int(input('Enter x dimension: '))
    dimension2 = int(input('Enter y dimension: '))
    gamma = float(
        input('Enter the gamma value (0, 1] (aka the discount factor, influences the importance of future rewards): '))
    lrn_rate = float(input(
        'Enter the learning rate (0, 1] (larger values increase the influence of both current rewards and future rewards (explore) at the expense of past rewards (exploit)): '))
    max_epochs = 1000

    # Create the Maze
    maze = Maze(dimension1, dimension2)
    maze.make_maze()

    # Draw the Maze
    margin = 80
    cell_side = 100
    line_thickness = 10
    maze = Maze(dimension1, dimension2)
    maze.make_maze()
    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw_image(img, "maze.png", maze.maze_grid)

    # Get the Feasibility Matrix
    feasibility = Feasibility(maze)
    feasibility.get_neighbors(maze)

    # Set start and goal:
    start = 0
    goal = feasibility.numbered_grid[maze.end[0], maze.end[1]]

    # Find the penultimate cell to set the highest reward for reaching the end of the maze:
    previous = find_reachable_neighbors(maze, maze.maze_grid[maze.end[0]][maze.end[1]])[0][1]
    prev_index = np.where(maze.maze_grid == previous)
    previous = feasibility.numbered_grid[prev_index[0], prev_index[1]][0]

    # Rewards:
    R = np.copy(feasibility.F)
    R = np.where(R == 1, -0.1, R)

    # Set the highest reward for reaching the end of the maze:
    R[previous, goal] = 1000.0

    # Initiate the Q-matrix:
    Q = np.zeros(shape=[feasibility.F.shape[0], feasibility.F.shape[0]], dtype=np.float32)  # Quality

    print("Analyzing maze with RL Q-learning")
    print("The F matrix:\n")
    my_print(feasibility.F)

    # Number of states:
    ns = feasibility.cells
    train(feasibility.F, R, Q, gamma, lrn_rate, goal, ns, max_epochs)
    print("Done ")

    print("The Q matrix is: \n ")
    my_print(Q)

    print(f"Using Q to go from 0 to goal ({goal})")

    walk(start, goal, Q)


if __name__ == "__main__":
    run()

