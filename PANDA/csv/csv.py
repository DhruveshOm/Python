import pandas as pd
df = pd.read_csv('/Users/dhruveshsinghom/Documents/Python/PANDA/csv/tips.csv')
df['sum']=df['Data_value']
print(df)
# import pandas as pd
# df = pd.read_csv('tips.csv')
# df['tip'] = [2.5, 3.0, 4.2, 1.8, 3.5] 
# df.to_csv('tips.csv', index=False)
# print("Tip column added and saved successfully!")
# import os
# print(os.getcwd())  # Prints the current working directory
