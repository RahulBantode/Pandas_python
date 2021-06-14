

import pandas as pd
import numpy as np 
def main():
	
	First = ['Rahul',np.nan,'Nitin','bhagi','sari']
	Role  = ['python developer ','flutter developer','java developer','C dev','Web dev']
	email = ['bantoderahul@gmail.com','NA','nitinc.793@gmail.com','bha@gmail.com','sari@gmail.com']

	dict = {'First':First,
	        'Role' :Role,
	        'email':email}

	df = pd.DataFrame(dict)

	df['salary'] = [500000,230000,700000,390000,980000]
	#print(df)

	df.columns = ['First_name','Emp_Role','Email_id','Emp_salary']
	#print(df.columns)

	#df.columns = [x.upper() for x in df.columns]
	#print(df.columns)

	#df.columns = df.columns.str.replace('_'," ")
	#print(df.columns)

	#to change specific columns name
	#df.rename(columns = {'First_name':'First'},inplace=True)
	#print(df.columns)

	df.loc[5]=['pooja','excel data entry','pooja@gmail.com',150000]  #here we added new rows
	#print(df)

	#here we change specific columns value.
	df.loc[2, ['Emp_Role' ,'Emp_salary']] = ['salesforce developer',350000]
	#print(df)

	df.at[2 , 'First_name'] = 'Ni3'
	#print(df)

	sal = (df['Emp_salary'] < 900000 ) & (df['Emp_salary'] > 200000)
	df.loc[-sal,'First_name'] = 'RAM'
	#print(df)

	df['Emp_Role'] = df['Emp_Role'].str.upper()
	#print(df)

	length = (df['Email_id'].apply(len) < 25) & (df['Email_id'].apply(len) > 15)
	print(df[length])

	#Sorting data columns

	print(df.sort_values(by='Emp_salary')) #to sort the df

	#df.isna()
	#df.fillna('MISING')

	df.drop('First_name',inplace=True,axis=1)
	print(df)

	df.drop(index=0,axis=0,inplace=True)
	print(df)

if __name__ == '__main__':
	main()