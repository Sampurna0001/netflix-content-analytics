import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_clean.csv')

# Fix missing values properly
# Replace the old fillna lines with these:
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')
df['date_added'] = df['date_added'].fillna('Unknown')

# Word cloud from descriptions
text = ' '.join(df['description'].dropna())
wc = WordCloud(width=1200, height=600, background_color='black',
               colormap='Reds', max_words=100).generate(text)
plt.figure(figsize=(15, 7))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
plt.savefig('chart5_wordcloud.png', dpi=150)
plt.show()
print("Word cloud done!")

# Re-export properly cleaned CSV
df.to_csv('netflix_clean.csv', index=False)
print("Clean CSV re-exported!")