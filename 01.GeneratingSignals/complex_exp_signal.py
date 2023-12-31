import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4 * np.pi, 1000)

frequency = 0.5
amplitude = 1
phase = 0

y = amplitude * np.exp(1j * (2 * np.pi * frequency * t + phase))

plt.figure(figsize=(8, 4))

plt.subplot(2, 1, 1)
plt.plot(t, np.real(y), label='Real part')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * np.pi)
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, np.imag(y), label='Imaginary part')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(0, 4 * np.pi)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('complex_exp.png')
