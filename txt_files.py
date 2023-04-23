try:
    myfile = open("tasks.txt", "r")
    res=myfile.read()
    print(res)
except Exception as e:
        print(e)
finally:
        myfile.close()
