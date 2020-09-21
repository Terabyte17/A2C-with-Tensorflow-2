# A2C with Tensorflow 2
One of the key concepts in Reinforcement Learning is Advantage Actor Critic or A2C which has an actor and a critic which train a neural network to learn a policy directly. This procedure also involves a network for predicting the value function. Although A2C has been implemented by many people, with the Stable Baselines and OpenAI Baselines being very popular, I wanted to implement A2C on my own to get to know more about how we can implement DeepRL techniques using Tensorflow and Keras. 

There are many open source implementations of the algorithm, but, most of them are in tensorflow 1.x. Hence, the code in this repository is written in Tensorflow 2.x, and while writing the code it was more about getting to know new Tensorflow functionalities and their power rather than the algorithm which is actually pretty straightforward. I tested the A2C algorithm on the CartPole environment given by OpenAI, an environment in which the reward is based on what is the angle between the cartpole and the vertical. If it exceeds a paricular value or goes out of the frame, the episode terminates. The maximum reward in the environment is 200.

The algorithm upon training for nearly 500 episodes, was able to perform sufficiently well during test time and most of the times it got a reward of 200. This is only the first draft and I'll hopefully optimize it to give better results.

Following are the results from <b>training</b> and <b>testing</b>:
<p align="center">
<h3 align="center">Training Results</h3>
</p>
<p align="center">
<img src="https://github.com/Terabyte17/A2C-with-Tensorflow-2/blob/master/media/training%20results.png" height="400" width="600"/>
</p>
<h3 align="center">Test Results</h3>
<p align="center">
<img src="https://github.com/Terabyte17/A2C-with-Tensorflow-2/blob/master/media/test%20results.png" height="400" width="600"/>
</p>
<h3 align="center">Model's performance</h3>
<p align="center">
<img align="center" src="https://github.com/Terabyte17/A2C-with-Tensorflow-2/blob/master/media/test.gif" height="400" width="600"/>
</p>
