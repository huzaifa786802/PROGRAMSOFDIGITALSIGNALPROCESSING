import numpy as np
import matplotlib.pyplot as plt
roll_number = 9
A = 9
a = -1/2 * 9
n_values = np.arange(-10, 11)
x_values = A * (a ** n_values)
is_increasing = all(x_values[i] < x_values[i+1] for i in range(len(x_values)-1))
is_decreasing = all(x_values[i] > x_values[i+1] for i in range(len(x_values)-1))
plt.stem(n_values, x_values)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Sequence x(n)')
plt.grid(True)
plt.show()
if is_increasing:
    print("The sequence is increasing exponentially.")
elif is_decreasing:
    print("The sequence is decreasing exponentially.")
else:
    print("The sequence is neither increasing nor decreasing exponentially.")
