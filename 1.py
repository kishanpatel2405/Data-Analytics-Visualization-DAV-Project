#top 10 songs by streaming count
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("spotifydata.xlsx")
plt.figure(figsize=(10,6))
top_10_streams = df.sort_values(by=['streams', 'track_name'], ascending=False).head(10)

plt.bar(top_10_streams['track_name'], top_10_streams['streams'], color = 'pink')


for i, streams in enumerate(top_10_streams['streams']):
    plt.text(i, streams, str(streams), ha='center', va='top', rotation=90)


for i in range(1, len(top_10_streams)):
    difference = top_10_streams.iloc[i-1]['streams'] - top_10_streams.iloc[i]['streams']
    difference_str = str(difference)[:-6] + 'L'
    plt.text(i, top_10_streams.iloc[i]['streams'], f"{difference_str}", ha='center', va='bottom', color='red')


plt.xticks(rotation=90)
plt.yticks([])
plt.title('Top 10 Tracks by Streaming count')


plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.show()









