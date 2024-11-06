
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel("spotifydata.xlsx")

# Assuming 'mode' is the column name containing the mode data
mode_counts = df['mode'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(mode_counts, labels=mode_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Mode')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
