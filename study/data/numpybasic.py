import numpy as np

#python data library for arrary manipulation (linear algebra)

#array -> a collection of matrices
#ndarray -> an N-dimensional array in python, created with list or tuple

a = np.array([2, 3, 4]) #a list in the array function creates a vector array
#tuples in the list creates row vectors in the matrix
b = np.array([(1.5 ,2 , 3), (4 , 5, 6)]) 
#lists in the biggest list in the array function seperated with commas create a 3-dimesional array 
c = np.array([[(1.5, 2, 3), (4, 5, 6)],[(3, 2, 1), (4, 5, 6)], [(1, 2, 3),(1 ,2, 3)]])
# 4-D array -> the array of 3-D array
d = np.array([[[(1, 2),(3, 4)],[(1, 2),(3, 4)]],[[(1, 2),(3, 4)],[(1, 2),(3, 4)]]])

#ndarray attribution functions
ndarray.ndim #returns the dimnension of the array
ndarray.shape #returns the number of elements in the vectors, matrices, 3-D array, ... and so on in a tuple (from right to left).
ndarray.size #returns the total number of elements in the vectors of the array
ndarray.dtype #returns the types of elements in the vectors of the array

#ndarray data types
#the machine language formations are different
'int32'
'int64'
'float32'
'float64'
'complex128' #data that can express complex numbers 
'bool' #true or false

#ndarray creating functions 
np.zeros(shape) #creates an array with zeros
np.ones(shape) #creates an array with ones
np.eye(n) #creates an identity matrix with n-rows
np.empty(shape) #creates an array with random elements in the memory 
np.full(shape, fill_value) #creates an array with full_value
np.arange(start, end, step, dtype) #creates a vector of integer sequence
np.linspace(start, end, num-points, dtype) #creates a vector of real numbers that are uniformly space between the range
np.random.seed([seed]) #generates random seed
np.random.rand(shape) #random xs' probabilities ~ uniform[0,1) -> the range of x is given for all the next dists
np.random.randn(shape) #random xs' probabilities ~ N[0,1]
np.random.randint(low, high, shape) #random numbers among the range with the size
np.random.binomial(n, p, shape) #random xs' probabilities ~ b(n,p) 
np.random.chisquare(df, shape) #random xs' probabilities ~ chi(df)
np.random.exponential(lam, shape) #random xs' probabilities ~ exp(gamma)
np.random.f(df1, df2, shape) #random xs' probabilities ~ f(df1, df2)
np.random.normal(mean, sd, shape) #random xs' probabilities ~ N[mean,sd]
np.random.poisson(lam, shape) #random xs' probabilities ~ pois(lam)
np.random.standard_t(shape) #random xs' probabilities ~ t(df)
np.random.uniform(a, b, shape) #random xs' probabilities ~ uniform(a,b)

##accessing values in the array
#indexing single elements
ndarray[coordinate] #0-based, following nd.array.shape.
d[1, 1, 1, 0]
#slicing subarrays
ndarray[start:stop:step, ::, ::] #-1 step means reversed array. A double colon means the whole array.
d[1, 1, 1,::-1]
#assigments are possible. Numpy would convert assigned data automatically. 
d[1, 1, 1 , ::-1] = np.array([1, 2])
d.dtype #int64
d[1, 1, 1, ::-1] = np.array([1, 2.2]) #2.2 will be coverted to 2
#copying. Since arrays are mutable, to hold in the changes by creating whole new data '.copy' need use.
a = np.arange(10)
c = a[::2].copy()
c[0] = 12 #if '.copy' is not used, a would have changed also.
#reshaping arrays -> the # of elements must be equal
grid = np.array(range(6)).reshape((3, 2))
#np.newaxis creates another dimension with the value 1
a.shape #(10,)
a = a[:, np.newaxis]
a.shape #(10,1)
#array concatenation, array dimensions should match
np.vstack([a, b]) #adds vertical upward -> the last shape number should match
np.hstack([a, b]) #adds horizontal right -> the first shape number should match
#splitting of arrays 
a, b = np.vsplit(ndarray, the number of seperation or shape, axis) #splits vertical vectors 
a, b = np.hsplit(ndarray, the number of seperation or shape, axis) #splits horizontal vectors

#element operations
a + b, np.add(a, b) #adds scalar to every scalar, vector to every vector, matrix to matrix, and array to array
a - b, np.subtract(a, b) #subtracts scalar, vector, matrix, and array
-a, np.negative(a) #returns negative a 
a * b, np.multiply(a, b) #multiplies them
a / b, np.divide(a, b) #divides them 
a // b, np.floor_divide(a, b) #floor divides them 
a ** b, np.power(a, b) #powers them
a % b, np.mod(a, b) #mods them 
a == b, np.equal(a, b) #returns a boolean array
a != b, np.not_equal(a, b)
a < b, np.less(a, b)
a <= b, np.less_equal(a, b)
a > b, np.greater(a, b) 
a >= b, np.greater_equal(a, b) 
np.bitwise_and(a, b), a & b #returns a logical result array of a & b. Scalars as binary boolean.
np.bitwise_or(a, b), a | b   

#functions
np.exp(a) #returns an array of exp(elements)
np.log(a) #returns an array of ln(elements)
np.log10(a) #returns an array of log10(elements)
np.sqrt(a) #returns an array of elements^(1/2)
np.sin(a), np.cos(a), and np.tan(a) #coverts element = radian to ratio of triangle
np.rint(a) #rounds up the elements to the nearest integers
np.ceil(a) #returns elements to ceiling
np.floor(a) #returns elements to floor
np.abs(a) #returns elments as absolute values  
np.isnan(a) #returns boolean for elements whether they are NaN(Not a number) or is
np.isfinite(a), np.isinf(a) #returns boolean for elements whether they are finite or not

##broadcasting -> the way numpy deals with operations with arrays in different sizes and shapes
#rule 1. 1s are added to the smaller arrary's dimension index to match the bigger array's
#rule 2. 1s will match the bigger array's dimension index by duplicating itself 
a = np.ones((2,3))
b = np.arange(3)
a + b #b.shape will be (3,) -> (1,3) then duplication -> (1*2, 3) to satisfy rule 2
#rule 3. if rule 1 and 2 cannot make the array's dimensions the same, error occurs
a = np.ones((3,2))
b = np.arange(3)
a + b #causes error

#aggregations

"""
intuition about the axis
the function: axis will gather the elements with indices differ only in the nth position.
for example, if x = [[1,2],[3,4]] then x[0,0] = 1, x[0,1] = 2, x[1,0] = 3, and x[1,1] = 4
given n is 0, axis will group x[0,0] and x[1,0], also x[0,1] and x[1,1]
following operations will be done within the group and return the result   
"""

np.sum(a,axis = n), np.nansum(a, axis = n) #computes the sum of elements 
np.prod(a, axis = n), np.nanprod(a, axis = n) #computes the product of elements
np.mean(a, axis = n), np.nanmean(a, axis = n) #computes the mean of the elements
np.std(a, axis = n), np.nanstd(a, axis = n) #computes the standard deviation
np.var(a, axis = n), np.nanvar(a, axis = n) #computes variance
np.max(a, axis = n), np.nanmax(a, axis = n) #find the maximum value
np.min(a, axis = n), np.nanmin(a, axis = n) #find the minimum value
np.median(a, axis = n), np.nanmedian(a, axis = n) #computes the median of elements
np.percentile(a, q, axis = n), np.nanpercentile(a, q, axis = n) #computes rank based statistics of elements.
np.any(a, axis = n) #evaluate any element is true
np.all(a, axis = n) #evaluate all element is true

#sorting and searching function
np.sort(a, axis = n) #None will give a vector. Axis will work the same and sorting will reposition scalars
np.argsort(a, axis = n) #returns the changed indices of the elements
np.argmax(a, axis = n) #returns the maximum scalar indices among groups
np.argmin(a, axis = n) #returns the maximum scalar indices among groups
np.nonzero(a) #returns indices of each dimension of elements that are non-zero
np.where(condition, x, y) #condition will return indices 
#x statement will print elements that satiesfy the condition applying the statement to the elements 
#y statement will print elements that does not

#set logic function
np.unique(a) #finds unique elements 
np.intersect1d(a,b) #finds the intersection
np.union1d(a,b) #finds the union
np.in1d(a,b) #returns a boolean array showing elements in a is also in b

#linear algebra function
np.transpose(a) #transposes an array
np.dot(a) #matrix multiplication
np.diag(a, k = n) #changes square matrix -> 1-d of diagonals, k will give off diagonals, or 1-d array to diag
np.trace(a) #computes the sum of diagonal elements 
np.linalg.det(a) #computes the matrix determinant
np.linalg.eig(a) #computes the eigenvalue and eigenvectors of a square matrix
np.linalg.inv(a) #computes the inverse of a square matrix
np.linalg.qr(a) #computes the QR decomposition
np.linalg.svd(a) #computes the SVD (singular value decomposition)
np.linalg.solve(a) #sloves Ax = b, A being a square matrix 

#logical indexing
condition with a #returns a boolean array
a[condition] #returns elements that satisfy the condition

#mixing
a[1:3, np.sum(a < 1, 0) >= 3] #conditions and functions can be used in slicing subarrays

#numerical indexing
a[array]
x = np.random.randint(100, size = 10)
ind = [3,5,7]
x[ind]
#can contain an element repeated values
ind = [3,3,7]
x[ind]
#easy to design the result array
ind2 = np.arrary([[3,7],[5,5]])
x[ind2]
#for tensors, think about the result of indice returning function of numpy and reverse it
#broadcasting occurs for multiple arrays
row = np.array([0,1,2])
col = np.array([2,1,3])
x[row, col] #since it is 2-d
x[row[:,np.newaxis], col] #broadcasting happens for row[:,np.newaxis] with col then indexing done
#slicing can mix
x = x = np.random.randint(100, size = 9).reshape(3,3)
x[:,[1,2]]
#also can be mixed with logical indexing

#assignment with broadcasting
#assignment is possible for numerical indexing
x = np.arange(-2,2.0) 
x[[0,1,2]] = np.array([3.14, 3.14, 3.14])
#does not have to match since broadcasting will happen
x[:2] = 99.0 

#since logical and numerical indexing copys the result 
#unlike slicing which the result is still connected to the original
#use this property well