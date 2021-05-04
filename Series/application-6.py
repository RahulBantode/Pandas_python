'''
	write a prgram to calculate or to get the first and and last few rows from series

'''


import numpy as np 
import pandas as pd 

def main():

	series = pd.Series(np.arange(1,20,1))

	print("First row of series : ",series[0])

	print("First few rows of series : ")
	print(series.head(3))

	print("Last few rows of series : ")
	print(series.tail(3))

	print("Last row of series : ",series[-1:])

if __name__ == '__main__':
	main()