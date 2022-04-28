python

#Values and data types
x = None
y = True and False #Boolean 
z = -1 #integer 
a = .1 #float
b = 2 + 3j #complex
c = 'hey' #string
d = ('hi', True, 1) #tuple
e = ['hi', False, .01] #list
f = set(1, None, 'no') #set
g = {'a':None, True:1} #dictionary

#Variables >> numbers letters and underscores 
x, y
print(object(s), sep=separator, end=end, file=file, flush=flush)
#print a variable, file -> writing method, flush -> sees whether the outcome is true or false.
type(c) #print the value type of the variable 
##Operators 
#Arithmatic 
1 + 3
2 - 2
3 * 4 
7 / 2 
2 % 1 #divide and returns reminder 
4 ** 3 #exponetial 
-11 // 3 #floor division 
#Relational 
a == b #is
a != b #isnot
>
<
>=
<=
#Assignment
= 
+= #a += b >> a = a + b 
-= 
/=
%=
**=
//=
#Logical 
and 
or
not
#Operator Precedence
** 
~,+,- #complement and unary plus and minus
*,/,%,//
+, - #operators 
<=, >=, <, >
==, != 
=, +=, -=, /=, %=, **=, //=
is, is not #idnetity
in, not in #membership
not, or, and #logical
#Mathematical functions, built in 
abs()
round(x, n) #type(x)=float, n = nth round up
#Math module, math.f()
import math
math.ceil(x) #round up
math.factorial(x)
math.floor(x)
math.isfinite(x)
math.isinf(x)
math.isnan(x)
math.trunc(x)
math.exp(x)
math.log(x, 10) #(x,base)
math.log10(x)
math.sqrt(x)
math.cos(x)
math.sin(x)
math.tan(x)
math.degrees(x) #radian to degree
math.pi 
math.e
#Output function
print(1,2,3,4 ,sep='*', end=' hey')
#1*2*3*4 hey
#format
x = 3; y = 5 # all the operations must be seperated in line or semicolon
print('I love {} and {}'.format(x,y)) #Values assigned come out
print('I love {1} and {0}'.format('bread','butter')) #the numbers in {} assigns output values' order
print(f'I love {x} and {y}')
#input function >> adds a step before an assignment 
x = input("how are you?: ")

##Container manipulation 
#Strings
str(x) #makes characters in the function a string
int(x) #make the string to an integer
#Indexing >> gives an individual character,
word = "python" 
word[3]
#Slicing >> to obtain substring
word[0:2] #does not include the last index
word[::3] #step(starts from 0)
word[3::-1] #default is [0, the last index + 1, 1]
L = len(word) #shows the number of characters in the string
#Functions 
x.find(str) #determines str is in x or not 
x.count(str) #counts how many times does str repeats in x 
x.lower()
x.upper()
x.split(str) #deletes str in x and splits x 
x.replace(old, new) #relaces old characters in the string to new 
x.startswith(str) #determines whether x begins with str
x.endswith(str) #vice a versa 
x.isalpha() #does x contain only alphabet
x.isnumeric() #dodes x contain only numeric value
x.isalnum() #does x contain both numeric and alphabet 

a = 'a' + 'b' #this is possible. One can add variables between strings. 

#mutable >> idependent class(index changing occurs)
#immutable >> index replacing is impossible, but function might work
#String is immutable 
'\n' #next line
'\r' #carriage return and inserts 
'\t' #tab

#List >> mutable
list() >> #only one object available 
[] >> #or this
#indexing and slicing are similar 
a = list('cat')
#positive numbers are from left to right. negative numbers are from right to left. starting at 0 and -1 excluding.
print(a[0:2], a[2], sep ='\n')
#multi-dimension is also possible 
x = [[1,2],[3,4]]
print(x[0][1])
#updating lists
x[0] = [0,2]
print(x)
#list operations
[] + []
[] * int()
'a' in [] = True or False 
#list functions 
len(x)
min(x)
max(x)
del x[slice]
x.append(value)
x.extend(list)
x.pop(index)
x.remove(value)
x.count(value)
x.insert(index, value)
x.index(value) #states the index of 
x.sort()
x.reverse()
#copying list
#use _copy method or [:]

#Tuples 
(,) #indexing and slicing 
tuple()
#packign and unpacking
a = ('a', 'b', 'c')
x,y,z = a
print(x,y,z, sep = '\t') #print(x) will result 'a'
#changing the data in tuples are impossible but mutable data in tuples can change
a = ([1,2],)
a[0][1] = 'p'
#tuple operations
() + ()
() * int()
'a' in () = True or False 
#tuple functions 
len(x)
max(x)
min(x)
x.index(value)
x.count(value)

#Dictionary
#mutable and unordered
{}
dict()
#it can use a list of two-item tuples, lists and two character strings as input
#accessing value in dictionary
a = ['12', '24', '56'] #keys cannot be repeated 
d = dict(a)
d['1']
#adding new key and value
d['new value'] = 'hi'
#operation and functions 
'2' in d #only key works 
len(d)
del d[key]
d.clear()
d.items() #makes a dictionary into a tuple
d.keys()
d.values()
d.update(dict2) #adds dict2
tuple(d.values())
#coping dictionary 
a = d.copy()
del a['1']
a
d

#Set -> unique, unordered elements 
{}
set() #only with lists, strings, tuples and dictionaries (only with keys).
#empty set -> variable = set(), {} does not work 
#unordered -> slicing and indexing is impossible
#operations 
a = set('cat'); b = set([1,2])
'c' in a  
0 not in b
a == b
a != a
a <= a #subset
a >= b #superset
a - b 
a & b #intersection
a | b #union
a ^ b #aUb - a&b
#set functions 
len(x)
x.add(element)
x.update(element)
x.discard(element)
x.remove(element)
x.clear()
#coping set
a 
c = a.copy()
c.add('p')
c
a

##Control-flows # - comment, \ - line continues, tab - indentation
#if conditionals
if condition:
    statement

exam1 = 90; exam2 = 85

if exam1 >= 100:
    print('Good job! Jake')
elif exam2 >= 80: #the next condition. else if. 
    print('Good job! Joe')
else:
    print('Good!')

#when upper condition satisfied, the statement executes. Then, elif. Then, else. 

#for loop 
for iterating_var in iterable:
    statements 

a = 'key'

for i in 'key':
    print('key\'s characters are: ', i, sep = '\n')

range(a,b,i) #a list of integers that a <= x < b, seperated by i, a == 0 default. i == 1 

for i in range(len(a)):
    print('hihi:', a[i])

count = 0

for i in range(10):
    for j in range(10):
        count += j

x = range(0,10,2)
for i, j in enumerate(x): #enumerate() returns (index, value) of an iteratable
    print('index:', i)
    print('value:', j)

x = [(1,2,3)]
for i, j, k in x: #mutiple iterating_var
    print(k,j,i)

#while loop 
while condition: #must be true and not repeating, otherwise, does not work or infinite loop
    statement 

maxsum = 50 
sum = 0 
i = 0 
while sum <= maxsum:
    i += 1 
    sum += i
print('The sequence is:', list(range(1, i + 1)))

#Loop control statement 
break #a statement that terminates the loop and transfers to the next loop 

var = 10 
while var > 0:
    print('Current variable value:', var)
    var -= 1
    if var == 5: 
        break

continue #passes a control flow

for i in 'python':
    if i == 'p':
        continue 
    print('hi')

#list comprehension >> using logical expressions to build lists
#other containers can be built with comprehension 

[(x,y) for x in range(3) for y in range(4) if x + y < 3]

x = list(range(-5,5))
z_set = {x[i]**2 for i in range(len(x))}

z_tuple = tuple(i**3 for i in x)

word = 'letters'
letter_counts = {letter:word.count(letter) for letter in set(word)}

def function(var, ): #creating one's own function. Variable can follow order or assigned (var = x).
    return argument #function concludes as the argument, can be assigned as well.



class #creating a class 