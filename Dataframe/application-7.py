#Write a program to create a dataframe using pandas series.

import pandas as pd 
import matplotlib.pyplot as plt 

def main():
	Author  = ["Rahul","Nitin","Kunal","Mohit"]
	b_price = [900,450,740,100]
	Article = ["C-lang","Java-lang","Flutter","Native-core"]

	auth_series   = pd.Series(Author)
	book_series   = pd.Series(b_price)
	articl_series = pd.Series(Article)

	frame = {"Author" : auth_series, "Book-price": book_series , "Article" : articl_series}

	df = pd.DataFrame(frame)
	
	#Now add series externally into the dataframe

	age = [78,25,82,39]

	df["Age"] = pd.Series(age) #hyane ek new series externally add hote.
	print(df)

	df.plot.bar()
	plt.show()


if __name__ == '__main__':
	main()