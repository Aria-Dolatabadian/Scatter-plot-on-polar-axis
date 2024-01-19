import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Read data from CSV file
loaded_data = pd.read_csv('polar_data.csv')

# Change the radius scale (e.g., multiply by 2)
loaded_data['Radius'] = 1 * loaded_data['Radius']

# Plotting loaded data with modified radius scale
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='polar')
c1 = ax1.scatter(loaded_data['Theta'], loaded_data['Radius'], c=loaded_data['Colors'], s=loaded_data['Area'], cmap='hsv', alpha=0.75)
ax1.set_title('Loaded Data with Modified Radius Scale')

plt.show()

# Plotting loaded data from 'polar_data.csv' with original radius scale
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='polar')
c2 = ax2.scatter(loaded_data['Theta'], loaded_data['Radius'], c=loaded_data['Colors'], s=loaded_data['Area'], cmap='hsv', alpha=0.75)
ax2.set_title('Loaded Data with Original Radius Scale')

ax2.set_rorigin(-2.5)
ax2.set_theta_zero_location('W', offset=10)

plt.show()
