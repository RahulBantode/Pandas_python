# Write a program to create the Series using list and dictonaries.


import pandas as pd 

def createSeriesUsingList():
	list_1 = [20,304,50]

	series = pd.Series(list_1)
	series.columns = ["row"]

	print("Series are : ")
	print(series)
	print("Shape : ",series.shape)

	#shortcut.
	''' 
	series = pd.Series([10,30,40,50]);
	print(series)
	'''

def createSeriesUsingDict():
	dict_ = {'Rahul':20,"Kunal":30}

	series = pd.Series(dict_)

	print("Series are (using dictornary): ")
	print(series)
	print("Shape : ",series.shape)



	#shortcut.
	''' 
	series = pd.Series({"Rahul":20,"Naina":30,"Bhagi":50});
	print(series)
	
	'''
def main():

	createSeriesUsingList()
	createSeriesUsingDict()


if __name__ == '__main__':
	main()