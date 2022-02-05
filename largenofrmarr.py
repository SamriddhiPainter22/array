

#initialize an array
arr = [23,4,54,44,9]

#initialize max with the first element of the array

max = arr[0]


#loop through the array

for i in range(0,len(arr)):
    
    #compare the elements of array with min

    if(arr[i]>max):
        max=arr[i]

        print("largest element if the given array : "+str(max))
