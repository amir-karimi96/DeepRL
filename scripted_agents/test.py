import gym
import numpy as np
def agent(obs):
    action = np.zeros((4,))
    action[:3] = (obs['achieved_goal']-obs['observation'][:3])*1
    return action

if __name__ == "__main__":
    env = gym.make(id="FetchPickAndPlaceDense-v1")

    N=1000
    obs = env.reset()
    for i in range(N):
        action = agent(obs)
        obs,b,c,d = env.step(action)

        env.render()
