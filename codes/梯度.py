import numpy as np
import matplotlib.pyplot as plt
# 定义目标函数
def f(x):
    return x**2
# 定义目标函数的梯度
def df(x):
    return 2 * x
# 梯度下降法
def gradient_descent(initial_x, learning_rate, num_iterations):
    x = initial_x
    for i in range(num_iterations):
        grad = df(x)  # 计算梯度
        x = x - learning_rate * grad  # 更新参数
        print(f"Iteration {i+1}: x = {x}, f(x) = {f(x)}")
    return x
# 初始化参数
initial_x = 10.0  # 初始值
learning_rate = 0.1  # 学习率
num_iterations = 20  # 迭代次数
# 执行梯度下降法
optimal_x = gradient_descent(initial_x, learning_rate, num_iterations)
# 可视化
x_values = np.linspace(-10, 10, 400)
plt.plot(x_values, f(x_values), label="f(x) = x^2")
plt.scatter(optimal_x, f(optimal_x), color='red', label="Optimal Point")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Gradient Descent Optimization")
plt.show()