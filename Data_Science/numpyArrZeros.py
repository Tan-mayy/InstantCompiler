import numpy as np

zeroarr =  np.zeros(10)
print(zeroarr)  # These are in floats we need to convert them into integers
onearr =  np.ones(10)
print(onearr)  # These are in floats we need to convert them into integers

zeroarr = zeroarr.astype(int)
print(zeroarr)

onearr = onearr.astype(int)
print(onearr)