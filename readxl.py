import pandas as pd
df = pd.read_excel('employees.xlsx')
print(df)
print("After descending values is:")
s = df.sort_values('Years of experience', ascending=False)
print(s)