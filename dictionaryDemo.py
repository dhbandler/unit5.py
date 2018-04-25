#Daniel Bandler
#4/25/18
#dictionaryDemo.py --- more list practice

words = ["computer", "mortify", "dog", "firetruck", "yes", "python", "cat"]

words.sort()

num = int(input("what number word do ya want? "))

if num <= 0 or num>=len(words)+1:
    print("Invalid number you degenerate swine")
else:
    print(words[num-1])