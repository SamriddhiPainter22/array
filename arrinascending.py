#initialize an array
arr=[40,3,77,65,9,23]

temp=0

#displaying elements of original array

print("Elements of original array : ")

for i in range(0,len(arr)):
    print(arr[i],end=" ")


    #sort the array in ascending order

    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):

            if(arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp

print()

#displaying elements if array aftr sorting

print("Elements of array sorted in ascen ding order : ")

for i in range(0,len(arr)):
    print(arr[i],end=" ")