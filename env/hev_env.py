import gymnasium as gym
from gymnasium import spaces
import numpy as np

class HEVEnv(gym.Env):

    def __init__(self):

        super(HEVEnv,self).__init__()

        self.observation_space = spaces.Box(
            low=np.array([0,0,0]),
            high=np.array([120,100,100]),
            dtype=np.float32
        )

        self.action_space = spaces.Discrete(3)

        self.state = np.array([50,80,30],dtype=np.float32)

    def step(self,action):

        speed,battery,temp = self.state

        efficiency = battery/100 - temp/200

        noise = speed/2 + action*5

        reward = efficiency*10 - noise/50

        self.state = self.state + np.random.randn(3)

        done = False

        return self.state,reward,done,False,{}

    def reset(self,seed=None,options=None):

        self.state = np.array([50,80,30],dtype=np.float32)

        return self.state,{}

    def render(self):
        pass
