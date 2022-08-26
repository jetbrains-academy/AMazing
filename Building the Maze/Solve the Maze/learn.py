import numpy as np


def get_poss_next_states(s, F, ns):
    # given a state s and a feasibility matrix F
    # get list of possible next states
    poss_next_states = []
    for j in range(ns):
        if F[s, j] == 1:
            poss_next_states.append(j)
    return poss_next_states


def get_rnd_next_state(s, F, ns):
    # Given a state s, pick a feasible next state.
    poss_next_states = get_poss_next_states(s, F, ns)
    next_state = poss_next_states[np.random.randint(0, len(poss_next_states))]
    return next_state


# =============================================================

def train(F, R, Q, gamma, lrn_rate, goal, ns, max_epochs):
    # Compute the Q matrix
    for i in range(0, max_epochs):
        curr_s = np.random.randint(0, ns)  # random start state

        while True:
            next_s = get_rnd_next_state(curr_s, F, ns)
            poss_next_next_states = get_poss_next_states(next_s, F, ns)

            max_Q = -9999.99
            for j in range(len(poss_next_next_states)):
                nn_s = poss_next_next_states[j]
                q = Q[next_s, nn_s]
                if q > max_Q:
                    max_Q = q
            # Bellman's equation: Q = [(1-a) * Q]  +  [a * (rt + (g * maxQ))]
            # Update the Q matrix
            Q[curr_s][next_s] = ((1 - lrn_rate) * Q[curr_s][next_s]) + (lrn_rate * (R[curr_s][next_s] + (gamma * max_Q)))

            curr_s = next_s
            if curr_s == goal:
                break


# =============================================================

def walk(start, goal, Q):
    # Walk to the goal from start using Q matrix.
    curr = start
    print(str(curr) + "->", end="")
    while curr != goal:
        next_ = np.argmax(Q[curr])
        print(str(next_) + "->", end="")
        curr = next_
    print("done")





