import numpy as np
import tensorflow as tf

import gym
env = gym.make('CartPole-v0')
env.reset()

input_size = env.observation_space.shape[0] # 4
output_size = env.action_space.n            # 2


X = tf.placeholder(tf.float32, [None, input_size], name = "input_x")

# First layer of weights
W1 = tf.get_variable("W1", shape=[input_size, output_size], 
                        initializer = tf.contrib.layers.xavier_initializer())

Qpred = tf.matmul(X, W1)

# parts of the network => need for learning  a policy
Y = tf.placeholder(shape=[None, output_size], dtype=tf.float32)

# loss function
loss = tf.reduce_sum(tf.square(Y - Qpred))

learning_rate = 1e-1
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)