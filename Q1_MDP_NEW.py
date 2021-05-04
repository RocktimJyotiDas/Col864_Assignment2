import numpy as np
import math as mt
import matplotlib.pyplot as plt 
from plotpolicy import plot_policy, plot_visited
from mdputils import Next_state_and_reward
from simulatepolicy import plot_simulation, simulate_policy
actions = {0:"north", 1:"south", 2:"east", 3:"west"}

#Value_Iteration
def Value_iteration(goal_state= (48,12), theta=0.1, gamma=0.1, iterations =10):
    
    V_history = {}
    delta_history = []
    change_history = []
    V = np.zeros((50,25))
    #V[1:49,1:24] = np.random.randn(48,23)
    x_goal, y_goal = goal_state
    V[x_goal,y_goal] = 0
    for j in range(25):
        V[0,j] = None
        V[49,j] = None
    
    for i in range(50):
        V[i, 0] = None
        V[i, 24] = None
    iter = 0
    Policy2 = np.zeros((50,25))
    #value_iteration
    while(True):
        
        n_changes = 0
        delta = 0
        
        print(f'Iteration {iter}:', end=' ')
        for i in range(1, 49):
            for j in range(1, 24):
                if i in [25,26] and j in range(1,12) or i in [25,26] and j in range(13,24):
                    V[i,j] = None
                    Policy2[i,j] = None

                else:
                    v = V[i,j]
                    temp = np.zeros(4)
                    for k in range(0,4):
                        #north
                        if k == 0:
                            temp[k] = 0
                            #get the reward and next state according to every stochastic next state and find values of the states
                            for l in range(0,4):
                                #print((i,j))
                                #print(l)
                                next_state, reward = Next_state_and_reward((i,j),l,goal_state)
                                #print(next_state)
                                x_n , y_n = next_state
                                #print(x_n)
                                if l == 0:
                                    temp[k] += 0.8*(reward + gamma*V[x_n, y_n])
                                elif l == 1:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                                elif l == 2:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                                elif l == 3:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                        #south
                        if k == 1:
                            temp[k] = 0
                            for l in range(0,4):
                                next_state, reward = Next_state_and_reward((i,j),l,goal_state)
                                x_n , y_n = next_state
                                if l == 0:
                                    temp[k] += 0.2/3*(reward + gamma*V[x_n, y_n])
                                elif l == 1:
                                    temp[k] += 0.8 * (reward + gamma * V[x_n, y_n])
                                elif l == 2:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                                elif l == 3:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                        #east
                        if k == 2:
                            temp[k] = 0
                            for l in range(0,4):
                                next_state, reward = Next_state_and_reward((i,j),l,goal_state)
                                x_n , y_n = next_state
                                if l == 0:
                                    temp[k] += 0.2/3*(reward + gamma*V[x_n, y_n])
                                elif l == 1:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                                elif l == 2:
                                    temp[k] += 0.8 * (reward + gamma * V[x_n, y_n])
                                elif l == 3:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                        #west

                        if k == 3:
                            temp[k] = 0
                            for l in range(0,4):
                                next_state, reward = Next_state_and_reward((i,j),l,goal_state)
                                x_n , y_n = next_state
                                if l == 0:
                                    temp[k] += 0.2/3*(reward + gamma*V[x_n, y_n])
                                elif l == 1:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                                elif l == 2:
                                    temp[k] += 0.2/3 * (reward + gamma * V[x_n, y_n])
                                elif l == 3:
                                    temp[k] += 0.8 * (reward + gamma * V[x_n, y_n])

                    action = np.argmax(temp)
                    V[i,j] = temp[action]

                    if(action != Policy2[i,j]):
                        Policy2[i,j] = action
                        n_changes += 1
                    delta = np.maximum(delta, np.abs(v-V[i,j]))
        
        change_history.append(n_changes)
        if theta is None:
            pass
        elif delta < theta:
            break
        iter = iter + 1
        
        V_history[iter] = V.copy()
        delta_history.append(delta)

        print("Iteration completed.")
        #print(iter)

        if iter == iterations:
            break




    return V, Policy2, V_history, delta_history, change_history


Value_of_state, Policy2, V_history, delta_hist, c = Value_iteration((48,12), 0.1, 0.99, 100)

fig, ax = plt.subplots()
ax.imshow(Value_of_state.T, cmap='gray')
ax.set_title("Value function with discount factor of 0.1")
plt.show()

try:
    fig, ax = plt.subplots()
    ax.imshow(V_history[20].T, cmap='gray'); ax.set_title("After 20 iterations")
    plt.show()

    fig, ax = plt.subplots()
    ax.imshow(V_history[50].T, cmap='gray'); ax.set_title("After 50 iterations")
    plt.show()

    fig, ax = plt.subplots()
    ax.imshow(V_history[100].T, cmap='gray'); ax.set_title("After 100 iterations")
    plt.show()

except Exception:
    print("Oops")
    
plot_policy(Policy2.T, Value_of_state.T)

#simulating the policy
states, actions, rewards = simulate_policy(start_state = (1, 1), P=Policy2, iter=200)
plot_simulation(states, actions)

#visualizing how many times a state has been visitied
N_times = 200
n_visited = np.zeros((50,25))
for n in range(N_times):
    states, actions, rewards = simulate_policy((1,1), Policy2, 100)
    for s in states:
        n_visited[s[0], s[1]] += 1
'''
plt.imshow(n_visited.T, cmap='gray')
plt.show()

n_visited[48, 12] = 0
plt.imshow(n_visited.T, cmap='gray')
plt.show()
'''
plot_visited(n_visited)
#now visualizing how max_norm changes over different values of gamma.
fig, ax = plt.subplots(1, 2)
Value_of_state, Policy2, V_history, delta_hist, c = Value_iteration((48,12), None, 0.99, 500)
ax[0].plot(delta_hist, 'r'); ax[1].plot(c, 'r')
Value_of_state, Policy2, V_history, delta_hist, c = Value_iteration((48,12), None, 0.01, 500)
ax[0].plot(delta_hist, 'b'); ax[1].plot(c, 'b')

ax[0].set_title("Max_norm over different values of the discount factor: 0.99 and 0.01")
ax[1].set_title("Changes in the policy over different iterations")
plt.show()