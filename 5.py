import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
df = pd.read_excel("spotifydata.xlsx")

play = df.sort_values(by='in_spotify_playlists', ascending=False)
play = play[['track_name', 'in_spotify_playlists']][:10]

chart = df.sort_values(by='in_spotify_charts', ascending=False)
chart = chart[['track_name', 'in_spotify_charts']][:10]

stream = df.sort_values(by='streams', ascending=False)
stream = stream[['track_name', 'streams']][:10]

fig, axes = plt.subplots(3,1,figsize=(10,10))
plt.subplot(3,1,1)
ax1 = sns.barplot(play, y='track_name', x='in_spotify_playlists')
ax1.set_xlabel('count of spotify playlist')
ax1.set_title('Top songs according to playlist')

plt.subplot(3,1,2)
ax1 = sns.barplot(chart, y='track_name', x='in_spotify_charts')
ax1.set_xlabel('Charts')
ax1.set_title('Top songs according to Charts')


plt.subplot(3,1,3)
ax1 = sns.barplot(stream, y='track_name', x='streams')
ax1.set_xlabel('Total Streams')
ax1.set_title('Top songs according to Streams')

plt.tight_layout()
plt.show()

















