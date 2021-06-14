
#Filter the data is in dataframe.

import pandas as pd

def main():
	
	First = ['Rahul','Kunal','Nitin','bhagi','sari']
	Role  = ['python developer ','flutter developer','java developer','C dev','Web dev']
	email = ['bantoderahul@gmail.com','kunalc@gmail.com','nitinc.793@gmail.com','bha@gmail.com','sari@gmail.com']

	dict = {'First':First,
	        'Role' :Role,
	        'email':email}

	df = pd.DataFrame(dict)

	df['salary'] = [500000,230000,700000,390000,980000]
	#print(df)

	sal = (df['salary'] == 980000) 
	#print(df[sal])
	#print(df.loc[sal, 'Role':'email'])

	name = (df['salary'] < 900000) & (df['salary'] > 400000)
	print(df[name])
	print()
	print(df.loc[name,['First','Role','salary']])
	print()

	Rol = (df['Role'] == 'java developer' ) | (df['Role'] == 'C dev')
	print(df[Rol])
	print()
	print(df.loc[Rol, 'email'])

	filt = (df['Role'].str.contains('developer'))
	print(df.loc[filt,'First'])

if __name__ == "__main__":
	main()
