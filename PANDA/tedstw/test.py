# import pandas as pd
# df = pd.read_csv('/Users/dhruveshsinghom/Documents/Python/PANDA/csv/tips.csv')
# df['sum']=df['Data_value']
# print(df)
# import pandas as pd
# df = pd.read_csv('tips.csv')
# df['tip'] = [2.5, 3.0, 4.2, 1.8, 3.5] 
# df.to_csv('tips.csv', index=False)
# print("Tip column added and saved successfully!")
# import os
# print(os.getcwd())  # Prints the current working directory

import pandas as pd

# # Creating two proper DataFrames
# df = pd.DataFrame([[1, 2]], index=[1], columns=['A', 'B'])  
# df1 = pd.DataFrame([[2, 3]], index=[4], columns=['A', 'B'])  

# # Using pd.concat instead of append()
# df_combined = pd.concat([df, df1])

# # Print result
# print(df_combined)

from pandas import read_csv


df = read_csv('tips.csv')
print(df.head(3))