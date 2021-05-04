#Write a program to creating the pandas dataframe using list of tuples.


import pandas as pd 

def main():
	
	li = [(1,2,3),
	      (4,5,6),
	      (7,8,9)]

	df = pd.DataFrame(li)
	
	df.columns = ["col-1","col-2","col-3"]
	df.index   = ["row-1","row-2","row-3"]


	print(df)
	print(df.pivot("col-1","col-2","col-3"))

if __name__ == '__main__':
	main()