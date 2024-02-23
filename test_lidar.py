import serial
from pyURG import serial_URG
import numpy as np
import matplotlib.pyplot as plt

URG1 = serial_URG('COM5', 900000)

URG1.init_timestamp2()

# xyz_MDMS, tm_MDMS = URG1.capture_MDMS(byte=3)
xyz_MDMS, tm_MDMS = URG1.capture_MDMS(byte=3, interval = 4, num_scans = 10)
np.set_printoptions(threshold=np.inf)
print(xyz_MDMS)
print(xyz_MDMS.shape)


mask = ~np.isnan(xyz_MDMS).any(axis=2).any(axis=0)

# Use the mask to filter rows without NaN
filtered_data = xyz_MDMS[:, mask, :]
print(filtered_data)
print(filtered_data.shape)

plt.plot(filtered_data[:,:, 0], filtered_data[:, :, 1], 'ro')
plt.xlim([-4000, 4000])
plt.ylim([-4000, 4000])
plt.show()


