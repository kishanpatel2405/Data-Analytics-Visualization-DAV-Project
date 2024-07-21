#numbers of artist worked per song
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("spotifydata.xlsx")

plt.figure(figsize=(8,6))

artists_counts = df['artist_count'].value_counts().sort_index()

# Create a bar plot
plt.bar(artists_counts.index, artists_counts, color="#EBF400")
plt.bar(artists_counts.index, artists_counts, color="none", edgecolor="#F72798", linewidth=3)
plt.yticks([])

for x, y in zip(artists_counts.index, artists_counts):
    plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10)

# Hide spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

plt.title('Number of artists worked per song')
plt.show()
