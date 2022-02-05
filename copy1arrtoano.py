
#initialize the array
arr1=[1,2,3,4,5]

#creat another array

arr2 =[None]*len(arr1)


#copying all elements of one array to another
for i in range(0,len(arr1)):
    arr2[i] = arr1[i]


    #Displaying elements of array arrr1
print("Elements of original array : ")
for i in range(0,len(arr1)):
    print(arr1[i]),

print()


#displaying array2 elements

print("Elements of new array : ")
for i in range(0,len(arr2)):
    print(arr2[1]),

