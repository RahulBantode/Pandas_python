'''
	Problem Statement :-
		How to generate demo on randomly generated DataFrame
'''

#Generate the DataFrame using random values

import pandas as pd
import numpy as np 

def main():
	np.random.seed(55)   #this method is used to random number generator , the random number genrator needs
	                     #the number to start with this value known as seed value which are passed in the
	                     #seed function.  by default the random number genrator uses the current system time
	df_random = pd.DataFrame(np.random.randint(1000, size=(10,6)),
		        columns = list('ABCDEF'),
		        index = ["Row-{}".format(i+1) for i in range(10)])


	'''
	random.randint(100  #this argument states that the random number will between or less than num specified
	               size = (10,6) #this arg. is shape of the dataframe in this 10 rows * 6 columns
	               )
	'''
	print(df_random)

if __name__ == "__main__":
	main()