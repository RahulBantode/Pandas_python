'''
	Write a program to slice the series into subsets.

	Basic Terminology about series slicing.

	Slicing is a powerful approach to retrive subsets a data from a pandas object. A slice
	object is built using a syntax of start:end:step, the segments representing the first item,
	last item,and the increment between each item that you would like as the step.

'''

import pandas as pd 
import numpy as np 

def main():

	num = np.arange(100,1100,100)

	idx = ['A','B','C','D','E','F','G','H','I','J']

	series = pd.Series(num, index = idx)

	print("\n [2:4] \n")  #this will print the element from 2 to 4 index  
	print(series[2:4])  

	print("\n [1:6:2] \n") # this will go through index 1 to 6 but get values one after.
	print(series[1:6:2])

	print("\n [:6] \n")  #this will print the element from first to 6
	print(series[:6])

	print("\n [4:] \n ") #this will print the element from 6 to last
	print(series[4:])

	print("\n [:4:2] \n ") #this will print the element from 0 to 4 by steping in value by 2
	print(series[:4:2])

	print("\n [4::2] \n") #this will print the element from 4 to last by steping in value by 2
	print(series[4::2])

	print("\n [::-1] \n") #this will print the whole element from last 
	print(series[::-1])

	print("\n [::] \n") #this will print whole element from first
	print(series[::])

	print("\n [0] \n ") #this will print very first element
	print(series[0])

	print("\n [-1:] \n")#this will print the last element
	print(series[-1:])


if __name__ == '__main__':
	main()