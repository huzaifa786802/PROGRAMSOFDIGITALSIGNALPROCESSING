num=input('Type the Numerator coefficients=')
import numpy as np
from scipy import signal
num=[2,6.4,4.9,-0.1,-0.6]
den=[5,15.5,13.7,-22.52,-0.48]
z,p,k=signal.tf2zpk(num,den)
roc=signal.convolve(den,den[::-1])
print("Transfer function coefficients:")
print("Numerator:",num)
print("Denominator:",den)
print("\nZeros:",z)
print("Poles:",p)
print("Gain",k)
print("\nROC:",roc)