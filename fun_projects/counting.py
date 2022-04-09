def count(word):
    vowels = "aeiou" 
    countvowel = 0
    for letter in word:
        if letter in vowels:
            countvowel +=1
    print(countvowel)  
print(count("toast"))                



