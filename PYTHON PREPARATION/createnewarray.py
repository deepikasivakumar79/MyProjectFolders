# creating a new array 

# using for loop
length = int(input("Enter the length of array: "))
array = []
for i in range (length):
    arr = int(input("Enter the number: "))
    array.append(arr)
print(array)

# while loop

def array1(n):
    array = []
    while(n > 0):
        arr = int(input("Enter the number: "))
        array.append(arr)
        n = n-1
    return array
print(array1(int(input("Enter the length of array: "))))