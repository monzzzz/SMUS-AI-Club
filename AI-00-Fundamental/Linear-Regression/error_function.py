import numpy as np
import matplotlib.pyplot as plt 


# ERROR FUNCTION

# error function (Error = 1/(2*m)*sum((y_train-y_hat)^2))
def error(y_train, y_hat):
    len = y_train.shape[0] 
    sumError = 1/(2*len)*np.sum((y_hat - y_train)**2)
    error = 1/(2*len)*sumError
    return error


# error function is 1/(2*m)*(y_train-y_hat)^2 -> 1/(2*m)*(y_train-(x_train*w + b))^2 -> de/dw = 1/m*(y_hat-y_train)*x
def error_derivative_r_w(m, x_train, y_train, y_hat):
    dedw = np.sum((y_hat-y_train)*x_train)/m
    return dedw


# error function is 1/(2*m)*(y_train-y_hat)^2 -> 1/(2*m)*(y_train-(x_train*w + b))^2 -> de/db = 1/m*(y_hat-y_train)
def error_derivative_r_b(m, y_train, y_hat):
    dedb = (np.sum(y_hat-y_train))/m
    return dedb