'''
	Write a program to add new columns to existing dataframe
	and get the list of columns header

'''

import pandas as pd 
import numpy as np 

def main():

	name = pd.Series(["Rahul","Kunal","Nitin","Manish","Mohit"])
	age  = pd.Series([24,22,28,39,35])

	data = {"Name":name,"age":age}

	df = pd.DataFrame(data)
	print(df)

	#Now add the new column to the existing data frame
	print("\nNewly added column is city : \n")
	df["city"] = ["pune","hydrabad","banglore","gurugram","mumbai"]
	print(df)

	#Now get the headers of all the columns

	print("\n Header of the columns : ")
	for col in df.columns:
		print(col,)

if __name__ == '__main__':
	main()