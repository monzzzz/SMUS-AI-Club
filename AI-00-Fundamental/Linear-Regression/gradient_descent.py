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
cost_list = np.zeros(t)

for i in range(len):
    y_hat[i] = introduction.y_model_output(w, x_train[i] ,b)

def gradient_descent(x_train, y_train, y_hat, a, w, b, t):
    w = w
    b = b
    y_hat = w*x_train + b
    weight_list = np.zeros(t)
    bias_list = np.zeros(t)
    for i in range(t):
        w = w - a*(error_function.error_derivative_r_w(len, x_train, y_train, y_hat))
        b = b - a*(error_function.error_derivative_r_b(len, y_train, y_hat))
        y_hat = w*x_train + b
        cost_list[i] = error_function.error(y_train, y_hat)
        weight_list[i] = w
        bias_list[i] = b
    return weight_list, bias_list

weight_list, bias_list = gradient_descent(x_train, y_train, y_hat, a, w, b, t)
print(weight_list[4999])
print(bias_list[4999])


# Progress for each variable (including bias, weight, and error)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1) # row, column, order
plt.plot(weight_list, label='Weight')
plt.xlabel('Iteration')
plt.ylabel('Weight')
plt.title('Weight Progression')
plt.legend()

# Plotting the bias progression
plt.subplot(1, 3, 2)
plt.plot(bias_list, label='Bias', color='green')
plt.xlabel('Iteration')
plt.ylabel('Bias')
plt.title('Bias Progression')
plt.legend()

# Plotting the cost (error) progression
plt.subplot(1, 3, 3)
plt.plot(cost_list, label='Cost', color='red')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.title('Cost Progression')
plt.legend()

plt.tight_layout()
plt.show()



# Visualize the path of the model progression

fig = plt.figure(figsize=(10, 7)) # the size of the figure
ax = fig.add_subplot(111, projection='3d')

# Plotting weight, bias, and cost
ax.plot(weight_list, bias_list, cost_list, label='Cost Evolution', color='red')

# Adding labels and title
ax.set_xlabel('Weight')
ax.set_ylabel('Bias')
ax.set_zlabel('Cost')
ax.set_title('3D Plot of Weight, Bias, and Cost Evolution')

# Show legend
ax.legend()

plt.show()