import numpy as np
import tensorflow as tf

import gym
env = gym.make('CartPole-v0')

input_size = env.observation_space.shape[0] # 4
output_size = env.action_space.n            # 2


X = tf.placeholder(tf.float32, [None, input_size], name = "input_x") # None, input_size = [1, 4]

# First layer of weights
W1 = tf.get_variable("W1", shape=[input_size, output_size], 
                        initializer = tf.contrib.layers.xavier_initializer()) #샤이비에

Qpred = tf.matmul(X, W1)

# parts of the network => need for learning  a policy
Y = tf.placeholder(shape=[None, output_size], dtype=tf.float32)

# loss function
loss = tf.reduce_sum(tf.square(Y - Qpred))

learning_rate = 1e-1
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

num_episodes = 2000
dis = 0.9
rList = []

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(num_episodes):
        e = 1. / ((i// 10) + 1)
        rAll = 0
        step_count = 0
        s = env.reset()
        done = False

        # Q-Net train
        while not done:
            step_count += 1
            x = np.reshape(s, [1, input_size]) # preprocess pi

            # random or Q-net
            Qs = sess.run(Qpred, feed_dict = {X:x})
            if np.random.rand(1) < e:
                a = env.action_space.sample()
            else:
                a = np.argmax(Qs)
            
            s1, reward, done, _ = env.step(a)

            if done:
                Qs[0, a] = -100 # get negative
            else:
                x1 = np.reshape(s1, [1, input_size])

                # Obtain Q' value (new_state(x) => Qpred)
                Qs1 = sess.run(Qpred, feed_dict={X: x1})
                Qs[0, a] = reward + dis * np.max(Qs1)
            
            # Train it (target, Qs)
            sess.run(train, feed_dict={X:x, Y:Qs})
            s = s1
        
        rList.append(step_count)
        print("Episdoe: {} steps: {}".format(i, step_count))

        if len(rList) > 10 and np.mean(rList[-10:]) > 500:
            break
    
    # see in action, let's test it
    observation = env.reset()
    reward_sum = 0
    while True:
        env.render()

        x = np.reshape(observation, [1, input_size])
        Qs = sess.run(Qpred, feed_dict= {X:x})
        a = np.argmax(Qs)

        observation, reward, done, _ = env.step(a)
        reward_sum += reward
        if done:
            print("total score: {}".format(reward_sum))
            break