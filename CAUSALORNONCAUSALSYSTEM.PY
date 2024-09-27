import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(12)
x[0] = 1 
y = np.zeros_like(x)
for n in range(0, len(x)):
    if n + 2 < len(x): 
        y[n] = x[n]**2 + 2*x[n+2]

if np.all(y[2:] == x[2:]**2 + 2*x[:-2]):
    print("The system is causal")
else:
    print("The system is non-causal")

# Plot the input and output signals
n = np.arange(len(x))
plt.stem(n, x, 'b', markerfmt='bo', label='Input signal')
plt.stem(n, y, 'g', markerfmt='go', label='Output signal')
plt.xlabel('n')
plt.ylabel('Signal Amplitude')
plt.legend()
plt.show()