#Daniel Bandler
#4/23/18
#Asks user for a bunch of words, only prints ones with the letter "f"

words = input("Type in words ").split(" ")

for item in words:
    if "f" in item or "F" in item:
        print(item)
