
this is installation link:-

pip install signal-ICT-ManavChotai-92400133081

first install that through cmd or any ide where we have to install that package 







first create a LHC name folder 
inside that create 4 folder : 1. build 2. dist 3. signal_ICT_ManavChotai_92400133081 4. signal_ICT_ManavChotai_92400133081.egg-info
and two file also main.py , setup.py

inside 1. build
two folder : 1. bdist.win-amd64 2. lib
inside 2. lib create folder of "signal_ICT_ManavChotai_92400133081"
four file 1.	unitary_signals.py
2.	trigonometric_signals.py
3.	operations.py
4.  __init__.py
file 


2.dist create  two file 
1.signal_ict_manavchotai_92400133081-1.0.0.tar.gz
2.signal_ICT_ManavChotai_92400133081-1.0.0-py3-none-any.whl

3. signal_ICT_ManavChotai_92400133081 create four file
1.	unitary_signals.py
2.	trigonometric_signals.py
3.	operations.py
4.  __init__.py
file 

4. signal_ICT_ManavChotai_92400133081.egg-info
   create 5 file dependency_links
   PKG-INFO
   requires
   SOURCES
   top_level

now follow the following step 
# signal_ICT_Manav_Chotai_92400133081

This is my Python package for the ICT course.  
The package contains functions for basic signal generation and signal operations.  

- unitary_signals → unit_step, unit_impulse, ramp  
- trigonometric_signals → sine_wave, cosine_wave, exponential  
- operations → time_shift, time_scaling, signal_addition, signal_multiplication  
- main.py → integrates all modules and shows plots  

---

# Files in the Package
- unitary_signals.py → unit_step, unit_impulse, ramp  
- trigonometric_signals.py → sine_wave, cosine_wave, exponential  
- operations.py → time_shift, time_scaling, signal_addition, signal_multiplication  
- main.py → runs examples and shows all required plots  

---

# Installation

## Local Install (from wheel file)
Build the package:
python setup.py sdist bdist_wheel

Install locally:
pip install dist/signal_ICT_Manav_Chotai_92400133081-0.1-py3-none-any.whl

## Upload & Install from TestPyPI
Upload to TestPyPI:
twine upload --repository testpypi dist/*

Install from TestPyPI:
pip install --index-url https://test.pypi.org/simple/ signal-ICT-Manav-Chotai-92400133081

---

# Step-by-Step Execution Guidelines

## 1. Run unitary_signals.py
from signal_ICT_Manav_Chotai_92400133081 import unitary_signals
import numpy as np

n = np.arange(0, 20)
step = unitary_signals.unit_step(n)
impulse = unitary_signals.unit_impulse(n)
ramp = unitary_signals.ramp_signal(n)

Generates and plots unit step, impulse, and ramp signals.

---

## 2. Run trigonometric_signals.py
from signal_ICT_Manav_Chotai_92400133081 import trigonometric_signals
import numpy as np

t = np.linspace(0, 1, 500)
sine = trigonometric_signals.sine_wave(2, 5, 0, t)
cosine = trigonometric_signals.cosine_wave(2, 5, 0, t)
expo = trigonometric_signals.exponential_signal(1, 0.5, t)

Generates and plots sine, cosine, and exponential signals.

---

## 3. Run operations.py
from signal_ICT_Manav_Chotai_92400133081 import operations

shifted = operations.time_shift(sine, 5)
scaled = operations.time_scale(sine, 2)
added = operations.signal_addition(step, ramp)
multiplied = operations.signal_multiplication(sine, cosine)

Performs time shift, scaling, addition, and multiplication of signals.

---

## 4. Run main.py
python main.py

This demonstrates all tasks together:
1. Generate and plot a unit step and impulse (length 20).  
2. Generate sine wave (A=2, f=5 Hz, t=0–1s).  
3. Perform time shifting on sine wave by +5 units.  
4. Add unit step and ramp signals.  
5. Multiply sine and cosine signals.  

---

# Example Usage
import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_Manav_Chotai_92400133081.trigonometric_signals import sine_wave

t = np.linspace(0, 1, 500)
y = sine_wave(2, 5, 0, t)

plt.plot(t, y)
plt.title("Sine Wave")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

---

# Expected Outputs
1. Unit step and impulse signals (length 20)  
2. Sine wave (A=2, f=5 Hz, phase=0, t=0–1s)  
3. Shifted sine wave (+5 units)  
4. Addition of step + ramp  
5. Multiplication of sine and cosine  

---

# Student Information
Name: Manav Chotai  
Enrollment No: 92400133081  
Division: 3EK1
