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


