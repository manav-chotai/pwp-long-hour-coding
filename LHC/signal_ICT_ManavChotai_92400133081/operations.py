# operations.py
import numpy as np

# 1. Time shift for continuous signals
def time_shift_continuous(signal_func, t, shift, *args): #passing the parameter and argument
    return signal_func(*args, t - shift)

# 2. Signal addition (discrete signals)
def signal_addition(x1, x2, n):#passing the parameter and argument
    return np.array(x1) + np.array(x2)

# 3. Signal multiplication (continuous or discrete)
def signal_multiplication(x1, x2, t=None):#passing the parameter and argument
    return np.array(x1) * np.array(x2)
