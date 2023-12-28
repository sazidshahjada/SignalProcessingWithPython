import numpy as np 
import matplotlib.pyplot as plt 

pi = np.pi
frequency_1 = 0.5
frequency_2 = 1.5

time = np.linspace(0, 4 * pi, 1000)

amp_1 = np.sin(2 * pi * frequency_1 * time)
amp_2 = np.cos(2 * pi * frequency_2 * time)

resultant = amp_1 - amp_2


plt.figure(figsize=(20, 10))

plt.subplot(2, 1, 1)
plt.plot(time, amp_1, label='sin(x)')
plt.plot(time, amp_2, label='cos(x)')
plt.title('Continuous Time Sinusoidal Signals')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * pi)
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, resultant, label='sin(x)-cos(x)')
plt.title('Resultant Continuous Time Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * pi)
plt.legend()
plt.grid(True)

plt.savefig('subtraction.png')