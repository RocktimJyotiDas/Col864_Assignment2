import numpy as np

def Next_state_and_reward(s_t, actual_action, goal_state):
    x_t, y_t = s_t

    #calculating the next state!
    if actual_action == 0:
        next_state =(x_t, y_t + 1)
    elif actual_action == 1:
        next_state =(x_t, y_t - 1)
    elif actual_action == 2:
        next_state =(x_t + 1, y_t)
    elif actual_action == 3:
        next_state = (x_t - 1, y_t)
    
    
    if next_state[0] < 1 or next_state[0] > 48:
        if(s_t[0] == goal_state[0] and s_t[1] == goal_state[1]):
            return (s_t, 100)
        else:
            return (s_t, -1)
    
    if next_state[1] < 1 or next_state[1] > 23:
        return (s_t, -1)

    if next_state[0] >= 1 and next_state[0] <= 48:
        if next_state[1] >= 1 and next_state[1]<=23:
            if next_state[0] in [25, 26] and (next_state[1] in range(1, 12)  or next_state[1] in range(13, 24)):
                #print((s_t, -1))
                return (s_t, -1)
            else:
                if next_state[0] == goal_state[0] and next_state[1] == goal_state[1]:
                    #print((next_state, 100))
                    return (next_state, 100)
                else:
                    #print((next_state, 0))
                    return (next_state, 0)
