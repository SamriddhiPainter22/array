#Initialize the array

arr =[1,2,3,4,5,6,7,8,9,12,13,14]

print("Elements of given array present on even position")

#looppThrough the array by incrementing the value i by 2
# here i will start with1 as the first even positioned element is present at position 1

for i in range(1,len(arr),2):
    print(arr[i])