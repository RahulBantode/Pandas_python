''' 
	Write a program to get the length size and shape of series in pandas

'''


import pandas as pd 

def main():

	list_ = [10,203,40,40]

	series = pd.Series(list_)
	print("length of series : ",len(series))
	print("Shape of  series : ",series.shape)
	print("Dimension of series :",series.ndim)

if __name__ == '__main__':
	main()