import numpy as np
import math as mt
actions = {0:"north", 1:"south", 2:"east", 3:"west"}

def Next_state_and_reward(s_t, actual_action, goal_state):
    x_t, y_t = s_t

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
                #print((s_t, -1))
                return (s_t, -1)
            else:
                if next_state[0] == goal_state[0] and next_state[1] == goal_state[1]:
                    #print((next_state, 100))
                    return (next_state, 100)
                else:
                    #print((next_state, 0))
                    return (next_state, 0)


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
                else:
                    v = Value_of_states[i,j]
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
                                    temp[k] += 0.8*(reward + gamma*Value_of_states[x_n, y_n])
                                elif l == 1:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                                elif l == 2:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                                elif l == 3:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                        #south
                        if k == 1:
                            temp[k] = 0
                            for l in range(0,4):
                                next_state, reward = Next_state_and_reward((i,j),l,goal_state)
                                x_n , y_n = next_state
                                if l == 0:
                                    temp[k] += 0.2/3*(reward + gamma*Value_of_states[x_n, y_n])
                                elif l == 1:
                                    temp[k] += 0.8 * (reward + gamma * Value_of_states[x_n, y_n])
                                elif l == 2:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                                elif l == 3:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                        #east
                        if k == 2:
                            temp[k] = 0
                            for l in range(0,4):
                                next_state, reward = Next_state_and_reward((i,j),l,goal_state)
                                x_n , y_n = next_state
                                if l == 0:
                                    temp[k] += 0.2/3*(reward + gamma*Value_of_states[x_n, y_n])
                                elif l == 1:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                                elif l == 2:
                                    temp[k] += 0.8 * (reward + gamma * Value_of_states[x_n, y_n])
                                elif l == 3:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                        #west

                        if k == 3:
                            temp[k] = 0
                            for l in range(0,4):
                                next_state, reward = Next_state_and_reward((i,j),l,goal_state)
                                x_n , y_n = next_state
                                if l == 0:
                                    temp[k] += 0.2/3*(reward + gamma*Value_of_states[x_n, y_n])
                                elif l == 1:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                                elif l == 2:
                                    temp[k] += 0.2/3 * (reward + gamma * Value_of_states[x_n, y_n])
                                elif l == 3:
                                    temp[k] += 0.8 * (reward + gamma * Value_of_states[x_n, y_n])

                    action = np.argmax(temp)
                    Value_of_states[i,j] = temp[action]

                    Policy2[i,j] = action
                    delta = np.maximum(delta, np.abs(v-Value_of_states[i,j]))
        if delta < theta:
            break
        iter = iter + 1
        print("Iteration completed:-")
        print(iter)

        #if iter == iterations:
        #    break




    return Value_of_states, Policy2


Value_of_state, Policy2 = Value_iteration((48,12), 0.1, 0.99, 1000)






from PIL import Image
Image_value = (255 * (Value_of_state - np.min(Value_of_state)) / np.ptp(Value_of_state)).astype(int)
im = Image.fromarray(Image_value)
resized_img = im.resize((400, 800))
resized_img.show()
resized_img .save('gfg_dummy_pic2.png')


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
resized_img2.save('Policy23.png')


with np.printoptions(threshold=np.inf):
    #print(Policy[1:49, 1:24])
    print(Policy2[1:49, 1:24])

    print(Value_of_state[1:49, 1:24])
    print(Value_of_state[48,12])

