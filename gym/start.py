import gym
from gym.envs.registration import register
import sys, tty, termios

class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

inkey = _Getch()

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3
arrow_keys = {
    '\x1b[A': UP,
    '\x1b[B': DOWN,
    '\x1b[C': RIGHT,
    '\x1b[D': LEFT,
}

register(
    id="FrozenLake-v3",
    entry_point="gym.envs.toy_text:FrozenLakeEnv",
    kwargs={"map_name" : "4x4", "is_slippery" : False}
)

env = gym.make("FrozenLake-v3")
observation = env.reset()

for _ in range(1000):
    key = inkey()
    if key not in arrow_keys.keys():
        print("Abort")
        break
    action = arrow_keys[key]
    
    #action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print("state: ", observation, "action: ", action, "reward ", reward, "info:", info)
    env.render()

    if done:
        print("Finished with reward", reward)
        break

