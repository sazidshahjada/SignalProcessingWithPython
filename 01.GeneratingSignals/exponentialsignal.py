import numpy as np 
import matplotlib.pyplot as plt 

constant = 1

time = np.linspace(0, 5, 1000)
d_time = np.linspace(0, 5, 100)

amp = np.exp(constant * time)
d_amp = np.exp(constant * d_time)


plt.figure(figsize=(20, 10))

plt.subplot(2, 1, 1)
plt.plot(time, amp)
plt.title('Continuous Time Exp Signals')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 5)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.stem(d_time, d_amp)
plt.title('Discrete Time Sinusoidal Exp Signals')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 5)
plt.grid(True)

plt.savefig('exponentialsignal.png')