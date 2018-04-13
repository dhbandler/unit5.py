#Daniel Bandler
#4/13/18
#listdemo.py --- How to use lists

words = input("Enter some words:    ").split(" ")


print("The first word was ", words[0])
print("The last word was ", words[-1])

#print out list 1 item at a time

for item in words:
    print(item)
