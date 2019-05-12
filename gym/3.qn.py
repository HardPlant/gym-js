## one_hot
def one_hot(x):
    return np.identify(16)[x:x + 1]

## make network
input_size = env.observation_space.n
output_size = env.action_space.n
learning_rate = 0.1

X = tf.placeholder(shape=[1, input_size], dtype=tf.float32)
W = tf.Variable(tf.random_uniform([input_size, output_size, 0, 0.01]))
Qpred = tf.matmul(X, W)
Y = tf.placeholder(shape=[1, output_size], dtype=tf.float32)

loss = tf.reduce_sum(tf.square(Y - Qpred))
train = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(loss)

## train

Qs[0, a] = reward + dis * np.max(Qs1)
sess.run(train, feed_dict={X: one_hot(s), Y: Qs})

## algorithm

Qs = sess.run(Qpred, feed_dict={X: one_hot(s)})

if np.random.rand(1) < e:
    a = env.action_space.sample()
else:
    a = np.argmax(Qs)

## make Y label, loss_function

if done:
    Qs[0, a] = reward
else:
    Qs1 = sess.run(Qpred, feed_dict={X: one_hot(s1)})

    Qs[0, a = reward + dis * np.max(Qs1)]
