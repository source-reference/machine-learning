import numpy as np 
import matplotlib.pyplot as plt

# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T

# weight (kg)
y = np.array([[ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T

# plt.plot(X, y, 'ro')
# plt.axis([140, 190, 45, 75])
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.show()

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)

w_0 = w[0][0]
w_1 = w[1][0]

// du doan
y0 = w_0 + w_1*165
print(y0)