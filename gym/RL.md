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
