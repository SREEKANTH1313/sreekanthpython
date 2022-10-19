import pandas as pd
df = pd.read_excel('employees.xlsx')
print(df)
print("After descending values is:")
s = df.sort_values('Years of experience', ascending=False)
print(s)

#OUtput      Name  Years of experience      JobTitle        DOB
# 0      MUNIRAJA                     7   Mathematics 1985-01-04
# 1         RAMESH                   12    Statistics 1980-01-05
# 2        Amrutha                    7     Computers 1986-02-04
# 3  Shankar Reddy                   13    Statistics 1979-05-10
# 4         Pavani                    5        Python 1990-01-04
# After descending values is:
#            Name  Years of experience      JobTitle        DOB
# 3  Shankar Reddy                   13    Statistics 1979-05-10
# 1         RAMESH                   12    Statistics 1980-01-05
# 0      MUNIRAJA                     7   Mathematics 1985-01-04
# 2        Amrutha                    7     Computers 1986-02-04
# 4         Pavani                    5        Python 1990-01-04

