import numpy as np
import math as mt
actions = {0:"north", 1:"south", 2:"east", 3:"west"}

def Transition_function(state_t, action_t, state_t_1):
    x_t, y_t =  state_t
    x_t_1, y_t_1 = state_t_1
    if x_t_1 >= 49 or y_t_1 >= 24 or x_t_1 <=0 or y_t_1 <=0 or x_t >= 49 or y_t >= 24 or x_t <=0 or y_t <=0:
        return np.float(0.0)
    if actions[action_t] == "north":
        #left_corner_wall
        if x_t == 1 and y_t == 1 and x_t_1==1 and y_t_1 ==1:
            return np.float(0.4/3)
        elif x_t == 1 and y_t == 23 and x_t_1==1 and y_t_1 ==23:
            return np.float(0.2/3 + 0.8)
        elif x_t == 1 and y_t in range(2,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        #middle_wall
        elif x_t == 24 and y_t == 1 and x_t_1==24 and y_t_1 ==1:
            return np.float(0.4/3)
        elif x_t == 24 and y_t == 23 and x_t_1==24 and y_t_1 ==23:
            return np.float(0.2/3 + 0.8)
        elif x_t == 24 and y_t in range(2,12) and x_t_1==x_t and y_t_1 ==y_t or x_t == 24 and y_t in range(13,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t == 27 and y_t == 1 and x_t_1==27 and y_t_1 ==1:
            return np.float(0.4/3)
        elif x_t == 27 and y_t == 23 and x_t_1==27 and y_t_1 ==23:
            return np.float(0.2/3 + 0.8)
        elif x_t == 27 and y_t in range(2,12) and x_t_1==x_t and y_t_1 ==y_t or x_t == 27 and y_t in range(13,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t in [25,26] and y_t ==12 and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3 + 0.8)

        #right_wall
        elif x_t == 48 and y_t == 1 and x_t_1==48 and y_t_1 ==1:
            return np.float(0.4/3)
        elif x_t == 48 and y_t == 23 and x_t_1==48 and y_t_1 ==23:
            return np.float(0.2/3 + 0.8)
        elif x_t == 48 and y_t in range(2,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t_1 == x_t and y_t_1 == y_t+1:
            return np.float(0.8)
        elif x_t_1 == x_t+1 and y_t_1 == y_t:
            return np.float(0.2/3)
        elif x_t_1 == x_t and y_t_1 == y_t-1:
            return np.float(0.2/3)
        elif x_t_1 == x_t-1 and y_t_1 == y_t:
            return np.float(0.2/3)
        else:
            return np.float(0.0)

    elif actions[action_t] == "east":
        if x_t == 1 and y_t == 1 and x_t_1==1 and y_t_1 ==1:
            return np.float(0.4/3)
        elif x_t == 1 and y_t == 23 and x_t_1==1 and y_t_1 ==23:
            return np.float(0.4/3)
        elif x_t == 1 and y_t in range(2,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)


        elif x_t == 24 and y_t == 1 and x_t_1==24 and y_t_1 ==1:
            return np.float(0.2/3 + 0.8)
        elif x_t == 24 and y_t == 23 and x_t_1==24 and y_t_1 ==23:
            return np.float(0.2/3 + 0.8)
        elif x_t == 24 and y_t in range(2,12) and x_t_1==x_t and y_t_1 ==y_t or x_t == 24 and y_t in range(13,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.8)

        elif x_t == 27 and y_t == 1 and x_t_1==27 and y_t_1 ==1:
            return np.float(0.4/3)
        elif x_t == 27 and y_t == 23 and x_t_1==27 and y_t_1 ==23:
            return np.float(0.4/3)
        elif x_t == 27 and y_t in range(2,12) and x_t_1==x_t and y_t_1 ==y_t or x_t == 27 and y_t in range(13,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t in [25,26] and y_t ==12 and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.4/3)

        elif x_t == 48 and y_t == 1 and x_t_1==48 and y_t_1 ==1:
            return np.float(0.2/3 + 0.8)
        elif x_t == 48 and y_t == 23 and x_t_1==48 and y_t_1 ==23:
            return np.float(0.2/3 + 0.8)
        elif x_t == 48 and y_t in range(2,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.8)

        elif x_t_1 == x_t and y_t_1 == y_t+1:
            return np.float(0.2/3)
        elif x_t_1 == x_t+1 and y_t_1 == y_t:
            return np.float(0.8)
        elif x_t_1 == x_t and y_t_1 == y_t-1:
            return np.float(0.2/3)
        elif x_t_1 == x_t-1 and y_t_1 == y_t:
            return np.float(0.2/3)
        else:
            return np.float(0.0)

    elif actions[action_t] == "west":
        if x_t == 1 and y_t == 1 and x_t_1 == 1 and y_t_1 == 1:
            return np.float(0.2 / 3 + 0.8)
        elif x_t == 1 and y_t == 23 and x_t_1 == 1 and y_t_1 == 23:
            return np.float(0.2 / 3 + 0.8)
        elif x_t == 1 and y_t in range(2,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.8)

        elif x_t == 24 and y_t == 1 and x_t_1 == 24 and y_t_1 == 1:
            return np.float(0.4/ 3)
        elif x_t == 24 and y_t == 23 and x_t_1 == 24 and y_t_1 == 23:
            return np.float(0.4/3)
        elif x_t == 24 and y_t in range(2,12) and x_t_1==x_t and y_t_1 ==y_t or x_t == 24 and y_t in range(13,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t == 27 and y_t == 1 and x_t_1 == 27 and y_t_1 == 1:
            return np.float(0.2 / 3 + 0.8)
        elif x_t == 27 and y_t == 23 and x_t_1 == 27 and y_t_1 == 23:
            return np.float(0.2 / 3 + 0.8)
        elif x_t == 27 and y_t in range(2,12) and x_t_1==x_t and y_t_1 ==y_t or x_t == 27 and y_t in range(13,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.8)

        elif x_t in [25,26] and y_t ==12 and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.4/3)

        elif x_t == 48 and y_t == 1 and x_t_1 == 48 and y_t_1 == 1:
            return np.float(0.4/3)
        elif x_t == 48 and y_t == 23 and x_t_1 == 48 and y_t_1 == 23:
            return np.float(0.4/3)
        elif x_t == 48 and y_t in range(2,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t_1 == x_t and y_t_1 == y_t + 1:
            return np.float(0.2 / 3)
        elif x_t_1 == x_t + 1 and y_t_1 == y_t:
            return np.float(0.2/3)
        elif x_t_1 == x_t and y_t_1 == y_t - 1:
            return np.float(0.2 / 3)
        elif x_t_1 == x_t - 1 and y_t_1 == y_t:
            return np.float(0.8)
        else:
            return np.float(0.0)
    elif actions[action_t] == "south":
        if x_t == 1 and y_t == 1 and x_t_1 == 1 and y_t_1 == 1:
            return np.float(0.2 / 3 + 0.8)
        elif x_t == 1 and y_t == 23 and x_t_1 == 1 and y_t_1 == 23:
            return np.float(0.4/ 3)
        elif x_t == 1 and y_t in range(2,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t == 24 and y_t == 1 and x_t_1 == 24 and y_t_1 == 1:
            return np.float(0.2 / 3 + 0.8)
        elif x_t == 24 and y_t == 23 and x_t_1 == 24 and y_t_1 == 23:
            return np.float(0.4/3)
        elif x_t == 24 and y_t in range(2,12) and x_t_1==x_t and y_t_1 ==y_t or x_t == 24 and y_t in range(13,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t == 27 and y_t == 1 and x_t_1 == 27 and y_t_1 == 1:
            return np.float(0.2 / 3 + 0.8)
        elif x_t == 27 and y_t == 23 and x_t_1 == 27 and y_t_1 == 23:
            return np.float(0.4/ 3)
        elif x_t == 27 and y_t in range(2,12) and x_t_1==x_t and y_t_1 ==y_t or x_t == 27 and y_t in range(13,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t in [25,26] and y_t ==12 and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3 + 0.8)

        elif x_t == 48 and y_t == 1 and x_t_1 == 48 and y_t_1 == 1:
            return np.float(0.2 / 3 + 0.8)
        elif x_t == 48 and y_t == 23 and x_t_1 == 48 and y_t_1 == 23:
            return np.float(0.4/3)
        elif x_t == 48 and y_t in range(2,23) and x_t_1==x_t and y_t_1 ==y_t:
            return np.float(0.2/3)

        elif x_t_1 == x_t and y_t_1 == y_t + 1:
            return np.float(0.2 / 3)
        elif x_t_1 == x_t + 1 and y_t_1 == y_t:
            return np.float(0.2/3)
        elif x_t_1 == x_t and y_t_1 == y_t - 1:
            return np.float(0.8)
        elif x_t_1 == x_t - 1 and y_t_1 == y_t:
            return np.float(0.2/3)
        else:
            return np.float(0.0)





def Reward_function(state_t, state_t_1):
    x_t , y_t = state_t
    x_t_1, y_t_1 =  state_t_1
    if x_t_1== 48 and y_t_1 == 12:
        return 100
    if x_t == 1 and y_t == 1 and x_t_1 == 1 and y_t_1 == 1:
        return -1
    elif x_t == 1 and y_t == 23 and x_t_1 == 1 and y_t_1 == 23:
        return -1
    elif x_t == 1 and y_t in range(2, 23) and x_t_1 == x_t and y_t_1 == y_t:
        return -1

    elif x_t == 24 and y_t == 1 and x_t_1 == 24 and y_t_1 == 1:
        return -1
    elif x_t == 24 and y_t == 23 and x_t_1 == 24 and y_t_1 == 23:
        return -1
    elif x_t == 24 and y_t in range(2, 12) and x_t_1 == x_t and y_t_1 == y_t or x_t == 24 and y_t in range(13,
                                                                                                           23) and x_t_1 == x_t and y_t_1 == y_t:
        return -1

    elif x_t == 27 and y_t == 1 and x_t_1 == 27 and y_t_1 == 1:
        return -1
    elif x_t == 27 and y_t == 23 and x_t_1 == 27 and y_t_1 == 23:
        return -1
    elif x_t == 27 and y_t in range(2, 12) and x_t_1 == x_t and y_t_1 == y_t or x_t == 27 and y_t in range(13,
                                                                                                           23) and x_t_1 == x_t and y_t_1 == y_t:
        return -1

    elif x_t in [25, 26] and y_t == 12 and x_t_1 == x_t and y_t_1 == y_t:
        return -1

    elif x_t == 48 and y_t == 1 and x_t_1 == 48 and y_t_1 == 1:
        return -1
    elif x_t == 48 and y_t == 23 and x_t_1 == 48 and y_t_1 == 23:
        return -1
    elif x_t == 48 and y_t in range(2, 23) and x_t_1 == x_t and y_t_1 == y_t:
        return -1
    else:
        return 0

#Value_Iteration
def Value_iteration(goal_state= (48,12), theta=0.1, gamma=0.1):
    Value_of_states = np.random.randn(50,25)
    x_goal, y_goal = goal_state
    Value_of_states[x_goal,y_goal] = 0
    #value_iteration
    while(True):
        delta = 0
        for i in range(1, 49):
            for j in range(1, 24):
                if i == 25 or i == 26 and j != 12:
                    Value_of_states[i,j] = np.inf
                else:
                    v = Value_of_states[i,j]
                    temp = np.zeros(4)
                    temp[0] = Transition_function((i,j), 0, (i+1, j))*(Reward_function((i,j), (i+1,j)) + gamma*Value_of_states[i+1, j]) \
                              + Transition_function((i,j), 0, (i-1, j))*(Reward_function((i,j), (i-1,j)) + gamma*Value_of_states[i-1, j])\
                              + Transition_function((i,j), 0, (i, j+1))*(Reward_function((i,j), (i,j+1)) + gamma*Value_of_states[i, j+1])\
                              + Transition_function((i,j), 0, (i, j-1))*(Reward_function((i,j), (i,j-1)) + gamma*Value_of_states[i, j-1])

                    temp[1] = Transition_function((i, j), 1, (i + 1, j)) * (
                                Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                              + Transition_function((i, j), 1, (i - 1, j)) * (
                                          Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                              + Transition_function((i, j), 1, (i, j + 1)) * (
                                          Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                              + Transition_function((i, j), 1, (i, j - 1)) * (
                                          Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1])
                    temp[2] = Transition_function((i, j), 2, (i + 1, j)) * (
                                Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                              + Transition_function((i, j), 2, (i - 1, j)) * (
                                          Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                              + Transition_function((i, j), 2, (i, j + 1)) * (
                                          Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                              + Transition_function((i, j), 2, (i, j - 1)) * (
                                          Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1])
                    temp[3] = Transition_function((i, j), 3, (i + 1, j)) * (
                                Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                              + Transition_function((i, j), 3, (i - 1, j)) * (
                                          Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                              + Transition_function((i, j), 3, (i, j + 1)) * (
                                          Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                              + Transition_function((i, j), 3, (i, j - 1)) * (
                                          Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1])
                    action = np.argmax(temp)
                    Value_of_states[i,j] = temp[action]
                    delta = np.max(delta, np.abs(v-Value_of_states[i,j]))
        if delta < theta:
             break


    #policy:
    Policy = np.zero((50,25))
    for i in range(1,24):
        for j in range(1,49):
            temp = np.zeros(4)
            temp[0] = Transition_function((i, j), 0, (i + 1, j)) * (
                        Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                      + Transition_function((i, j), 0, (i - 1, j)) * (
                                  Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                      + Transition_function((i, j), 0, (i, j + 1)) * (
                                  Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                      + Transition_function((i, j), 0, (i, j - 1)) * (
                                  Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1])

            temp[1] = Transition_function((i, j), 1, (i + 1, j)) * (
                    Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                      + Transition_function((i, j), 1, (i - 1, j)) * (
                              Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                      + Transition_function((i, j), 1, (i, j + 1)) * (
                              Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                      + Transition_function((i, j), 1, (i, j - 1)) * (
                              Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1])
            temp[2] = Transition_function((i, j), 2, (i + 1, j)) * (
                    Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                      + Transition_function((i, j), 2, (i - 1, j)) * (
                              Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                      + Transition_function((i, j), 2, (i, j + 1)) * (
                              Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                      + Transition_function((i, j), 2, (i, j - 1)) * (
                              Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1])
            temp[3] = Transition_function((i, j), 3, (i + 1, j)) * (
                    Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                      + Transition_function((i, j), 3, (i - 1, j)) * (
                              Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                      + Transition_function((i, j), 3, (i, j + 1)) * (
                              Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                      + Transition_function((i, j), 3, (i, j - 1)) * (
                              Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1])
            optimal_action = np.argmax(temp)
            Policy[i,j] = optimal_action


    return Value_of_states, Policy



