# unitary_signals.py
import numpy as np

# Unit Step Signal
def unit_step(n):#passing the parameter
    return np.where(n >= 0, 1, 0)

# Unit Impulse Signal
def unit_impulse(n):#passing the parameter
    return np.where(n == 0, 1, 0)

# Ramp Signal
def ramp_signal(n):#passing the parameter
    return np.where(n >= 0, n, 0)
