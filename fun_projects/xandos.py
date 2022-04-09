def xandos(word):
    x_count = 0
    o_count = 0
    for letter in word:
        if letter == "x":
            x_count +=1   
        elif letter == "o":
            o_count +=1
    if x_count == o_count:
        print(True)
    else:
        print(False)    
xandos("bomber")        