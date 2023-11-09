import pandas

# pip install pandas

data = pandas.read_csv('records.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  radek    coe     3   9.0
# 1  Zosia    cos     2   9.1
# 2  Tomek    cot     1   0.5
# 3  Zenek    con     8   0.0

print(data.columns)
print(data.values)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
# [['radek' 'coe' 3 9.0]
#  ['Zosia' 'cos' 2 9.1]
#  ['Tomek' 'cot' 1 0.5]
#  ['Zenek' 'con' 8 0.0]]
print(data.values[0])  # ['radek' 'coe' 3 9.0]
print(type(data.values))  # <class 'numpy.ndarray'>
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  radek    coe     3   9.0
# 1  Zosia    cos     2   9.1
# 2  Tomek    cot     1   0.5
# 3  Zenek    con     8   0.0>
