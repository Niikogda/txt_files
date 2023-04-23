try:
    flag = False
    words=input("what do you wanna find? :")
    words+='\n'
    with open("user_finder.txt", "r") as file:
#    myfile = open("user_finder.txt", "w")
#    x=input("enter something pls: ")
#    res=myfile.write(x)
        for line in file: 
            print(line)
            if words == line:
                flag = True
                break
        if flag == True:
           print("line exist")
        else:
           print("line doesn`t exist")
except Exception as e:
        print(e)
finally:
        file.close()
