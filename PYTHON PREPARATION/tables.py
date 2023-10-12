def tables(number):
    multiple =int(input("enter the multiple:"))
    for i in range(1,multiple+1): 
        print(number,"x",i,"=",number*i)
    
    

tables(int(input("enter the number:")))