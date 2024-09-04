import numpy as np
import matplotlib.pyplot as plt
def compute_cost(X, y, theta):
    m = len(y)
    predictions = X.dot(theta)
    cost = (1/2*m) * np.sum(np.square(predictions - y))
    return cost
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    cost_history = np.zeros(iterations)

    for it in range(iterations):
        predictions = X.dot(theta)
        errors = np.dot(X.T, (predictions - y))
        theta -= (learning_rate / m) * errors
        cost_history[it] = compute_cost(X, y, theta)

    return theta, cost_history
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
X_b = np.c_[np.ones((len(X), 1)), X]  
theta = np.random.randn(2)  
learning_rate = 0.01
iterations = 1000
theta, cost_history = gradient_descent(X_b, y, theta, learning_rate, iterations)
print(f"Final parameters (theta): {theta}")
print(f"Final cost: {cost_history[-1]}")
plt.plot(range(iterations), cost_history, color='blue')
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost History over Iterations')
plt.show()
plt.scatter(X, y, color='red', label='Original data')
plt.plot(X, X_b.dot(theta), color='blue', label='Fitted line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
