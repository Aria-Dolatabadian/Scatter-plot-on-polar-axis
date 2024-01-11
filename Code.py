import matplotlib.pyplot as plt
import pandas as pd

# Read data from CSV file
loaded_data = pd.read_csv('polar_data.csv')
# Change the radius scale (e.g., multiply by 2)
loaded_data['Radius'] = 1 * loaded_data['Radius']
# Plotting loaded data
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(loaded_data['Theta'], loaded_data['Radius'], c=loaded_data['Colors'], s=loaded_data['Area'], cmap='hsv', alpha=0.75)

plt.show()
