'''
		Write a program to make dataframe using list of list
		and perform some operations on it
'''

import pandas as pd 

def main():
	li = [['rahul','girish','bantode'],
	      ['nitin','anil','chaudhary'],
	      ['kunal','girish','bantode'],
	      ['sagar','dnya','bari']]

	df = pd.DataFrame(li,index=['r1','r2','r3','r4'],columns=['F_name','M_name','L_name'])
	print(df)

	#display only columns as F_name and M_name with all the row
	columns = ["F_name","M_name"]

	print("Display only the 2 columns : ")
	print(df[columns])

	#display only the 2 columns and two rows
	rows = ["r1","r2"]

	print("Display only 2 cols,and 2 rows : ")
	df = df.iloc[0:2,0:2]
	print(df)


	#transpose of dataframe :-
	df = df.transpose()
	print("After transpose : ")
	print(df)



if __name__ == '__main__':
	main()