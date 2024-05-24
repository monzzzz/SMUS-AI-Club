import numpy as np
import matplotlib.pyplot as plt
import json


# open the json file to get data
with open("./data.json") as file:
    data = json.load(file)

# model with only 1 parameter

# create array of inputs
x_train = np.array(data["x"])
y_train = np.array(data["y"])

# linear line equation y = wx + b (w = weight (slope), x = input, b = bias (constant))
def y_model_output(w, x, b):
    y = w*x + b
    return y


# the x_train array length
len = x_train.shape[0]

# initialize y hat array
y_hat = np.zeros(len)

# set parameters for the equation
w = 2.5308100281529797
b = -0.37734119808178146


for i in range(len):
    y_hat[i] = y_model_output(w,x_train[i],b)
    

# visualize this linear line graph by matplotlib library

# our original data
plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

# our prediction from the model
plt.plot(x_train, y_hat, c='b',label='Our Prediction')

plt.show()



    


