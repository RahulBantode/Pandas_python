#Write a program to create a Dataframe using two dimensional list

import pandas as pd 

def main():
	list = [[1,2,3],[4,5,6],[7,8,9]]

	dataframe = pd.DataFrame(list,index=['ln-1','ln-2','ln-3'],columns=['col-1','col-2','col-3'])

	print(dataframe)
	print("Shape of DataFrame : ",dataframe.shape)



if __name__ == '__main__':
	main()