import numpy as np
import matplotlib.pyplot as plt

# model with only 1 parameter

# create array of inputs
x_train = np.array([1,2,3,4,5])
y_train = np.array([2,2,4,4,6])

# linear line equation y = wx + b (w = weight (slope), x = input, b = bias (constant))
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
plt.scatter(x_train, y_hat, c='b',label='Our Prediction')

plt.show()


# error function (Error = 1/(2*m)*sum((y_train-y_hat)^2))
def error(y_train, y_hat):
    len = y_train.shape[0] 
    sumError = 0
    for i in range(len):
        sumError  += (y_train[i]-y_hat[i])**2
    error = 1/(2*len)*sumError
    return error


# error function is 1/(2*m)*(y_train-y_hat)^2 -> 1/(2*m)*(y_train-(x_train*w + b))^2 -> de/dw = 1/m*(y_train-y_hat)*x
def error_derivative_r_w(m, x, y_train, y_hat):
    dedw = 1/m*(y_train-y_hat)*x
    return dedw
    
# error function is 1/(2*m)*(y_train-y_hat)^2 -> 1/(2*m)*(y_train-(x_train*w + b))^2 -> de/db = 1/m*(y_train-y_hat)
def error_derivative_r_b(m, y_train, y_hat):
    dedb = 1/m*(y_train-y_hat)
    return dedb
    


