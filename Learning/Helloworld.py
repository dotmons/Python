from collections import deque
import heapq



print("Hello world")
arr = [1,2,3,4,5,6]
print(arr[0])
print('Len of arr: ',arr[len(arr)-1])
print('Last element', arr[-1])
arr.append(7)
print('New element', arr)
arr.pop()
print('Elements after pop', arr)
#To remove the first two elements
arr.remove(3)

for element in arr:
    print('Value: ',element)


#Tuple: Immutable list
tup = (1,2,3)


my_dict = dict() 
#Dictionary, list a map
person = {"Name": "Dotun",
          "Age": 36,
           "City": "Guelph" }

print(person)
print(person["Name"])
# Used to remove values from Dictionary
del person["City"]
person.pop("Age")
print(person)



#Set: Just like hashset
number = {1,2,3,4,5,6}
number.add(6)
#throws error if not found
number.remove(4)
#no errror if not found
number.discard(5)
print('number', number)


# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Union → {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection → {3}
print(set1 - set2)  # Difference → {1, 2}


stack = deque()
stack.append(1)
stack.append(2)
print('stack value pop', stack.pop())
print('stack value: ', stack)



queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())  # 1 (FIFO)



pq = []
heapq.heappush(pq, (1, "low priority"))
heapq.heappush(pq, (0, "high priority"))

print(heapq.heappop(pq))  # (0, "high priority")



#Slicing
text = "Python Slicing"
print(text[7:])    # Output: "Slicing" (from index 7 to the end)
print(text[:6])    # Output: "Python" (from the beginning to index 6)
print(text[7:14])   # Output: "Slicing" (from index 7 up to index 14)
print(text[::2])    # Output: "Pto lcng" (every second character)
print(text[::-1])   # Output: "gnicilS nohtyP" (reverses the string)