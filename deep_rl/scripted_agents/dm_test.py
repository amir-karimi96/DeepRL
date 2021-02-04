from scripted import *
import gym
import numpy as np

a = globals()['fetch_reacher']


if __name__ == "__main__":
    env = gym.make(id="FetchPickAndPlaceDense-v1")

    N=1000
    obs = env.reset()
    for i in range(N):
        action = a(obs)
        obs,b,c,d = env.step(action)

        env.render()
