''' 
df.set_index('column_name',inplace=True)
df.reset_index(inplace=True)

'''

import pandas as pd 

def main():
	df = pd.read_csv("WinePredictor.csv",index_col='Alcohol')
	#print(df.head())
	#df.reset_index(inplace=True)
	#print(df.head())
	
	schema_df = pd.read_csv("WinePredictor.csv")
	#print(schema_df)

	First = ['Rahul','Kunal','Nitin']
	Role  = ['python developer ','flutter developer','java developer']
	email = ['bantoderahul@gmail.com','kunalc@gmail.com','nitinc.793@gmail.com']

	dict = {'First':First,
	        'Role' :Role,
	        'email':email}

	df_schema = pd.DataFrame(dict)
	#print(df_schema) 

	df_schema.set_index('email',inplace=True)  #to set index for purpose.
	#print(df_schema.index)

	#benefit to set the one of the column as index mean when use the loc function we are not need to pass
	#Integer value for the row we directly pass the text to int
	print(df_schema.loc['bantoderahul@gmail.com' ,'Role'])

	print(df_schema)

	#df_schema.reset_index(inplace=True)
	#print(df_schema)

if __name__ == '__main__':
	main()