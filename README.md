Requisites Gym, Mujoco[version]
```Install or Gym examples package```
```-> alterated on setup.py```
```->alterated on envs.__init__.py```
```-> alterated gym/envs/mujoco/assets -> adds XML of bipedal and STL meshes ```
```Code for MJEnv:```
```https://github.com/openai/gym/blob/master/gym/envs/mujoco/mujoco_env.py```

```REPORT ERROR ON MUJOCO_RENDERING.PY ON MUJOCO 2.3.6```
```YOU CAN USE```
```bottomleft, "Solver iterations", str(self.data.solver_niter + 1)```
```python3 test.py```
```python3 learn.py```
```tensorboard --logdir gym_examples/```
