#!/usr/bin/env python
# coding: utf-8

# In[ ]:

question 1 solutions

a=[]
l=range(2000,3201)
for i  in l:
    if i%7==0 and i%5 != 0:
        a.append(i)
print(a)


# In[ ]:

question 2 solutions

l=input("enter  the first name: ")
m=input("enter the last name: ")

print("your first name reverse {} and last name {}".format(l[::-1],m[::-1]))


# In[ ]:

question 3 solutions

x=int(input("enter the daimeter"))

volume = 4/3*3.14*((x/2)**3)
print(volume)


# In[ ]:

question 4 solutions

x=input("enter your comma seperated number :")
y =list( x.split(","))
print(y)


# In[ ]:

question 5 solutions

x=  int(input("enter the number of rows"))
for row in range(1,x+1):
    for col in range(1,row+1):
        print("*", end="")
    print("")
for row in range(x-1,0,-1):
    for col in range(1,row+1):
        print("*", end="")
    print("")


# In[ ]:

question 6 solutions

x= input("enter any thing  i will print it reverse")
print("Reverse of your entry is  {}".format(x[::-1]))











# In[ ]:




