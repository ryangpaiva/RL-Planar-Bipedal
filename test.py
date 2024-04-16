import gymnasium as gym
import gym_examples

from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.logger import Figure

env = gym.make('gym_examples/bipedal-v0', render_mode="human")
model = PPO('MlpPolicy', env, verbose=1, device='cuda')


model = PPO.load('gym_examples/bipedal-v0', env=env, tensorboard_log="./gym_examples/")
obs = env.reset()[0]
done = False
extra_steps = 500
while True:
        action, _ = model.predict(obs)
        obs, _, done, _, _ = env.step(action)

        if done:
            extra_steps -= 1

            if extra_steps < 0:
                break