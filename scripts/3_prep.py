import pandas as pd
import os

csv_file = ''
df = pd.read_csv(os.path.join(os.getcwd(), csv_file))

#change this logic according to the file
df['file'] = df["filepath"].astype(str)+'-'+ df["filename"].astype(str)
df['file'] = df['file'].apply(lambda x: (str(x)[7:])) #
df['file'] = df['file'].apply(lambda x: x.replace('\\', '-')) #replacing '/' with '-'
df = df.drop(['filename', 'filepath'], axis = 1)
first_column = df.pop('file')
df.insert(0, 'file', first_column)



print(df.head(10))


df.to_csv(os.path.join(os.getcwd(), 'labels_file.csv'))