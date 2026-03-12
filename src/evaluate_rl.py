from stable_baselines3 import PPO
from env.hev_env import HEVEnv
from config import *

env = HEVEnv()

model = PPO.load(MODEL_PATH)

obs,_ = env.reset()

score = 0

for i in range(200):

    action,_ = model.predict(obs)

    obs,reward,done,_,_ = env.step(action)

    score += reward

print("Episode Score:",score)
