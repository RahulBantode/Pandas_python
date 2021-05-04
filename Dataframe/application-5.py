#		Write a program to create a DataFrame using List of Dictonary.


import pandas as pd 

def main():

	#here we create a list of Dictonary.

	l_list = [{"Rahul" : 20 , "Meena":30, "Bhagi":40},
	          {"Rahul" : 40 , "Meena":50, "Bhagi":80}]

	print(l_list)


	df = pd.DataFrame(l_list)
	df.index = ["d1","d2"] #indexing the rows.
	print(df)

if __name__ == '__main__':
	main()
