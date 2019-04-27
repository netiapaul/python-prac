#  Question 1: Accept two int values from user and return their product. If the product is greater than 1000, then return their sum

a=int(input('Enter a number: '))
b=int(input('Enter a second number: '))
c=a*b
print(c)

if c > 1000:
    d=a+b
    print(d)

#  Question 2: Given a two list of ints create a third list such that should contain only odd numbers from the first list and even numbers from the second list

def mergeList(listOne, listTwo):
  thirdList = []
  for num in listOne:
    if(num % 2 != 0):
      thirdList.append(num)
  for num in listTwo:
    if(num % 2 == 0):
      thirdList.append(num)
  return thirdList
    
print("Merged List is")
listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]
print(mergeList(listOne, listTwo))

#  Question 3: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

rand=[value for value in range(1,21)]

for num in rand:
    if num % 5 == 0:
        print(num)

# Question 4: Given a list of ints, return True if first and last number of a list is same

numList = [10, 20, 30, 40, 10]

firstnum=numList[0]
lastnum=numList[-1]

if firstnum == lastnum:
    print(True)
else:
    print(False)

# Question 5: Given a string and an int n, remove characters from string starting from zero upto n and return a new string


def removeChars(str, n):
  return str[:n]
print("Removing n number of chars")
print(removeChars("programmer", 4))

# Question 6: Given a range of numbers. Iterate from o^th number to the end number and print the sum of the current number and previous number

def sumNum(num):
  previousNum=0
  for i in range(num):
    sum = previousNum + i
    print(sum)
    
print("Printing current and previous number sum in a given range")
sumNum(10)