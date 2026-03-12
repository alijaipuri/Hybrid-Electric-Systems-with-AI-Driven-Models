from stable_baselines3 import PPO
from env.hev_env import HEVEnv
from config import *

env = HEVEnv()

model = PPO("MlpPolicy",env,verbose=1)

model.learn(total_timesteps=TIMESTEPS)

model.save(MODEL_PATH)

print("Training Complete")
