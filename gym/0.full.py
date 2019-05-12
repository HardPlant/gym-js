import numpy as np
import random as pr
import matplotlib.pyplot as plt

import gym
from gym.envs.registration import register


def rargmax(vector):
    # 가장 큰 값 중 랜덤하게 반환
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return pr.choice(indices)

register(
    id="FrozenLake-v3",
    entry_point="gym.envs.toy_text:FrozenLakeEnv",
    kwargs={"map_name" : "4x4", "is_slippery" : False}
)

env = gym.make("FrozenLake-v3")
observation = env.reset()

# table to wzro
Q = np.zeros([env.observation_space.n, env.action_space.n])
num_episodes = 2000

# 모든 결과의 저장
rList = []
for i in range(num_episodes):
    state = env.reset()
    rAll = 0
    done = False

    while not done:
        action = rargmax(Q[state, :])
        #state, reward, done, info
        new_state, reward, done, _ = env.step(action)

        # Q table 추가
        Q[state, action] = reward + np.max(Q[new_state, :])

        rAll += reward
        state = new_state
    
    rList.append(rAll)

#print

print("Success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print("Left Down Right Up")
print(Q)

plt.bar(range(len(rList)), rList, color="blue")
plt.show