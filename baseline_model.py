import gymnasium as gym
import gym_examples

from stable_baselines3 import A2C

env = gym.make('gym_examples/bipedal-v0', render_mode="human")
model = A2C('MlpPolicy', env, verbose=1, device='cuda')

TIMESTEPS = 25
iters = 0
while True:
        iters += 1

        model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False)
        model.save("gym_examples/bipedal-v0.zip")

model = A2C.load('gym_examples/bipedal-v0', env=env)
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