import pandas as pd
import os

df = pd.read_csv('./laptops.csv')

dir_path = './data'
file_names = [f.split('.')[0] for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

# for each row in the dataframe, check if the image exists in the data folder 
# if it does, add the path to the image to the dataframe 
# if it doesn't, add default image path to the dataframe

df['file_path'] = df.apply(lambda row: os.path.join(dir_path, row['Manufacturer'] + '.jpg') if row['Manufacturer'] in file_names else os.path.join(dir_path, 'default.jpg'), axis=1)
df.to_csv('./metadata.csv', index=False)
