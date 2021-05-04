''' 

	Write a program to get the index and values of series in pandas

'''


import pandas as pd 
import numpy as np 

def main():
	#first of all i am creating one series

	series = pd.Series(np.arange(1,20,1))

	#Now get the index and values of series only whoom the number is even

	i = 1
	for i in range(len(series)):

		if(series[i] % 2 == 0):
			print("Index : {} , values : {}".format(i,series[i]))


	#by following code we can get there index and values.
	print("Series index  : ",series.index)
	print("Series values : ",series.values)


if __name__ == '__main__':
	main()