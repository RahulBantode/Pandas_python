'''
	Write a program to create a dataframe in pandas using series and list

	And rename the column names :-

'''


import pandas as pd 
import numpy as np 

def main():

	data1 = np.arange(1,9)
	data2 = ['A','B','C','D','E','F','G','H']

	data = { "Integers" : data1, "Alphabets": data2}

	df = pd.DataFrame(data)

	print("DataFrame")
	print(df)

	#The Data after renaming the columns names :-

	df.columns = ["Int","Alf"]
	print(df)

if __name__ == '__main__':
	main()