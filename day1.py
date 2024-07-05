#------------- FUNCTIONS--------------#

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))


#-------------DICTIONARIES-------------#
ids= {'zainab':1, 'maham':2, 'Ahmad':3, 'hamza':4}
scores= {'zainab':20, 'maham':25, 'Ahmad':22, 'hamza':10} 

def fun1(ids, math):
    new_dict={}
    for name in math:
        new_dict[ids[name]]=[name,math[name]]
    return new_dict

fun1(ids, scores)

#------------ LIST COMPREHENSION------------------#
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"


#------------SET COMPREHENSION------------------#
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)  # Prints "{0, 1, 2, 3, 4, 5}"

#-------------------using numpy(arrays)-----------#
import numpy as np
a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
x = np.array([[1,2],[3,4]])


print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"


#makes 2d array then convert to 1d
e = np.random.random((4,2))
print("2D Array: ",e)
a = np.empty(8)
idx=0
for i in range(4):
    for j in range(2):
        a[idx] = e[i,j]
        idx+=1
print("1D Array: ",a)



#---------MATPLOTLIB-----------------#
import matplotlib.pyplot as plt
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

#---------------USING OS-----------------#
import os
from datetime import datetime
print(os.getcwd())
print(os.listdir())
#os.mkdir('Day3')
# os.rmdir('Day3')
time = os.stat('Day1.py').st_mtime
print(datetime.fromtimestamp(time))
#file_path= os.path.join()
print(os.path.dirname('/tmp/test.txt'))


#-----------USING DATES------------------#
import datetime
d = datetime.date(2024,6,4)
print(d)
today=datetime.date.today()
print(today.day)

tdelta= datetime.timedelta(days=7)
print(tdelta)

#-----------FILES--------------#

# f= open('text.txt', 'r')
with open('text.txt', 'r') as f:
    content = f.read()
    print(content)

print(f.name)

f.close()

#---------------Generators---------------------#
def squares(nums):
    for n in nums:
        yield(n*n)

def simple_sq(nums): #takes more mem
    new_list=[]
    for n in nums:
        new_list.append(n*n)
    return new_list

my_nums = squares([1,2,3,4,5])
simple=simple_sq(nums)
print(my_nums)
print(next(my_nums))
print(next(my_nums))
print(list(my_nums))

#--------Decorator--------------#
def outer(msg):
    message=msg
    def inner(): #wrapper func called first then outer func runs
        print( message)
    return inner

func=outer('HI')
func() 
#helps in logging(how many times a function runs, can also find time it runs in)

#----------------IMAGE MANIPULATION--------#
from PIL import Image
image1= Image.open('dog5.jpg')
image1.save('dog5.jpg')
image1.show()
image1.convert(mode='L'.save('dog_mod.jpg'))