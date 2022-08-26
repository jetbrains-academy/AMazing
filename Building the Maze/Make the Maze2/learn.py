import numpy as np
from maze import Maze
from cell import Cell
from convert import Feasibility, find_reachable_neighbors
from PIL import Image, ImageDraw, ImageFont
from output import draw_image


def my_print(Q):
    # hard-coded hack for this problem only
    rows = len(Q);
    cols = len(Q[0])
    print("       0      1      2      3      4      5\
      6      7      8      9      10     11     12\
     13     14")
    for i in range(rows):
        print("%d " % i, end="")
        if i < 10: print(" ", end="")
        for j in range(cols): print(" %6.2f" % Q[i, j], end="")
        print("")
    print("")


def get_poss_next_states(s, F, ns):
    # given a state s and a feasibility matrix F
    # get list of possible next states
    poss_next_states = []
    for j in range(ns):
        if F[s, j] == 1: poss_next_states.append(j)
    return poss_next_states


def get_rnd_next_state(s, F, ns):
    # given a state s, pick a feasible next state
    poss_next_states = get_poss_next_states(s, F, ns)
    next_state = poss_next_states[np.random.randint(0, len(poss_next_states))]
    return next_state


# =============================================================

def train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs):
    # compute the Q matrix
    for i in range(0, max_epochs):
        curr_s = np.random.randint(0, ns)  # random start state

        while(True):
            next_s = get_rnd_next_state(curr_s, F, ns)
            poss_next_next_states = get_poss_next_states(next_s, F, ns)

            max_Q = -9999.99
            for j in range(len(poss_next_next_states)):
                nn_s = poss_next_next_states[j]
                q = Q[next_s, nn_s]
                if q > max_Q:
                    max_Q = q
            # Q = [(1-a) * Q]  +  [a * (rt + (g * maxQ))]
            Q_ = ((1 - lrn_rate) * Q[curr_s][next_s]) + (lrn_rate * (R[curr_s][next_s] + (gamma * max_Q)))
            Q[curr_s][next_s] = Q_

            curr_s = next_s
            if curr_s == goal: break


# =============================================================

def walk(start, goal, Q):
    # go to goal from start using Q
    curr = start
    print(str(curr) + "->", end="")
    while curr != goal:
        next = np.argmax(Q[curr])
        print(str(next) + "->", end="")
        curr = next
    print("done")


# =============================================================

def main():
    np.random.seed(1)
    # dimension1 = int(input('Enter x dimension: '))
    # dimension2 = int(input('Enter y dimension: '))
    dimension1 = 5
    dimension2 = 5
    gamma = float(input('Enter the gamma value (0, 1] (aka the discount factor, influences the importance of future rewards): '))
    lrn_rate = float(input('Enter the learning rate (0, 1] (larger values increase the influence of both current rewards and future rewards (explore) at the expense of past rewards (exploit)): '))
    max_epochs = 1000

    maze = Maze(dimension1, dimension2)
    maze.make_maze()

    # Draw
    margin = 80
    cell_side = 100
    line_thickness = 10
    maze = Maze(dimension1, dimension2)
    maze.make_maze()

    width, height = (margin + cell_side * dim for dim in maze.maze_grid.shape)
    img = Image.new("RGB", (width, height), (255, 255, 255))

    draw_image(img, "maze.png", maze.maze_grid)

    feasibility = Feasibility(maze)
    feasibility.get_neighbors(maze)
    print(feasibility.F)
    start = 0
    # Set the goal cell:
    goal = feasibility.numbered_grid[maze.end[0], maze.end[1]]
    # Find the penultimate cell to set the highest reward for reaching the end of the maze:
    previous = find_reachable_neighbors(maze, maze.maze_grid[maze.end[0]][maze.end[1]])[0][1]
    prev_index = np.where(maze.maze_grid == previous)
    previous = feasibility.numbered_grid[prev_index[0], prev_index[1]][0]

    # print(goal)
    # print(previous)

    R = np.copy(feasibility.F)  # Rewards
    R = np.where(R == 1, -0.01, R)
    # Set the highest reward for reaching the end of the maze:
    R[previous, goal] = 1000.0
    # print(R[previous, goal])
    # Initiate the Q-matrix:
    Q = np.zeros(shape=[feasibility.F.shape[0], feasibility.F.shape[0]], dtype=np.float32)  # Quality


    print("Analyzing maze with RL Q-learning")
    print("The R matrix:\n")
    print(R)

    # print(feasibility.numbered_grid)
    ns =  feasibility.cells  # Number of states
    # gamma = 0.9
    # lrn_rate = 0.5
    # max_epochs = 1000
    train(feasibility.F, R, Q, gamma, lrn_rate, goal, ns, max_epochs)
    print("Done ")

    print("The Q matrix is: \n ")
    print(Q)

    print(f"Using Q to go from 0 to goal ({goal})")

    walk(start, goal, Q)


if __name__ == "__main__":
    main()
