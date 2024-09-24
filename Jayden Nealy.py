def insertElement(arr, n): #Inserts and element into an array using arr and n
    arr.insert(0,n) #arr.insert will insert the array at position (0,n)
n = 7 #n is the element being inserted
arr = [3,6,4,8] #arr is the array

print("Before the insert: ") #Prints the array before the insert of 7
print(arr)

insertElement(arr,n)
print("After the insert: ") #Prints the array after the insert of 7
print(arr)

#The time complexity is O(n) because my code inserts element n, n times