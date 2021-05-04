import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as shapes

actions = {0:"north", 1:"south", 2:"east", 3:"west"}
orientation_dict = {"north":"down", "south":"up", "east":"right", "west":"left"}
goal_state = (48,12)
def move(x, y, a):
    
    if a == 0:
        return x, y + 1
    elif a == 1:
        return x, y - 1
    elif a == 2:
        return x + 1, y
    elif a == 3:
        return x - 1, y

def plot_policy(P, V, orientation_dict = orientation_dict, overlay=False):
    #P - policy, V - value function
    assert P.shape[0] == 25 and P.shape[1] == 50, "Improper input to the function"
    assert P.shape == V.shape, "Improper input to the function"
    V -= np.min(V)
    V /= np.max(V)
    _, ax = plt.subplots()
    for y in range(25):
        for x in range(50):
            #color the walls
    
            if(x > 0 and x < 49 and y > 0 and y < 24 and not (x in [25,26] and y in range(1,12) or x in [25,26] and y in range(13,24))):
                if(overlay):
                    marker = shapes.Rectangle((x, y), width=1, height=1, color=f'{V[y, x]}', alpha=0.5)
                    ax.add_artist(marker)
                x_, y_ = move(x, y, P[y, x])
                if P[y, x] == 0:
                    ax.arrow(x + 0.5, y, x_-x, y_-y, width=0.1, length_includes_head=True, color='red')
                elif P[y, x] == 1:
                    ax.arrow(x + 0.5, y + 1, x_-x, y_-y, width=0.1, length_includes_head=True, color='red')
                elif P[y, x] == 2:
                    ax.arrow(x, y + 0.5, x_-x, y_-y, width=0.1, length_includes_head=True, color='red')
                elif P[y, x] == 3:
                    ax.arrow(x + 1, y + 0.5, x_-x, y_-y, width=0.1, length_includes_head=True, color='red')
            else:
                if(x == goal_state[1] and y == goal_state[0]):
                    marker = shapes.Rectangle((x, y), width=1, height=1, color='red')
                else:    
                    marker = shapes.Rectangle((x, y), width=1, height=1, color='blue')
                ax.add_artist(marker)
    
    ax.set_xticks(np.arange(0, 50, 1))
    ax.set_yticks(np.arange(0, 25, 1))
    ax.grid(b=True, which='major')
    ax.set_title('Policy Plot')

    plt.show()

def plot_policy2(P, V, orientation_dict = orientation_dict, grid=False, title='Policy Plot'):
    #P - policy, V - value function
    assert P.shape[0] == 25 and P.shape[1] == 50, "Improper input to the function"
    assert P.shape == V.shape, "Improper input to the function"
    _, ax = plt.subplots()
    ax.imshow(V)
    for y in range(25):
        for x in range(50):
            #color the walls
    
            if(x > 0 and x < 49 and y > 0 and y < 24 and not (x in [25,26] and y in range(1,12) or x in [25,26] and y in range(13,24))):
                x_, y_ = move(x, y, P[y, x])
                if P[y, x] == 0:
                    ax.arrow(x, y-0.5, x_-x, y_-y, width=0.1, length_includes_head=True, color='red')
                elif P[y, x] == 1:
                    ax.arrow(x, y + 0.5, x_-x, y_-y, width=0.1, length_includes_head=True, color='red')
                elif P[y, x] == 2:
                    ax.arrow(x-0.5, y, x_-x, y_-y, width=0.1, length_includes_head=True, color='red')
                elif P[y, x] == 3:
                    ax.arrow(x + 0.5, y, x_-x, y_-y, width=0.1, length_includes_head=True, color='red')
    
    ax.set_xticks(np.arange(0, 50, 1))
    ax.set_yticks(np.arange(0, 25, 1))
    if(grid):
        ax.grid(b=True, which='major')
    ax.set_title(title)

    plt.show()
    