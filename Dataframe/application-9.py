'''
	Write a program to create a dataframe in pandas using series and list

'''


import pandas as pd 
import numpy as np 

def main():

	data1 = np.arange(1,9)
	data2 = ['A','B','C','D','E','F','G','H']

	data = { "Integers" : data1, "Alphabets": data2}

	df = pd.DataFrame(data)

	df['Age'] = [20,30,40,50,60,70,80,90]
	print("DataFrame")
	print(df)

if __name__ == '__main__':
	main()