import gymnasium as gym
import gym_examples
import numpy as np
import matplotlib.pyplot as plt

from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.logger import HParam

env = gym.make('gym_examples/bipedal-v0', render_mode="human")
model = PPO('MlpPolicy', env, verbose=1, device='cuda', tensorboard_log="./gym_examples/")

TIMESTEPS = 25000


model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False)

model.save("gym_examples/bipedal-v0.zip")