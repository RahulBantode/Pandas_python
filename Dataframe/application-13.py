'''
	Write a program to iterate over the rows and columns in the Dataframe

'''

import pandas as pd 
import numpy as np 


def main():
	df = pd.DataFrame({"Names":["Rahul","Bhagi","Kunal","Pooja","Nitin"],
					   "Id_no":[20,30,40,50,60],
					   "City":["jalgaon","pune","A-Bad","mumbai","bupur"]})

	print(df)
	print("Shape : ",df.shape)
	print("Dimension : ",df.ndim)

	#Iterate over the dataframe by using columns property where each columns are displayed sperately
	print("Iterate by using columns property")
	for col  in df.columns:
		print(df[col])


	#Iterrate over dataframe by using iterrows function. which sends two value one is index/row id one is the
	#columns are present in that rows so by passing the name to col value you can get the data of individual
	print("By using iterrows function")
	for row,col in df.iterrows():
		print(row,"\t",col["Names"],"  ",col["Id_no"])

	
	#Iterate over the dataframe by using itertuples function.
	print("By using itertuples function")
	for row in df.itertuples():
		print(getattr(row,"Names"),"   ",getattr(row,"City"))


if __name__ == '__main__':
	main()