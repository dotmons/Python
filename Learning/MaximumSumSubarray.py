def max_sum_subarray(arr, k):
    max_sum, window_sum = 0, sum(arr[:k])  # Initial window sum
    max_sum = max(max_sum, window_sum)
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]  # Slide the window
        max_sum = max(max_sum, window_sum)
    return max_sum


def reverseString(val: str) -> str:
    left: int = 0
    right: int = len(val)
    result: str = ""

    while (left<right):
        result += val[right-1:right]
        right -= 1
    return result

        
txt = "Dotun"
#print(len(txt))

print(reverseString("Dotun"))


arr = [20, 19, 21, 15, 2, 20]
k = 3
print(max_sum_subarray(arr, k))  # Output: 9
