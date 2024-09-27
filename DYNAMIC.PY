import numpy as np
import matplotlib.pyplot as plt
def H(z):
    numerator = 1 + 2*z**(-1) + 3*z**(-2)
    denominator = 1 + 2*z**(-1) + 3*z
    return numerator / denominator
def is_dynamic():
    if 'z**(-1)' in str(H) or 'z**(-2)' in str(H):
        return True
    else:
        return False
z_values = np.linspace(-10, 10, 1000)
H_values = H(z_values)
plt.plot(z_values, np.abs(H_values))
plt.title('Magnitude Response of H(z)')
plt.xlabel('z')
plt.ylabel('|H(z)|')
plt.grid(True)
plt.show()
if is_dynamic():
    print("The function H(z) is dynamic.")
else:
    print("The function H(z) is not dynamic.")