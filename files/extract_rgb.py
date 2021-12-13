import cv2
import h5py
import numpy as np
import matplotlib.pyplot as plt

snow = h5py.File('01813.h5', 'r')
city = h5py.File('01949.h5', 'r')
park = h5py.File('02167.h5', 'r')

snow_rgb = np.array(snow['rgb'])
city_rgb = np.array(city['rgb'])
park_rgb = np.array(park['rgb'])

snow_rgb = np.transpose(snow_rgb, (1, 2, 0))
city_rgb = np.transpose(city_rgb, (1, 2, 0))
park_rgb = np.transpose(park_rgb, (1, 2, 0))

plt.imsave('snow_rgb.png', snow_rgb)
plt.imsave('city_rgb.png', city_rgb)
plt.imsave('park_rgb.png', park_rgb)

