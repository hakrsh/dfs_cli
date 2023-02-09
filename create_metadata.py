import pandas as pd
import os

df = pd.read_csv('./laptops.csv')

dir_path = './data'
file_names = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
manufacturer = {}
for file_name in file_names:
    name = file_name.split('.')[0]
    manufacturer[name] = os.path.join(dir_path, file_name)

# for each row in the dataframe, check if the image exists in the data folder 
# if it does, add the path to the image to the dataframe 
# if it doesn't, add default image path to the dataframe

df['file_path'] = df['Manufacturer'].apply(lambda x: manufacturer[x] if x in manufacturer else 'default.jpg')
df.to_csv('./metadata.csv', index=False)
