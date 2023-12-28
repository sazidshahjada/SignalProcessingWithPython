import numpy as np
import matplotlib.pyplot as plt

def amp_scale(signal, scalar):
    scaled_signal = scalar * signal
    return scaled_signal

amp = 1
frequency = 1

time = np.linspace(0, 4 * np.pi, 1000)
signal = amp * np.sin(2 * np.pi * frequency * time)
scaled_signal = amp_scale(signal, 2)

plt.figure(figsize=(20, 10))

plt.subplot(2, 1, 1)
plt.plot(time, signal)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * np.pi)
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, scaled_signal)
plt.title('Amplitude Scaled Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * np.pi)
plt.grid(True)

plt.savefig('amp_scaling.png')