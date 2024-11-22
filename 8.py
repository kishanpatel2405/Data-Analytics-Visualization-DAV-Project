#most songs by single artist name
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel("spotifydata.xlsx")

# Assuming 'artist(s)_name' is the column name containing the artist names
# Count the occurrences of each artist and select the top ten
top_ten_artists = df['artist(s)_name'].value_counts().head(10)

# Plotting the bar chart
plt.figure(figsize=(10, 6))
top_ten_artists.plot(kind='bar', color='salmon')
plt.title('Top Ten Artists with Most Appearances')
plt.xlabel('Artist Name')
plt.ylabel('Frequency')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')       # Add grid lines along the y-axis
plt.tight_layout()
plt.show()




















