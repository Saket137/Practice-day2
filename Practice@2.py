
#Date: 23/02/2022

#Factorial of a number

import math
number=int(input("Enter the Number:"))
print("The factorial of ",number,"is:",int(math.factorial(int(number))))


#print first and last element
elements=input("Enter the elements:")
b=str(elements)
d=b.split(",")
print(d[0], d[-1])


#DIffernce between append and extend

#Append
set1=[0,2,4,6,8]
set2=[1,3,5,7,9]
set1.append(set2)
print(set1)

#Extend

set1=[0,2,4,6,8]
set2=[1,3,5,7,9]
set1.extend(set2)
print(set1)


#Difference b/w del and clear

#del
num1=[1,2,3,4,5,6]
num2=[7,8,9,10]
num3=[10,12,14,16,18]
num3.remove(14)
del num1[1]
num2.clear()
print(num1)
print(num2)
print(num3)



