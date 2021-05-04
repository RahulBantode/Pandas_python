'''
	Write a program to select or filter the rows
	from a DataFrame based on values in columns in pandas.

'''

import pandas as pd 
import numpy as np 

def main():

	data1 = np.arange(1,9)
	data2 = ['A','B','C','D','E','F','G','H']

	data = { "Integers" : data1, "Alphabets": data2}

	df = pd.DataFrame(data)

	df['Age'] = [20,30,40,50,60,70,80,90]
	

	#Now select the row according the values in columns.
	#loc function :- The function is used to access the group of rows and columns by labeled or boolean array

	print("\nColumns age == 30 ")
	print(df.loc[df["Age"] == 30])  #it gives the whole row entity where age == 30

	print("\nColumng age < 60 ")
	print(df.loc[df["Age"] < 60])  #it gives the row entity which less than age < 60

	print("\ncolumn Alphabets != F") #it gives all the row except F
	print(df.loc[df["Alphabets"] != "F"])

	print("\n multiple conditions ")
	print(df.loc[(df["Age"] > 50) & ((df["Alphabets"] == "G") | (df["Alphabets"] == "H"))])	

	print("The where columns matches 80 and print thier integers and columns")
	data = df.loc[df["Age"] == 80]
	print(data["Integers"])

if __name__ == '__main__':
	main()