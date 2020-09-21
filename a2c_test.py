import os
import numpy as np
import gym
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, Dense, BatchNormalization, Dropout
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.losses import mean_squared_error, SparseCategoricalCrossentropy, CategoricalCrossentropy
from a2c_model import a2c_Model
from a2c_agent import A2CAgent

if __name__ == '__main__':
  env = gym.make('CartPole-v0')
  env.render()
  model = a2c_Model(env.observation_space.shape[0],env.action_space.n)
  agent = A2CAgent(model)
  agent.test_model(env, 'models/model840.h5', 100)
