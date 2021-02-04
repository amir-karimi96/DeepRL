import numpy as np

def fetch_reacher(obs):
    print(obs)
    action = np.zeros((obs.shape[0],4),dtype=np.float32)
    action[:,:3] = (obs[:,:3]-obs[:,6:9])*1
    return action
