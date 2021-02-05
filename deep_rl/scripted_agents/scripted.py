import numpy as np
import torch
class fetch_reach_object():
    def __init__(self):
        pass
    def step(self,obs):
        #print(obs)
        action = np.ones((obs.shape[0],4),dtype=np.float32)
        action[:,:3] = (obs[:,3:6]-obs[:,6:9]-torch.tensor([0,0,-0.05]))*5
        return action

    def beta(self,obs):
        d=np.linalg.norm(obs[:,3:6]-obs[:,6:9]-torch.tensor([0,0,-0.0]))
        return np.ones((obs.shape[0],1))*(d<0.06)#(1-np.exp(-d*20))

class fetch_reach_goal():
    def __init__(self):
        pass
    def step(self,obs):
        #print(obs)
        action = np.zeros((obs.shape[0],4),dtype=np.float32)-1
        action[:,:3] = (obs[:,:3]-obs[:,6:9])*4
        return action

    def beta(self,obs):
        d=np.linalg.norm(obs[:,3:6]-obs[:,6:9])
        return np.ones((obs.shape[0],1))*(d>0.05)#*(np.exp(-d*20))

class fetch_grasp():
    def __init__(self):
        pass
    def step(self,obs):
        #print(obs)
        action = np.zeros((obs.shape[0],4),dtype=np.float32)-1
        action[:,:3] = (obs[:,3:6]-obs[:,6:9])*4
        action[:,3] = (np.linalg.norm(obs[:,3:6]-obs[:,6:9])-0.05)
        return action

    def beta(self,obs):
        d=np.linalg.norm(obs[:,3:6]-obs[:,6:9])
        d1=np.linalg.norm(obs[:,3:6]-obs[:,6:9])
        # print(d)
        return np.ones((obs.shape[0],1))*((d>0.07)+(d<0.02))#*(np.exp(-d*20))
