#Daniel Bandler
#4/13/18
#middleWord.py -- prints middle word

words = input("Input words ").split(" ")

length = len(words)

if length%2==0:
    print(words[((length)//2)-1:(length)//2+1])
else:
    print(words[((length)//2)])
