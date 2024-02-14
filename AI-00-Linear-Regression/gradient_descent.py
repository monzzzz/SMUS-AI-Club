import numpy as np
import matplotlib.pyplot as plt
import json
import introduction
import error_function

# open json file to get data
with open("./data.json") as file:
    data = json.load(file)

# only one type of input

x_train = np.array(data["x"])
y_train = np.array(data["y"])
len = x_train.shape[0]
y_hat = np.zeros(len)

a = 0.01 # alpha
w = 2 # weight
b = -10 # bias
t = 5000

for i in range(len):
    y_hat[i] = introduction.y_model_output(w, x_train[i] ,b)



def gradient_descent(x_train, y_train, y_hat, a, w, b, t):
    w = w
    b = b
    y_hat = w*x_train + b
    for i in range(t):
        w = w - a*(error_function.error_derivative_r_w(len, x_train, y_train, y_hat))
        b = b - a*(error_function.error_derivative_r_b(len, y_train, y_hat))
        y_hat = w*x_train + b
        print(f"round{i+1} w = {w}, b = {b}")
    
gradient_descent(x_train, y_train, y_hat, a, w, b, t)