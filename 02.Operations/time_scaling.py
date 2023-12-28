import numpy as np
import matplotlib.pyplot as plt

def time_scale(time, scalar):
    scaled_signal = scalar * time
    return scaled_signal

amp = 1
frequency = 1

time = np.linspace(0, 4 * np.pi, 1000)
signal = amp * np.sin(2 * np.pi * frequency * time)
scaled_time = time_scale(time, 3)

plt.figure(figsize=(20, 10))

plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * np.pi)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(scaled_time, signal)
plt.title('Time Scaled Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * np.pi)
plt.grid(True)

plt.savefig('time_scaling.png')