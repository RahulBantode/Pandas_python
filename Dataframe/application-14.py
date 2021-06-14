'''
	Write a program to delete the dataframe columns by name and index

'''


import pandas as pd 
import numpy as np 

def main():

	data1 = [10,20,30,40]
	data2 = ["a","b","c","d"]
	data3 = ["jalgaon","pune","mumbai","banglore"]

	df = pd.DataFrame({"Int":data1,"Alpha":data2,"city":data3})
	print(df)

	#To delete the dataframe entity pandas provide drop function

	print("\n Drop Column by Name \n")
	print(df.drop("Alpha",axis=1))

	print("\n Drop columns by index \n")
	print(df.drop(df.columns[:-1],axis=1))

	print("\n Drop the row by name/id \n") #we know that by default id will be start from 0
	print(df.drop([0,1],axis=0))


if __name__ == '__main__':
	main()