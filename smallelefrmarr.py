#initialize an array
arr = [23,4,54,44,65,9]

#initialize min with the first element of the array

min = arr[0]


#loop through the array

for i in range(0,len(arr)):
    
    #compare the elements of array with min

    if(arr[i]<min):
        min=arr[i]

        print("Smallest element if the given array : "+str(min))
