import pandas as pd

read_file = pd.read_csv (r'C:\Users\serda\PycharmProjects\Code_in_Place\countries\Afghanistan.txt')
read_file.to_csv (r'C:\Users\serda\PycharmProjects\Code_in_Place\countries_csv\Afghanistan.csv', index=None)
