def sorting(list,param):
    
    if param == "asc":
        list.sort()
        print(list)
    elif param == "dsc":
        list.sort(reverse=True)
        print(list)
    elif param == "none":
        print(list)        
list=[1,5,6,8,2,3,7]
print(sorting(list,"none"))