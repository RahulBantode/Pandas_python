''' 
	Write a program to create Series Using Numpy array/function in pandas.
'''

import pandas as pd 
import numpy as np

def display(ser):

	print("Type : ",type(ser))
	print("Series : ")
	print(ser)

def main():

	series1 = pd.Series(np.array([10,20,40,50,60],dtype='int'))
	display(series1)

	series2 = pd.Series(np.arange(1,20,4))
	display(series2)

	series3 = pd.Series(np.linspace(10,100,6))
	display(series3)

	series4 = pd.Series(np.random.rand(10))
	display(series4)

if __name__ == '__main__':
	main()