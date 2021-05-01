import numpy as np
import random
import math as mt
actions = {0:"north", 1:"south", 2:"east", 3:"west"}



def Environment_interaction_next_state_reward(s_t, action, goal_state):
    x_t, y_t = s_t
    #once the goal state is reached  the navigator stays at the goal state and return 0 reward
    if x_t == goal_state[0] and y_t == goal_state[1]:
        return (goal_state[0],goal_state[1]), 0
    actual_action = -1
    if actions[action] == "north":
        actual_action = np.random.choice([0,1,2,3], p = [0.8, np.float(0.2/3), np.float(0.2/3), np.float(0.2/3)])
    elif actions[action] == "south":
        actual_action = np.random.choice([0,1,2,3], p = [np.float(0.2/3), 0.8, np.float(0.2/3), np.float(0.2/3)])
    elif actions[action] == "east":
        actual_action = np.random.choice([0, 1, 2, 3], p=[np.float(0.2 / 3), np.float(0.2 / 3), 0.8, np.float(0.2 / 3)])
    elif actions[action] == "west":
        actual_action = np.random.choice([0, 1, 2, 3], p=[np.float(0.2 / 3), np.float(0.2 / 3), 0.8, np.float(0.2 / 3)])

    next_state = None
    if actual_action == 0:
        next_state =(x_t, y_t + 1)
    elif actual_action == 1:
        next_state =(x_t, y_t - 1)
    elif actual_action == 2:
        next_state =(x_t + 1, y_t)
    elif actual_action == 3:
        next_state = (x_t - 1, y_t)

    if next_state[0] < 1 or next_state[0] > 48:
        return (s_t, -1)
    if next_state[1] < 1 or next_state[1] > 23:
        return (s_t, -1)

    if next_state[0] >= 1 and next_state[0] <= 48:
        if next_state[1] >= 1 and next_state[1]<=23:
            if next_state[0] in [25, 26] and next_state[1] in range(1, 12) or next_state[0] in [25, 26] and next_state[1] in range(13, 24):
                return s_t, -1
            else:
                if next_state[0] == goal_state[0] and next_state[1] == goal_state[1]:
                    return next_state, 100
                else:
                    return next_state, 0

def epsilon_greedy(epsilon,Q_values):
    action_ty = np.choice(["greedy", "explore"], p = [1-epsilon, epsilon])
    if action_ty == "greedy":
        values = np.array(Q_values.values())
        return np.argmax(values)
    elif action_ty == "explore":
        return np.choice([0,1,2,3] , p = [0.25, 0.25, 0.25,0.25])


def Q_learning_algorithm(epsilon, alpha, gamma, goal_state, no_of_episodes):
    Q_value = {}
    for i in range(1,49):
        for j in range(1,24):
            if i in [25,26] and j in range(1,12) or i in [25,26] and j in range(13,24):
                continue
            else:
                Q_value[(i,j)] = {}
                for k in range(0,4):
                    if i == goal_state[0] and j == goal_state[1]:
                        Q_value[(i, j)][k] = 0
                    else:
                        Q_value[(i,j)][k] = np.random.normal(5, 20, size=(1))[0]


    for i in range(no_of_episodes):
        hack1 = (random.randint(1,26),random.randint(1,24))
        hack2 = (random.randint(27, 49), random.randint(1, 24))
        present_state = np.choice([hack1, hack2], p = [0.5, 0.5])
        while(True):
            current_action = epsilon_greedy(epsilon, Q_value[present_state])
            next_state, reward = Environment_interaction_next_state_reward(present_state,current_action,goal_state)
            values = np.array(Q_value[next_state].values())
            increment_1 = values[np.argmax(values)]
            Q_value[present_state][current_action] = (1 - alpha)*Q_value[present_state][current_action] + alpha*(reward + gamma*increment_1)
            present_state = next_state
            if present_state[0] == goal_state[0] and present_state[1] == goal_state[1]:
                break
    return  Q_value




