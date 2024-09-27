import numpy as np
import matplotlib.pyplot as plt
w = np.linspace(0, np.pi, 501) 
z = np.exp(-1j * w) 
x = 3 * (1 - 0.9 * z)**(-1) 
a = np.abs(x) 
b = np.angle(x) * 180 / np.pi 
plt.subplot(2, 1, 1)
plt.plot(w / np.pi, a)
plt.xlabel('Frequency (w / pi)')
plt.ylabel('Magnitude (a)')
plt.title('Magnitude Spectrum')
plt.subplot(2, 1, 2)
plt.plot(w / np.pi, b)
plt.xlabel('Frequency (w / pi)')
plt.ylabel('Phase (degrees)')
plt.title('Phase Spectrum')
plt.tight_layout()
plt.show()