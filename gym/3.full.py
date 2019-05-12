import numpy as np
import random as pr
import matplotlib.pyplot as plt

import gym
from gym.envs.registration import register

import tensorflow as tf

def rargmax(vector):
    # 가장 큰 값 중 랜덤하게 반환
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return pr.choice(indices)

def one_hot(x):
    return np.identify(16)[x:x + 1]
    
register(
    id="FrozenLake-v3",
    entry_point="gym.envs.toy_text:FrozenLakeEnv",
    kwargs={"map_name" : "4x4"}
)

env = gym.make("FrozenLake-v0")

input_size = env.observation_space.n
output_size = env.action_space.n
learning_rate = 0.1

## make network
X = tf.placeholder(shape=[1, input_size], dtype=tf.float32)
W = tf.Variable(tf.random_uniform([input_size, output_size, 0, 0.01]))
Qpred = tf.matmul(X, W)
Y = tf.placeholder(shape=[1, output_size], dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y - Qpred))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)


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
        
        # e - greedy
        # e = 0.1 / ((i // 100) + 1)
        # if np.random.rand(1) < e:
        #     action = env.action_space.sample()
        # else:
        #     action = rargmax(Q[state, :])

        ## OR

        # decaying
        action = np.argmax(Q[state, :] + np.random.randn(1, env.action_space.n) / ( i + 1))
        
        #state, reward, done, info
        new_state, reward, done, _ = env.step(action)

        # discounted future reward
        dis = 0.99
        # Q table 추가
        #Q[state, action] = reward + dis * np.max(Q[new_state, :])

        learning_rate = 0.85
        Q[state, action] = (1-learning_rate) * Q[state, action] \
            + learning_rate * (reward + dis * np.max(Q[new_state, :]))

        rAll += reward
        state = new_state
    
    rList.append(rAll)

#print

print("Success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print("Left Down Right Up")
print(Q)

plt.bar(range(len(rList)), rList, color="blue")
plt.show()