# Write a program to convert the list of nested dictonary into pandas dataframe


import pandas as pd 

def main():
	data = [
           		{
           			"Student" : [ {"Exam": 90, "Grade": "A"},
           						  {"Exam": 99, "Grade": "O"},
           						  {"Exam": 59, "Grade": "C"}
           						],
           			"Name"   : "Nitin Chaudhary"
           		},

           		{
           			"Student" : [ {"Exam": 80, "Grade": "A"},
           						  {"Exam": 70, "Grade": "B"},
           						  {"Exam": 59, "Grade": "C"}
           						],
           			"Name"   : "Kunal Chinchole"
           		},

           		{
           			"Student" : [ {"Exam": 90, "Grade": "A"},
           						  {"Exam": 40, "Grade": "D"},
           						  {"Exam": 30, "Grade": "D-"}
           						],
           			"Name"   : "Mohit Sharma"
           		}
	       ]

	for i in range(len(data)):
		print(data[i])


	#adding dict values to rows
	rows = []

	for d in data:
		data_row = d["Student"]
		time = d["Name"]

		for  row in data_row:
			row["Name"] = time
			rows.append(row)

	df = pd.DataFrame(rows)
	print(df)
	
if __name__ == '__main__':
	main()