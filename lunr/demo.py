import pandas as pd

df = pd.read_csv("https://calmcode.io/datasets/clinc.csv").assign(idx=lambda d: d.index)
df.sample(3)
# print(df)

documents = df.to_dict(orient="records")

from lunr import lunr

index = lunr(ref='idx', fields=('text',), documents=documents)

spanish = index.search("spanish")   # search for the word "spanish"

for i in spanish:
    print(documents[int(i['ref'])])

