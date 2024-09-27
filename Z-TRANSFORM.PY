num=input('Type the Numerator coefficients=')
import numpy as np
from scipy import signal
num=[2,16,44,56,32]
den=[3,3,-15,18,-12]
z,p,k=signal.tf2zpk(num,den)
roc=signal.convolve(den,den[::-1])
print("Transfer function coefficients:")
print("Numerator:",num)
print("Denominator:",den)
print("\nZeros:",z)
print("Poles:",p)
print("Gain",k)
print("\nROC:",roc)