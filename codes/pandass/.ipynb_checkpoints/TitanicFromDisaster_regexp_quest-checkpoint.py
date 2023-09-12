import pandas as pd
df_TFD = pd.read_csv('datasets/TitanicFromDisaster_train.csv')
print(df_TFD)
df_TFD.info()
df_TFD_Name = df_TFD['Name']
df_TFD_Name
lastName = r'^([A-Z]\w+)' 
df_TFD_Name['lastName'] = df_TFD_Name.str.extract(lastName)
print(df_TFD_Name)

merry = r'(\w+[rs][\.$])'
df_TFD_Name['Merry'] = df_TFD_Name.str.extract(merry)
print(df_TFD_Name)

