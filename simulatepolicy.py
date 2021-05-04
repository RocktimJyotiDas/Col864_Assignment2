import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as shapes
from mdputils import Next_state_and_reward

def get_distribution(action):
    p = np.array([0.2/3, 0.2/3, 0.2/3, 0.2/3])
    p[action] = 0.8
    return p

def simulate_policy(start_state, P, iter=200):
    x, y = start_state
    states = [(x, y)]
    rewards = []
    actions = []
    for i in range(iter):
        action = np.random.choice(np.array([0,1,2,3]), p = get_distribution(int(P[x, y])))
        actions.append(action)
        next_state, reward = Next_state_and_reward((x, y), action, (48, 12))
        states.append(next_state)
        rewards.append(reward)
        x, y = next_state
    return states, actions, rewards



def plot_simulation(states, actions, goal_state=(48, 12), outdir=None, plot=True):
    _, ax = plt.subplots()
    
    for y in range(25):
        for x in range(50):
            #color the walls
            
            if(x > 0 and x < 49 and y > 0 and y < 24 and not (x in [25,26] and y in range(1,12) or x in [25,26] and y in range(13,24))):
                continue
            else:
                if(x == goal_state[1] and y == goal_state[0]):
                    marker = shapes.Rectangle((x, y), width=1, height=1, color='red')
                else:    
                    marker = shapes.Rectangle((x, y), width=1, height=1, color='black')
                ax.add_artist(marker)
    
    for i in range(len(states)-1):
            x, y = states[i]
            x_, y_ = states[i + 1]
            P = actions[i]
            
            if P == 0:
                ax.arrow(x + 0.5, y, x_-x, y_-y, width=0.1, length_includes_head=True)
            elif P == 1:
                ax.arrow(x + 0.5, y + 1, x_-x, y_-y, width=0.1, length_includes_head=True)
            elif P == 2:
                ax.arrow(x, y + 0.5, x_-x, y_-y, width=0.1, length_includes_head=True)
            elif P == 3:
                ax.arrow(x + 1, y + 0.5, x_-x, y_-y, width=0.1, length_includes_head=True)
    
    ax.set_xticks(np.arange(0, 50, 1))
    ax.set_yticks(np.arange(0, 25, 1))
    ax.set_xlim([0,50])
    ax.set_ylim([0,25])
    ax.grid(b=True, which='major')
    ax.set_title('Policy Plot')
    if outdir is not None:
        plt.savefig(outdir, dpi=300)
    if plot:
        plt.show()
    

