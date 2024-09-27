
import numpy as np
import matplotlib.pyplot as plt
def u(n):
    return 1 if n >= 0 else 0
def convolution_sum(x, h):
    y = np.convolve(x, h, mode='full')
    return y
n = np.arange(0, 10)
x = np.array([u(i) for i in n])
h = np.array([u(i-3) for i in n])
result = convolution_sum(x, h)
plt.stem(result)
plt.title('Convolution Sum of x(n) and h(n)')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()