#This Application contains all the loc and iloc method mechanism 
import pandas as pd 

def main():
	df = pd.read_csv("WinePredictor.csv")

	#print(df.shape)
	#print(df.columns)
	#print(df.index)

	#print(type(df['Alcohol']))

	#print(df.Alcohol) #this is equivalent to df['Alcohol']  to getting the particular column by label.

	#print(df[['Alcohol','Ash','Hue']])

	#print(df.iloc[0]) #it gives a single row 
	#print(df.iloc[ [0,1,2] ])  #to getting the multiple rows we have to pass the list of indexes.
	#print(df.iloc[0 : 4]) #to getting the multiple rows
	
	#iloc - means integer location this function all about the integer locations.


	#print(df.iloc[0 : 4 , 6])  #here after comma the index is column index.
	#print(df.iloc[0:4 , 1:6])  #here we get multiple rows and columns
	#print(df.iloc[ [0,3,5] , [3,4,5]]) #here we passing the list of rows and columns 

	#by using loc we can pass the name of column with the index of location.
	#print(df.loc[[0,1],['Alcohol','Hue','Ash']])

	#print(df.loc[0:5,['Alcohol','Hue','Ash']])

	#print(df.loc[130:160, ['Alcohol','Hue','Ash']])

	print(df.loc[0:5,'Alcohol':'Magnesium'])

	#print(df['Alcohol'].value_counts()) #this function counts all the unique values from the alcohol.

if __name__ == '__main__':
	main()