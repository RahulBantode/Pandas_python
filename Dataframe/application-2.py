#Write a program to create a Dataframe using dict of narray/list


import pandas as pd

def main():
	dict = {'Rahul':[10,20,30],
			'Kunal':[40,50,60],
			'Nitin':[70,80,90],
			'Sagar':[1 ,2 ,4 ]}

	df = pd.DataFrame(dict)
	print(df)



if __name__ == '__main__':
	main()