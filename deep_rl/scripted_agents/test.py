import gym
import numpy as np
def agent(D):
    obs = np.concatenate([D['desired_goal'],D['achieved_goal'],D['observation']])
    action = np.zeros((4,),dtype=np.float)
    action[:3] = (D['desired_goal']-D['observation'][:3])*1
    return action

if __name__ == "__main__":
    env = gym.make(id="FetchPickAndPlaceDense-v1")

    N=1000
    obs = env.reset()
    for i in range(N):
        action = agent(obs)
        obs,b,c,d = env.step(action)

        env.render()
