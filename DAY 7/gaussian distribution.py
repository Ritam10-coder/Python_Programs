import numpy as np
import matplotlib.pyplot as plt
def gaussian(X, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi * sigma ** 2))) * np.exp(- (X - mu) ** 2 / (2 * sigma ** 2))
X = np.linspace(-10, 10, 1000)
means = [0, 0, -2]
variances = [1, 2, 1]
labels = [f"Mean = {mu}, Variance = {sigma ** 2}" for mu, sigma in zip(means, variances)]
plt.figure(figsize=(10, 6))
for mu, sigma, label in zip(means, variances, labels):
    plt.plot(X, gaussian(X, mu, sigma), label=label)
plt.title("Gaussian Distributions with Varying Means and Variances")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()
