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

# 모든 결과의 저장
rList = []

with tf.Session() as sess:
    sess.run(init)

    for i in range(num_episodes):
        s = env.reset()
        e = 1. / ((i // 50) + 10)
        rAll = 0
        done = False

    while not done:
        
        Qs = sess.run(Qpred, feed_dict={X: one_hot(s)})
        
        if np.random.rand(1) < e:
            a = env.action_space.sample()
        else:
            a = np.argmax(Qs)

        # step
        s1, reward, done, _ = env.step(a)

        
        # discounted future reward
        dis = 0.99
        # Q table 추가
        #Q[state, action] = reward + dis * np.max(Q[new_state, :])
        if done:
            Qs[0, a] = reward
        else:
            Qs1 = sess.run(Qpred, feed_dict={X: one_hot(s1)})

            Qs[0, a] = reward + dis * np.max(Qs1)]

        sess.run(train, feed_dict={X:one_hot(s), Y: Qs})

        rAll += reward
        s = s1

    rList.append(rAll)

#print

print("Success rate: " + str(sum(rList)/num_episodes))
print("Final Q-Table Values")
print("Left Down Right Up")
print(Q)

plt.bar(range(len(rList)), rList, color="blue")
plt.show()