'''
	Write a program in which specify the index while creating the series in pandas.

'''


import pandas as pd 

def main():
	data = ["India","America","Thiland","Austrilia","England"]

	index_list = [100,200,300,400,500]

	series = pd.Series(data,index = index_list)

	print(series)



if __name__ == '__main__':
	main()