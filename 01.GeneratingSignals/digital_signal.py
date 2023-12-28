import numpy as np 
import matplotlib.pyplot as plt 

time = np.array([0,1,2,3,4,5,6,7,8,9])
amp = np.array([0,0,0,1,1,0,1,0,0,1])

plt.figure(figsize=(20, 10))

plt.stem(time, amp)
plt.title('Digital Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)

plt.savefig('digital_signal.png')