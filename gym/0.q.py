import numpy as np
import random as pr
import matplotlib.pyplot as plt

def rargmax(vector):
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return pr.choice(indices)

Q = np.zeros([env.observation_space.n, env.action_space.n])
num_episodes = 2000

rList = []
for i in range(num_episodes):
    state = env.reset()
    rAll = 0
    done = False

    while not done:
        action = rargmax(Q[state, :])
        #state, reward, done, info
        new_state, reward, done, _ = env.step(action)

        Q[state, action] = reward + np.max(Q[new_state, :])

        state = new_state