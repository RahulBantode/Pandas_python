# Pandas_python
The repository contains the application on pandas library using python language

There are three main data structure in pandas :
1. Series
2. Dataframe
3. Panel

1. Series :- It is a one dimensional array which is created by using Series class constructor by passing the parameter to it.
             Syntax :- 
             import pandas 
             import numpy 
             
             def main():
                arr = numpy.arange(1,20,2)
                series = pandas.Series(arr)
                print(series)
             
             if __name__ == "__main__":
                  main()
  
  2. DataFrame :- Its two dimensional array where data is stored in the form of row and columns where each column and entire row consider as series
  
  3. Panel :- Panel define as the nested dataframes, means dataframes of dataframe but from python version 3.6 after it depriecated by the python
              to use the functionality of panel we have to create nested dataframes.
              
             
