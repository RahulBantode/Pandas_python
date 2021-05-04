#Write a program to construct the Dataframe using string data

import pandas as pd 

def main():

	Name         = "Rahul","Nitin","kunal","Mohit"
	Profession   = "ML-Engineer","Salesforce Dev","Flutter Dev","Native Dev"
	Organisation = "ThoughtWorke","Infosys","IBM","QuickHeal"

	frame = {"Employee Name":Name, "Profession":Profession, "Organisation":Organisation}

	df = pd.DataFrame(frame)
	print(df)

if __name__ == '__main__':
	main()