import numpy as np
import math as mt
actions = {0:"north", 1:"south", 2:"east", 3:"west"}

def Transition_function(state_t, action_t, state_t_1):
    x_t, y_t =  state_t
    x_t_1, y_t_1 = state_t_1
    if x_t_1 >= 49 or y_t_1 >= 24 or x_t_1 <=0 or y_t_1 <=0 or x_t >= 49 or y_t >= 24 or x_t <=0 or y_t <=0 \
            or x_t_1 in [25,26] and y_t_1 in range(1,12) or x_t_1 in [25,26] and y_t_1 in range(13,24) \
            or x_t in [25,26] and y_t in range(1,12) or x_t in [25,26] and y_t in range(13,24):
        return np.float(0.0)
    if actions[action_t] == "north":
        #left_corner_wall
        if x_t == 1 and y_t == 1:
            if x_t_1==1 and y_t_1 ==1:
                return np.float(0.4/3)
            elif x_t_1==0 and y_t_1 ==1:
                return np.float(0.0)
            elif x_t_1==1 and y_t_1 ==0:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 1 and y_t == 23:
            if x_t_1==1 and y_t_1 ==23:
                return np.float(0.2/3 + 0.8)
            elif x_t_1 == 0 and y_t_1 == 23:
                return np.float(0.0)
            elif x_t_1 == 1 and y_t_1 == 24:
                return np.float(0.0)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 1 and y_t in range(2,23):
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3)
            elif x_t_1 == 0 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        #middle_wall
        elif x_t == 24 and y_t == 1:
            if x_t_1==24 and y_t_1 ==1:
                return np.float(0.4/3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t-1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            else:
                return np.float(0.0)

        elif x_t == 24 and y_t == 23:
            if x_t_1==24 and y_t_1 ==23:
                return np.float(0.2/3 + 0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t+1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)


        elif x_t == 24 and y_t in range(2,12)  or x_t == 24 and y_t in range(13,23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)

        elif x_t == 27 and y_t == 1:
            if x_t_1==27 and y_t_1 ==1:
                return np.float(0.4/3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t-1:
                return np.float(0.0)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            else:
                return np.float(0.0)

        elif x_t == 27 and y_t == 23:
            if x_t_1==27 and y_t_1 ==23:
                return np.float(0.2/3 + 0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t+1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 27 and y_t in range(2,12) or x_t == 27 and y_t in range(13,23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t in [25,26] and y_t ==12:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3 + 0.8)
            elif x_t_1== x_t and y_t_1 == y_t-1:
                return np.float(0.0)
            elif x_t_1== x_t and y_t_1 == y_t+1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        #right_wall
        elif x_t == 48 and y_t == 1:
            if x_t_1==48 and y_t_1 ==1:
                return np.float(0.4/3)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1== x_t and y_t_1 == y_t-1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        elif x_t == 48 and y_t == 23:
            if x_t_1==48 and y_t_1 ==23:
                return np.float(0.2/3 + 0.8)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1== x_t and y_t_1 == y_t+1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)

        elif x_t == 48 and y_t in range(2,23):
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)
        elif x_t in range(2,25) and y_t == 1 or x_t in range(27,49) and y_t ==1:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t in range(2,25) and y_t == 1 or x_t in range(27,49) and y_t ==23:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.8)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t_1 == x_t+1 and y_t_1 == y_t:
            return np.float(0.2/3)
        elif x_t_1 == x_t and y_t_1 == y_t-1:
            return np.float(0.2/3)
        elif x_t_1 == x_t and y_t_1 == y_t+1:
            return np.float(0.8)
        elif x_t_1 == x_t-1 and y_t_1 == y_t:
            return np.float(0.2/3)
        else:
            return np.float(0.0)


    #EAST
    elif actions[action_t] == "east":
        # left_corner_wall
        if x_t == 1 and y_t == 1:
            if x_t_1 == 1 and y_t_1 == 1:
                return np.float(0.4 / 3)
            elif x_t_1 == 0 and y_t_1 == 1:
                return np.float(0.0)
            elif x_t_1 == 1 and y_t_1 == 0:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            else:
                return np.float(0.0)

        elif x_t == 1 and y_t == 23:
            if x_t_1 == 1 and y_t_1 == 23:
                return np.float(0.4 / 3)
            elif x_t_1 == 0 and y_t_1 == 23:
                return np.float(0.0)
            elif x_t_1 == 1 and y_t_1 == 24:
                return np.float(0.0)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 1 and y_t in range(2, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == 0 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        # middle_wall
        elif x_t == 24 and y_t == 1:
            if x_t_1 == 24 and y_t_1 == 1:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2/3)
            else:
                return np.float(0.0)

        elif x_t == 24 and y_t == 23:
            if x_t_1 == 24 and y_t_1 == 23:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)

        elif x_t == 24 and y_t in range(2, 12) or x_t == 24 and y_t in range(13, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.8 )
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)

        elif x_t == 27 and y_t == 1:
            if x_t_1 == 27 and y_t_1 == 1:
                return np.float(0.4 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 27 and y_t == 23:
            if x_t_1 == 27 and y_t_1 == 23:
                return np.float(0.4 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            else:
                return np.float(0.0)


        elif x_t == 27 and y_t in range(2, 12) or x_t == 27 and y_t in range(13, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            else:
                return np.float(0.0)

        elif x_t in [25, 26] and y_t == 12:
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.4 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            else:
                return np.float(0.0)


        # right_wall
        elif x_t == 48 and y_t == 1:
            if x_t_1 == 48 and y_t_1 == 1:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        elif x_t == 48 and y_t == 23:
            if x_t_1 == 48 and y_t_1 == 23:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)

        elif x_t == 48 and y_t in range(2, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)
        elif x_t in range(2,25) and y_t == 1 or x_t in range(27,49) and y_t ==1:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2/3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t in range(2,25) and y_t == 1 or x_t in range(27,49) and y_t ==23:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t_1 == x_t and y_t_1 == y_t + 1:
            return np.float(0.2/3)
        elif x_t_1 == x_t + 1 and y_t_1 == y_t:
            return np.float(0.8)
        elif x_t_1 == x_t and y_t_1 == y_t - 1:
            return np.float(0.2 / 3)
        elif x_t_1 == x_t - 1 and y_t_1 == y_t:
            return np.float(0.2 / 3)
        else:
            return np.float(0.0)

    #WEST_modified:
    elif actions[action_t] == "west":
        # left_corner_wall
        if x_t == 1 and y_t == 1:
            if x_t_1 == 1 and y_t_1 == 1:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == 0 and y_t_1 == 1:
                return np.float(0.0)
            elif x_t_1 == 1 and y_t_1 == 0:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 1 and y_t == 23:
            if x_t_1 == 1 and y_t_1 == 23:
                return np.float(0.2/ 3 + 0.8)
            elif x_t_1 == 0 and y_t_1 == 23:
                return np.float(0.0)
            elif x_t_1 == 1 and y_t_1 == 24:
                return np.float(0.0)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 1 and y_t in range(2, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == 0 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        # middle_wall
        elif x_t == 24 and y_t == 1:
            if x_t_1 == 24 and y_t_1 == 1:
                return np.float(0.4/ 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 24 and y_t == 23:
            if x_t_1 == 24 and y_t_1 == 23:
                return np.float(0.4 / 3 )
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)

            else:
                return np.float(0.0)

        elif x_t == 24 and y_t in range(2, 12) or x_t == 24 and y_t in range(13, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/3 )
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)

            else:
                return np.float(0.0)

        elif x_t == 27 and y_t == 1:
            if x_t_1 == 27 and y_t_1 == 1:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 27 and y_t == 23:
            if x_t_1 == 27 and y_t_1 == 23:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        elif x_t == 27 and y_t in range(2, 12) or x_t == 27 and y_t in range(13, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t in [25, 26] and y_t == 12:
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.4 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        # right_wall
        elif x_t == 48 and y_t == 1:
            if x_t_1 == 48 and y_t_1 == 1:
                return np.float(0.4 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)
            else:
                return np.float(0.0)


        elif x_t == 48 and y_t == 23:
            if x_t_1 == 48 and y_t_1 == 23:
                return np.float(0.4 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)

            else:
                return np.float(0.0)

        elif x_t == 48 and y_t in range(2, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)
            else:
                return np.float(0.0)
        elif x_t in range(2,25) and y_t == 1 or x_t in range(27,49) and y_t ==1:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2/3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)
            else:
                return np.float(0.0)

        elif x_t in range(2,25) and y_t == 1 or x_t in range(27,49) and y_t ==23:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.8)
            else:
                return np.float(0.0)

        elif x_t_1 == x_t and y_t_1 == y_t + 1:
            return np.float(0.2/3)
        elif x_t_1 == x_t + 1 and y_t_1 == y_t:
            return np.float(0.2 / 3)
        elif x_t_1 == x_t and y_t_1 == y_t - 1:
            return np.float(0.2 / 3)
        elif x_t_1 == x_t - 1 and y_t_1 == y_t:
            return np.float(0.8)
        else:
            return np.float(0.0)






    #SOuth_modified
    elif actions[action_t] == "south":
        # left_corner_wall
        if x_t == 1 and y_t == 1:
            if x_t_1 == 1 and y_t_1 == 1:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == 0 and y_t_1 == 1:
                return np.float(0.0)
            elif x_t_1 == 1 and y_t_1 == 0:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 1 and y_t == 23:
            if x_t_1 == 1 and y_t_1 == 23:
                return np.float(0.4/ 3)
            elif x_t_1 == 0 and y_t_1 == 23:
                return np.float(0.0)
            elif x_t_1 == 1 and y_t_1 == 24:
                return np.float(0.0)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.8)
            else:
                return np.float(0.0)

        elif x_t == 1 and y_t in range(2, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == 0 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.8)
            else:
                return np.float(0.0)


        # middle_wall
        elif x_t == 24 and y_t == 1:
            if x_t_1 == 24 and y_t_1 == 1:
                return np.float(0.2/ 3 + 0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 24 and y_t == 23:
            if x_t_1 == 24 and y_t_1 == 23:
                return np.float(0.4 / 3 )
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)

        elif x_t == 24 and y_t in range(2, 12) or x_t == 24 and y_t in range(13, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/3 )
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)

        elif x_t == 27 and y_t == 1:
            if x_t_1 == 27 and y_t_1 == 1:
                return np.float(0.2 / 3 + 0.8)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t == 27 and y_t == 23:
            if x_t_1 == 27 and y_t_1 == 23:
                return np.float(0.4 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        elif x_t == 27 and y_t in range(2, 12) or x_t == 27 and y_t in range(13, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        elif x_t in [25, 26] and y_t == 12:
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/ 3 + 0.8)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        # right_wall
        elif x_t == 48 and y_t == 1:
            if x_t_1 == 48 and y_t_1 == 1:
                return np.float(0.2/ 3 + 0.8)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        elif x_t == 48 and y_t == 23:
            if x_t_1 == 48 and y_t_1 == 23:
                return np.float(0.4 / 3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)

            else:
                return np.float(0.0)

        elif x_t == 48 and y_t in range(2, 23):
            if x_t_1 == x_t and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t + 1 and y_t_1 == y_t:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2 / 3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)
        elif x_t in range(2,25) and y_t == 1 or x_t in range(27,49) and y_t ==1:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.8)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.0)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.2/3)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)


        elif x_t in range(2,25) and y_t == 1 or x_t in range(27,49) and y_t ==23:
            if x_t_1==x_t and y_t_1 ==y_t:
                return np.float(0.2/3)
            elif x_t_1== x_t + 1 and y_t_1 == y_t:
                return np.float(0.2/3)
            elif x_t_1 == x_t and y_t_1 == y_t - 1:
                return np.float(0.8)
            elif x_t_1 == x_t and y_t_1 == y_t + 1:
                return np.float(0.0)
            elif x_t_1 == x_t - 1 and y_t_1 == y_t:
                return np.float(0.2 / 3)
            else:
                return np.float(0.0)

        elif x_t_1 == x_t and y_t_1 == y_t + 1:
            return np.float(0.2/3)
        elif x_t_1 == x_t + 1 and y_t_1 == y_t:
            return np.float(0.2 / 3)
        elif x_t_1 == x_t and y_t_1 == y_t - 1:
            return np.float(0.8)
        elif x_t_1 == x_t - 1 and y_t_1 == y_t:
            return np.float(0.2 / 3)
        else:
            return np.float(0.0)










#
#for test_j in range(1,24):
 #       print((1,test_j))
  #      print(Transition_function((1,test_j), 0, (1,test_j)))
   #     print(Transition_function((1, test_j), 0, (2, test_j)))
    #    print(Transition_function((1, test_j), 0, (1, test_j+1)))










def Reward_function(state_t, state_t_1):
    x_t , y_t = state_t
    x_t_1, y_t_1 =  state_t_1

    if x_t_1 >= 49 or y_t_1 >= 24 or x_t_1 <=0 or y_t_1 <=0 or x_t >= 49 or y_t >= 24 or x_t <=0 or y_t <=0 \
            or x_t_1 in [25,26] and y_t_1 in range(1,12) or x_t_1 in [25,26] and y_t_1 in range(13,24) \
            or x_t in [25,26] and y_t in range(1,12) or x_t in [25,26] and y_t in range(13,24):
        return -10000000
    #Goal
    if x_t_1== 48 and y_t_1 == 12:
        return 100
    #lEFT WALL
    if x_t == 1 and y_t == 1 and x_t_1 == 1 and y_t_1 == 1:
        return -1
    elif x_t == 1 and y_t == 23 and x_t_1 == 1 and y_t_1 == 23:
        return -1
    elif x_t == 1 and y_t in range(2, 23) and x_t_1 == x_t and y_t_1 == y_t:
        return -1

    #MIDDLE WALL
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

    #RIGHT WALL
    elif x_t == 48 and y_t == 1 and x_t_1 == 48 and y_t_1 == 1:
        return -1
    elif x_t == 48 and y_t == 23 and x_t_1 == 48 and y_t_1 == 23:
        return -1
    elif x_t == 48 and y_t in range(2, 23) and x_t_1 == x_t and y_t_1 == y_t:
        return -1

    #BOTTOM WALL
    elif x_t in range(2, 25) and y_t == 1 and x_t_1 == x_t and y_t_1 == y_t or x_t in range(27, 49) and y_t == 1 and x_t_1 == x_t and y_t_1 == y_t:
        return -1

    #TOP WALL
    elif x_t in range(2, 25) and y_t == 23 and x_t_1 == x_t and y_t_1 == y_t or x_t in range(27, 49) and y_t == 23 and x_t_1 == x_t and y_t_1 == y_t:
        return -1
    else:
        return 0

#Value_Iteration
def Value_iteration(goal_state= (48,12), theta=0.1, gamma=0.1, iterations =10):
    Value_of_states = np.zeros((50,25))
    #Value_of_states[1:49,1:24] = np.random.randn(48,23)
    x_goal, y_goal = goal_state
    Value_of_states[x_goal,y_goal] = 0
    iter = 0
    Policy2 = np.zeros((50,25))
    #value_iteration
    while(True):
        delta = 0
        for i in range(1, 49):
            for j in range(1, 24):
                if i in [25,26] and j in range(1,12) or i in [25,26] and j in range(13,24):
                    Value_of_states[i,j] = 0
                    Policy2[i,j] = None
                elif i == 48 and j == 12:
                    Value_of_states[i,j] = Reward_function((i,j), (i,j)) +gamma*Value_of_states[i, j]
                    Policy2[i,j] = -1
                else:
                    v = Value_of_states[i,j]
                    temp = np.zeros(4)
                    temp[0] = Transition_function((i,j), 0, (i+1, j))*(Reward_function((i,j), (i+1,j)) + gamma*Value_of_states[i+1, j]) \
                              + Transition_function((i,j), 0, (i-1, j))*(Reward_function((i,j), (i-1,j)) + gamma*Value_of_states[i-1, j])\
                              + Transition_function((i,j), 0, (i, j+1))*(Reward_function((i,j), (i,j+1)) + gamma*Value_of_states[i, j+1])\
                              + Transition_function((i,j), 0, (i, j-1))*(Reward_function((i,j), (i,j-1)) + gamma*Value_of_states[i, j-1]) \
                              + Transition_function((i, j), 0, (i, j)) * (Reward_function((i, j), (i, j)) + gamma * Value_of_states[i, j])

                    temp[1] = Transition_function((i, j), 1, (i + 1, j)) * (
                                Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                              + Transition_function((i, j), 1, (i - 1, j)) * (
                                          Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                              + Transition_function((i, j), 1, (i, j + 1)) * (
                                          Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                              + Transition_function((i, j), 1, (i, j - 1)) * (
                                          Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1]) \
                              + Transition_function((i, j), 1, (i, j)) * (
                                          Reward_function((i, j), (i, j)) + gamma * Value_of_states[i, j])
                    temp[2] = Transition_function((i, j), 2, (i + 1, j)) * (
                                Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                              + Transition_function((i, j), 2, (i - 1, j)) * (
                                          Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                              + Transition_function((i, j), 2, (i, j + 1)) * (
                                          Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                              + Transition_function((i, j), 2, (i, j - 1)) * (
                                          Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1]) \
                              + Transition_function((i, j), 2, (i, j)) * (
                                          Reward_function((i, j), (i, j)) + gamma * Value_of_states[i, j])
                    temp[3] = Transition_function((i, j), 3, (i + 1, j)) * (
                                Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                              + Transition_function((i, j), 3, (i - 1, j)) * (
                                          Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                              + Transition_function((i, j), 3, (i, j + 1)) * (
                                          Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                              + Transition_function((i, j), 3, (i, j - 1)) * (
                                          Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1]) \
                              + Transition_function((i, j), 3, (i, j)) * (
                                          Reward_function((i, j), (i, j)) + gamma * Value_of_states[i, j])
                    action = np.argmax(temp)
                    Value_of_states[i,j] = temp[action]

                    #if iter == iterations -1 and i == 25 and j == 12:
                    #    print((i, j))
                    #    print(temp)
                    #    print(np.argmax(temp))
                    #    print(v)

                    Policy2[i,j] = action
                    delta = np.maximum(delta, np.abs(v-Value_of_states[i,j]))
        if delta < theta:
            break
        iter = iter + 1
        print("Iteration completed:-")
        print(iter)

        #if iter == iterations:
        #    break

    #policy:
    Policy = np.zeros((50,25))
    for i in range(1,49):
        for j in range(1,24):
            if i in [25,26] and j in range(1,12) or i in [25,26] and j in range(13,24):
                Policy[i,j] = None
            else:
                temp = np.zeros(4)
                temp[0] = Transition_function((i, j), 0, (i + 1, j)) * (
                        Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                      + Transition_function((i, j), 0, (i - 1, j)) * (
                                  Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                      + Transition_function((i, j), 0, (i, j + 1)) * (
                                  Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                      + Transition_function((i, j), 0, (i, j - 1)) * (
                                  Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1]) \
                      + Transition_function((i, j), 0, (i, j)) * (
                                      Reward_function((i, j), (i, j)) + gamma * Value_of_states[i, j])

                temp[1] = Transition_function((i, j), 1, (i + 1, j)) * (
                    Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                      + Transition_function((i, j), 1, (i - 1, j)) * (
                              Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                      + Transition_function((i, j), 1, (i, j + 1)) * (
                              Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                      + Transition_function((i, j), 1, (i, j - 1)) * (
                              Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1]) \
                      + Transition_function((i, j), 1, (i, j)) * (
                                      Reward_function((i, j), (i, j)) + gamma * Value_of_states[i, j])

                temp[2] = Transition_function((i, j), 2, (i + 1, j)) * (
                    Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                      + Transition_function((i, j), 2, (i - 1, j)) * (
                              Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                      + Transition_function((i, j), 2, (i, j + 1)) * (
                              Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                      + Transition_function((i, j), 2, (i, j - 1)) * (
                              Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1]) \
                          + Transition_function((i, j), 2, (i, j)) * (
                                      Reward_function((i, j), (i, j)) + gamma * Value_of_states[i, j])

                temp[3] = Transition_function((i, j), 3, (i + 1, j)) * (
                    Reward_function((i, j), (i + 1, j)) + gamma * Value_of_states[i + 1, j]) \
                      + Transition_function((i, j), 3, (i - 1, j)) * (
                              Reward_function((i, j), (i - 1, j)) + gamma * Value_of_states[i - 1, j]) \
                      + Transition_function((i, j), 3, (i, j + 1)) * (
                              Reward_function((i, j), (i, j + 1)) + gamma * Value_of_states[i, j + 1]) \
                      + Transition_function((i, j), 3, (i, j - 1)) * (
                              Reward_function((i, j), (i, j - 1)) + gamma * Value_of_states[i, j - 1]) \
                          + Transition_function((i, j), 3, (i, j)) * (
                                      Reward_function((i, j), (i, j)) + gamma * Value_of_states[i, j])
                #if i == 2 and j == 23:
                #    print(temp)
                #    print(np.argmax(temp))
                optimal_action = np.argmax(temp)
                Policy[i,j] = optimal_action


    return Value_of_states, Policy, Policy2


Value_of_state, Policy, Policy2 = Value_iteration((48,12), 0.1, 0.94, 1000)






from PIL import Image
Image_value = (255 * (Value_of_state - np.min(Value_of_state)) / np.ptp(Value_of_state)).astype(int)
im = Image.fromarray(Image_value)
resized_img = im.resize((400, 800))
resized_img.show()
resized_img .save('gfg_dummy_pic.png')


Policy2_image = np.zeros((48,23,3), dtype= np.uint8)
for ki in range(1,49):
    for kj in range(1,24):
        if Policy2[ki,kj] == 0:
            Policy2_image[ki-1, kj-1] = [255, 0,0]
        elif Policy2[ki,kj] == 1:
            Policy2_image[ki-1, kj-1] = [0,255, 0]
        elif Policy2[ki, kj] == 2:
            Policy2_image[ki - 1, kj - 1] = [0,0,255]
        elif Policy2[ki,kj] == 0:
            Policy2_image[ki-1, kj-1] = [255, 255,255]
img2 = Image.fromarray(Policy2_image, 'RGB')
resized_img2 = img2.resize((200, 400))
resized_img2.show()
resized_img2.save('Policy.png')


with np.printoptions(threshold=np.inf):
    #print(Policy[1:49, 1:24])
    print(Policy2[1:49, 1:24])

    print(Value_of_state[1:49, 1:24])
    print(Value_of_state[48,12])

