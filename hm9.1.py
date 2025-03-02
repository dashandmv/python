a = "<"*50 + "5"*100 + "7"*30
while "<<<" in a or "555" in a or "7777" in a:
    if "<<<" in a:
        a = a.replace("<<<", "5" , 1)
    elif "555" in a:
        a = a.replace("555" , "7<" , 1)
    elif  "7777" in a:
        a = a.replace("7777" , "<<" , 1)
print(a.count("7")*7 + a.count("5")*5)
    
