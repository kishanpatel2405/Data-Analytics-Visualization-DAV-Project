#single artist with most streams
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df = pd.read_excel("spotifydata.xlsx")

# Select rows where 'artist_count' is 1
single_artist_tracks = df[df['artist_count'] == 1]

# Select top ten tracks based on 'streams'
top_ten_tracks = single_artist_tracks.nlargest(10, 'streams')

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_ten_tracks['artist(s)_name'], top_ten_tracks['streams'], color='skyblue')
plt.title('Top Ten Tracks by Single Artist with Most Streams')
plt.xlabel('Artist Name')
plt.ylabel('Streams')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(axis='y')       # Add grid lines along the y-axis
plt.tight_layout()
plt.show()
