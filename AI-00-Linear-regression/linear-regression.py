import numpy as np
import matplotlib.pyplot as plt

# create array of inputs
x_train = np.array([1,2,3,4,5])
y_train = np.array([2,2,4,4,6])

# linear line equation (w = weight (slope), x = input, b = bias (constant))
def y_model_output(w, x, b):
    y = w*x + b
    return y


# the x_train array length
len = x_train.shape[0]

# initialize y hat array
y_hat = np.zeros(len)

# set parameters for the equation
w = 1
b = 2


for i in range(len):
    y_hat[i] = y_model_output(w,x_train[i],b)
    

# visualize this linear line graph by matplotlib library

# our original data
plt.plot(x_train, y_train, marker='x', c='r',label='Actual Values')

# our prediction from the model
plt.plot(x_train, y_hat, c='b',label='Our Prediction')

plt.show()



