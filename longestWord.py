#Daniel Bandler
#4/23/18
#longestWord.py picks longest word in string

words = input("Input words here ").split(" ")

longest = ""
for i in words:
    if len(i) > longest:
        longest = words
        