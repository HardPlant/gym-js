# RL

## Dummy Q Table

## Exploit/Exploration

* E-greedy ()

e = random()

* decaying E-greedy

e = 0.1 / (i+1)
탐험 확률 줄이기

..random (episode와 독립)

* add random noise

a = argmax(Q(state,action) + random_values)

= >

a = argmax(q(state, action) + random_values / (i+1))

## Discounted future reward

gamma = 0.9
Q(s,a) = r + gamma * argmax(q(s', a'))

## Deterministic / Stochastic (Non-deterministic)

Stochastic ->
Q(s') little bit
update Q(s) little bit(learning rate)
Many mantor (not one mentor)

## Q-Learning

Q(s,a) = (1-lr)Q(s,a) + lr(r + gamma(argmax(Q(s,a'))))

## Q-Network

(s,a) => q
를 반환하는 NN

### linear regression

H(x) = Wx

Ws = Qs*

cost(W) = (Ws - y)^2, y = r + gamma*max(Q(s'))


W[s] = pred(Q(s,a) | theta) =~ Q&(s, a)

## QN

Q = random(W)
for episode= 1..M
    # pi near= s (전처리가 없을 경우)
    seq[1] = {x[1]}, preprocessed seq pi[1] = pi[s[1]]
    
    for t= 1..T
        E => random_action()
        Not(E) => maxarg(a, Q(pi), a;theta)

        execute(a) => 
        set s[t+1] = s[t], a[t], x

y label = if terminal(pi[j+1]) r[j] else r[j] + gamma*maxarg(a', Q(pi[j+1], a';theta))
loss function => gradient descent step
(y[j]-Q(pi[j],a[j];theta))^2

* no learning rate (1-lr)(Q(s,a)) + lr*()
.. gradient descent가 학습을 대신 함

min(theta, sum(t=>0, )
diverges => Deep, Replay, Separaed Network (DQN)

## 입력과 출력 설계

One-hot .. 1자리만 사용함 , pi = one_hot된 s

one_hot(x)=>{return np.identity(16)[x:x,1]}

state 7 -> one-hot(7)
np.identify(16)[s1:s1 + 1] # index, [16][1]

in[16] => out[4]

### Stable?

결과가 그렇게 좋지는 않음

* Minibatch

## CartPole

```
import gym
env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
```

### NN의 장점

input에 대한 분석 (ob에 대한 분석)을 하지 않아도 됨

```py
s1, reward, done, _ = env.step(a)
if done:
    Qs[0, a] = -100 # 넘어지게 한 행동에 대한 처벌
else:
    x1 = np.reshape(s1, [1, input_size]) # one-hot 불가, 1x4 input으로 만들어줌
    Qs1 = sess.run(Qpred, feed_dict={X:x1})
    Qs[0, a] = reward + dis * np.max(Qs1)
```


### Network

s (length=4) => Ws (action = 2)

```py
input_size = env.observation_space.shape[0] # 4
output_size = env.action_space.n            # 2

X = tf.placeholder(tf.float32, [None, input_size], name = "input_x")

# First layer of weights
W1 = tf.get_variable("W1", shape=[input_size, output_size], 
                        initializer = tf.contrib.layers.xavier_initializer())

Qpred = tf.matmul(X, W1)
```

### Training

```py
Qpred = tf.matmul(X, W1)

# parts of the network => need for learning  a policy
Y = tf.placeholder(shape=[None, output_size], dtype=tf.float32)

# loss function
loss = tf.reduce_sum(tf.sqaure(Y - Qpred))

train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
```

```py
Qs[0, a] = reward + dis * np.max(Qs1)

sess.run(train, feed_dict={X: x, Y: Qs})
```

## Not work

* 4 weight

* diverges

Correlations between samples

인접 데이터간 상관관계가 있어 적합이 제대로 되지 않음

Non-staionary target

Qpred, Target(y)가 같은 네트워크를 사용함
Pred를 수정했더니 Target도 움직임

## DQN

* Go Deep

* Capture/Replay

상태 => 버퍼에 저장 => 랜덤하게 뽑아서 학습

```
store (pi, action, reward, pi') = D
random minibatch from D
```

* Create New network

1) s => Ws
2) s => Y

3) copy (Ws, Y)

target Y <= Q(theta[1])
Y => theta[0]

n step reset theta[1] = theta[0]

### 2013

* Net-Build-Init

* Env
    loop:
        a = e-greedy.. # a = action
        r = env.step(a) # r= reward

        buff.append(r)

        if loop.circle(10):
            minibatch(buff):
                train