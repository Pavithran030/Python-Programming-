1.	Write a program that generates a stream of random numbers and writes them to a file.

import random
with open('p1.txt','w') as file:
    		for i in range(10):
        			file.write(str(random.randint(1,100)))
        			file.write("\n")
file.close()


2.	Write a program to read the random numbers from the file created above and calculate their average.

av=0
with open('p1.txt','r') as file:
    for i in range(10):
        k=file.readline()
        av=av+int(k)
print("The Average of all value in the file p1.txt is :",av/10)
file.close()

3.	Write a program that reads from a file and handles the case where the file does not exist.

try:
    with open('p2.txt','r') as file:
        print(file.read())
except FileNotFoundError as e:
    print("Error! ",e)

4.	Create a user-defined exception NegativeNumberError that is raised when a negative number is encountered in a list.

def NegativeNumberError(num):
    return f"Negative number encountered: {num}"
def check(n):
    if n < 0:
        raise ValueError(NegativeNumberError(n))
    return "All numbers are non-negative."
num=int(input("Enter a number : "))
try:
    result = check(num)
    print(result)
except ValueError as e:
    print(e)

5.	Create a NumPy array of 10 random numbers and print them.

import random
import numpy as np
l=[]
for i in range(10):
    k=random.randint(1,20)
    l.append(k)
print(np.array(l))
    
    
6.	Write a program to add and remove items from a NumPy array.

import numpy as np
import random
l=[]
for i in range(10):
    k=random.randint(1,20)
    l.append(k)
n=np.array(l)
print(n)
while True:
    print("1.add\n2.remove\n3.Exit")
    p=int(input("Enter a number "))
    if p==3:
        break
    elif p==1:
        k=int(input("Enter a number to add :"))
        print(np.append(n,k))
    elif p==2:
        k=int(input("Enter a number to remove :"))
        print(np.delete(n,k))
    
    
7.	Sort the NumPy array which you created.

import random
import numpy as np
l=[]
for i in range(10):
    k=random.randint(1,20)
    l.append(k)
m=np.array(l)
print(m)
print(np.sort(m))

8.	Reshape a NumPy array into a 2x5 matrix.

import random
import numpy as np
l=[]
for i in range(10):
    k=random.randint(1,20)
    l.append(k)
m=np.array(l)
print("Normal Array :\n",m)
print("The reshape of the array is:\n",m.reshape(2,5))

9.	Demonstrate indexing and slicing on the reshaped matrix.

import random
import numpy as np
l=[]
for i in range(10):
    k=random.randint(1,20)
    l.append(k)
m=np.array(l)
print("Normal array is : ",m)
f=m.reshape(2,5)
print("Sorted array is : \n",f)
print("Slicing of the array:")
print("Specific Value ",f[1,2])
print("Range of Value ",f[0:2:4])


10.	Write a program to append new data to an existing file and then read the updated file.

k=int(input("Enter a number to add :"))
with open('p1.txt','a') as f:
    f.write(str(k)+'\n')
    print()
f.close()
with open('p1.txt','r') as q:
    p=q.read()
    l=p.split('\n')
    print(l[:(len(l)-2)])
q.close()


