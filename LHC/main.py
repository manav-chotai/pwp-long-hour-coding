import sys
import os
import numpy as np
import matplotlib.pyplot as plt

folder_path = r"D:\ict\sem3\pwp\LHC\signal_ICT_ManavChotai_92400133081"
sys.path.append(folder_path)

# Import the modules from the folder
import unitary_signals
import trigonometric_signals as trig_signals
import operations as ops

# 1. Unit Step & Unit Impulse (length 20)
n = np.arange(0, 20)
u = unitary_signals.unit_step(n)
d = unitary_signals.unit_impulse(n)
r = unitary_signals.ramp_signal(n)

# 2. Sine wave (Amplitude=2, Freq=5Hz, Phase=0)
t = np.linspace(0, 1, 500)
sine = trig_signals.sine_wave(2, 5, 0, t)
cosine = trig_signals.cosine_wave(2, 5, 0, t)

# 3. Time shift sine wave by +5 units
shifted_sine = ops.time_shift_continuous(trig_signals.sine_wave, t, 5, 2, 5, 0)

# 4. Addition of Unit Step + Ramp
sum_signal = ops.signal_addition(u, r, n)

# 5. Multiply Sine × Cosine
product = ops.signal_multiplication(sine, cosine, t)

# Plotting
plt.figure(figsize=(12, 10))
#unit step function
plt.subplot(3, 2, 1) #ploting the value in that graph
plt.stem(n, u, basefmt=" ")
plt.title("Unit Step (Length 20)") # title of function

#unit impulse function
plt.subplot(3, 2, 2) #ploting the value in that graph 
plt.stem(n, d, basefmt=" ")
plt.title("Unit Impulse (Length 20)")# title of function

#sine wave
plt.subplot(3, 2, 3) #ploting the value in that graph
plt.plot(t, sine)
plt.title("Sine Wave (Amplitude=2, Freq=5Hz, Phase=0)")# title of function

#timeshift of sine wave
plt.subplot(3, 2, 4) #ploting the value in that graph 
plt.plot(t, sine, label="Original")
plt.plot(t, shifted_sine, label="Shifted +5")
plt.title("Time Shift of Sine Wave")# title of function
plt.legend()

#unit step + ramp  signal
plt.subplot(3, 2, 5) #ploting the value in that graph
plt.stem(n, sum_signal, basefmt=" ")
plt.title("Unit Step + Ramp Signal")# title of function

#sine * cosine wave
plt.subplot(3, 2, 6) #ploting the value in that graph
plt.plot(t, product)
plt.title("Sine × Cosine (Amplitude=2, Freq=5Hz)")# title of function

plt.tight_layout()
plt.show()
