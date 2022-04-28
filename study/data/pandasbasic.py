import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv

#python data library that frames data. also involves cvs formats.

pd.Series(data, index = index) #1-d object, data can be any python data structure, index labels the data

s = pd.Series(np.random.randn(3), index = ('a', 'b', 'c')) #index can be any object container.

#attributes
s.index #gets index
s.values #gets values
s.shape #finds the shape 
s.value_counts() #frequency of each value
s.unique() #unique each value
#default is integers when index is not identified 
s = pd.Series([1,2,4,8,16,32,64])
s.index
#dictionary as data will generate the index automatically
s = pd.Series({2:'a', 1:'b', 3:'c'})
s = pd.Series({2:'a', 1:'b', 3:'c'}, index = [3,2]) #index identified, includes indexed keys and values only
#an element in pd.Series will duplicate
s = pd.Series(5, index = ['a', 'b', 'c']) #not working??
##data selection in Series 
#as a dictionary
s['b']; 'c' in s; s.keys() #dictionary functions are possible
#as an array
s[0:2] #implicit index is the same with numpy 
s['a':'c'] #explicit index will include the final index
#indexers 
s.loc['a':'c'] #using explicit indexing
s.iloc[0:3] #using implicit indexing


pd.DataFrame(data, index = index, columns = columns)
#2-d object, data can be pd.Series, dictionary of Series, dictionary of 1-d ndarrays or lists, 2-d numpy matrix, a list of dictinaries..
#index identifies rows and columns indentifies columns

s = pd.DataFrame(np.random.randn(4).reshape(2,2), index = index, columns = ('a', 'c'))

#attributes
s.index #gets index
s.columns #gets columns
s.shape #finds the shape 
s.values #gives a numpy array of values without index or columns

##creating pd.DataFrame
#single pd.Series
s = {'a':1, 'b':2}
s = pd.Series(s)
s = pd.DataFrame(s, columns = ['1']) #keys in Series -> index, keys in DataFrame -> columns
#dictionary of Series
s = {'a':1, 'b':2}
s = pd.Series(s)
t = {'a':3, 'b':4}
t = pd.Series(t)
u = pd.DataFrame({'a':s, 'b':t})
#dictionary of ndarrays or lists
s = {'a':[1,2,3], 'b':np.arange(3)}
s = pd.DataFrame(s)
#2-d ndarray
s = pd.DataFrame(np.random.rand(3,2), columns = ('a', 'b'), index = [1,2,4])
#list of dictionaries
pd.DataFrame([{'a':1, 'b':3}, {'b':2, 'c':3}])
pd.DataFrame([{'a':1, 'b':3}, {'b':2, 'c':3}], columns = ('a',)) #if there is no value in dictionary, NaN pops up

##data selection in DataFrame
#[]
s = pd.DataFrame(np.random.rand(3,2), columns = ('a', 'b'), index = [1,2,4])
s['a'] #indexing is for implicit or explicit column selection
s[1:4] #slicing is for implicit or explicit row selection. when index is integer, implicit is used
s[s['b'] >= 0.5] #select rows that satisfy boolean conditions on the columns
s[[,]] #numerical indexing for multiple column selection. both implicit and explicit
#.loc, [row, column]
s.loc[::,::] #operations used for s[] can be used for rows and columns explicitly 
#.iloc 
s.iloc[::, ::] #operations used for s[] can be used for rows and columns implicitly

#input function
pd.read_csv(filepath, arguments) #import csv file as pandas object
filepath = '', #cvs filepath in the operation system
sep = '' #character that splits each row
header = integer #selects the row that will be the column names. default is 0.
index_col = integer #selects the column that will be the row names. default is still 0.
names = [] #list of column names, use with header = None
skiprows = integer '''number of rows to skip from the first row.''' or [] #to identify rows to skip
na_values = () #sequence of values that will be considered as NA value
dtype = {'column name':dtype} #manipulate the dtypes of columns
#output function 
s.to_csv(filepath, arguments) #export DataFrame as csv file
sep = '' #character that splits each column. default is ','.
na_rep = '' #replace NA values. default is ''. 
index = True or False #implicit indexing will be included 
header = True or False #header will be preserved

##operation on pandas object
#unary operation such as numpy operations can be used. Indice and columns are preserved.
s = np.exp(s) #such as
s.sample(n, axis = axis, replace = boolean) #replace enables samples to be formed in the same columns or rows
s.describe() #useful summary values 
#binary operation of equal dimensional pd odjects. Various combined applications are possible
s + t, pd.add(s,t) #indice become a union, if values do not match NaN will pop out 
s - t, pd.sub(s,t)
s * t, pd.mul(s,t)
s / t, pd.div(s,t)
s // t, pd.floordiv(s,t)
s % t, pd.mod(s,t)
s ** t, pd.pow(s,t)

##DataFrame manipulation
#overall DataFrame
s.info() #index & dtypes
s.head(n) #get first n rows
s.tail(n) #get last n rows
s.copy() #copies a DataFrame
s.rank() #returns a rank of a DataFrame
s.sort_values(axis = axis, by = ['columns or indice that the others will follow'], ascending = boolean, inplace = boolean) #sorts the Dataframe
#the first column or row of the 'by' feature will be the standard, following will be sorted independently
s.sort_index(axis = axis, ascending = boolean, inplace = boolean) #sorts by index 
s.astype(dtype) #type conversion
#adding new columns
s['new_col'] = new_Series
s['new1', 'new2'] = new_DataFrame
#swaping columns
s['a','b'] = s['b', 'a']
#deleting columns and rows
s.drop['a', axis = axis, inplace = if False, return a copy, otherwise the change is applied directly]
del s.['col']
#find column duplication
s['a'].duplicated()
#element-wise methods and string-type operations are possible
s.replace([999, 0], np.NaN, inplace = True) #value, numerical indexing all possible #element-wise method example
s.str.startswith('prefix') #string-type operation example
#adding rows 
s.append(s.Series) #same column labels
#find row duplication
s.index.duplicate(::, boolean) #finds duplicated indice, boolean will be the duplicated indice
#math operations are possible 
s = s.diff() #such as differentions of DataFrame
#concatenation 
pd.concat([s, t], axis = axis, sort = boolean) #indice won't make a union but concatenate
#join = 'outer' = sorted union, 'inner' = intersection, join_axes = [container] -> selected indice, ignore_index = boolean -> implicit index
#aggregation 
s.apply(function, (condition to the function), axis = axis) #user defined function can be applied
s.groupby(by = [], axis = axis) #groups the DataFrame for a function. 
s.aggregate() #mutiple functions can be applied and return as a DataFrame
s.groupby('col1').aggregate([min, np.median, max]) #list of functions
s.groupby('col1').aggregate({'col2': min, 'col3': max}) #dictionary forms can be used
s.filter() #filters the Dataframe by groups using conditonal functions and return as a DataFrame
s.groupby('a').filter(lambda x: x.data.mean() > 3) #use it like this
s.transform() #transfroms Dataframe value by applying functions 
s.groupby('a').transform(lambda: x: x - x.mean()) #other column values will change according to the function