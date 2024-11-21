#total song released per year
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
df = pd.read_excel("spotifydata.xlsx")

ax = sns.histplot(df['released_year'], binrange=(2000, 2022), discrete=True)
ax.set(xlabel='Year', ylabel='Count')
ax.set_title('Total Songs Released Per Year (2000 - 2024)')
plt.show()






















