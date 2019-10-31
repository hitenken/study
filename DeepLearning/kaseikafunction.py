import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))

def step_funtion(x):
    return np.array(x > 0, dtype=np.int)

def relu(x):
    return np.maximum(0,x)

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
z = step_funtion(x)
l = relu(x)
plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,l)
plt.ylim(-0.1, 3)
plt.show()