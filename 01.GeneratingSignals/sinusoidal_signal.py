import numpy as np 
import matplotlib.pyplot as plt 

pi = np.pi
frequency = 0.5
sample = 10

time = np.linspace(0, 4 * pi, 1000)
d_time = np.linspace(0, 4 * pi, 10)

amp_1 = np.sin(2 * pi * frequency * time)
amp_2 = np.cos(2 * pi * frequency * time)

d_amp_1 = np.sin(2 * pi * sample * d_time)
d_amp_2 = np.cos(2 * pi * sample * d_time)


plt.figure(figsize=(20, 10))


plt.plot(time, amp_1, label='sin(x)')
plt.plot(time, amp_2, label='cos(x)')
plt.title('Continuous Time Sinusoidal Signals')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * pi)
plt.legend()
plt.grid(True)

plt.savefig('sinusoidal_signal.png')