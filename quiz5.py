#Daniel Bandler
#5/7/18
#quiz5.py


#Penultimate takes a list and returns second to last element

list1 = input("Entrevous some words here:    ").split(" ")
print("The first penultimate word is: ", list1[-2])


#plusEquals takes a list and an integer and adds the integer to each num in list
list2=[]
list2.append(int(input("Type some numbers ")).split(" "))
num1 = int(input("Input the integer here "))
for i in list2:
    list2[i-1] += num1
print(list2)


#decimalRange finds range of numbers you gave it
numb1 = int(input("Enter the first number here "))
numb2 = int(input("Enter the second number here "))
numb3 = int(input("Enter the third number here "))

args = [numb1, numb2, numb3]

print((max(args)-min(args)))


