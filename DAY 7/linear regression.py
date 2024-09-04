import numpy as np
import matplotlib.pyplot as plt
class LinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None

    def fit(self, X, y):
        
        X_mean = np.mean(X)
        y_mean = np.mean(y)
        
        
        n = len(X)
        numerator = 0
        denominator = 0
        for i in range(n):
            numerator += (X[i] - X_mean) * (y[i] - y_mean)
            denominator += (X[i] - X_mean) ** 2
        self.slope = numerator / denominator
        self.intercept = y_mean - (self.slope * X_mean)

    def predict(self, X):
        return self.slope * X + self.intercept

X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.scatter(X, y, color='blue', label='Original data')
plt.plot(X, y_pred, color='red', label='Fitted line')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
print(f"Slope: {model.slope}")
print(f"Intercept: {model.intercept}")
