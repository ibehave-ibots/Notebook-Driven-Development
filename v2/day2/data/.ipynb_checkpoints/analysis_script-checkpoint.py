import pandas as pd
import hvplot.pandas
url = "https://uni-bonn.sciebo.de/s/3ZbmkolHLQu1ADa/download"
df = pd.read_csv(url)
df.head()
df['mouse'].value_counts()
df['contrast_left'].value_counts()
df['contrast_right'].value_counts()
df['response_time'].hvplot.hist()
df['feedback_time'].hvplot.hist()
