num=input('Type the Numerator coefficients=')
import numpy as np
from scipy import signal
num=[1,-0.21,-0.1144,-0.3582,-0.1456]
den=[1,2.4,5.6,-1.2,3]
z,p,k=signal.tf2zpk(num,den)
roc=signal.convolve(den,den[::-1])
print("Transfer function coefficients:")
print("Numerator:",num)
print("Denominator:",den)
print("\nZeros:",z)
print("Poles:",p)
print("Gain",k)
print("\nROC:",roc)