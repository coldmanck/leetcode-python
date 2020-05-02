# Time: worst=avg=best O(n^2)
# Space: O(1)
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Time: worst=avg=best O(n^2)
# Space: O(1)
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr


# Time: worst=avg O(n^2), best O(n)
# Space: O(1)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr

# Time: worst O(n^2), best=avg O(nlogn)
# Space: O(1)
def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)

def quick_sort_helper(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort_helper(arr, left, pivot - 1)
        quick_sort_helper(arr, pivot + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    new_pivot_idx = left
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[i], arr[new_pivot_idx] = arr[new_pivot_idx], arr[i]
            new_pivot_idx += 1
    arr[new_pivot_idx], arr[right] = arr[right], arr[new_pivot_idx]
    return new_pivot_idx


# Time: worst=avg=best time O(n+k) where k is the size range (k=10 here). Thus it is linear time when k is O(n)
# Space: O(n+k)
# Counting sort is used when:
# - there are smaller integers with multiple counts and in small range k=O(n).
# - linear complexity is the need.
def counting_sort(arr, div=1): # arr in the range of 0-9
    count = [0] * 10
    out = [0] * len(arr)
    # count the occurrence
    for i in arr:
        count[i // div % 10] += 1 # count[i] += 1
    # transform into cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # put element into correct location
    for i in range(len(arr) - 1, -1, -1): # note here we need to go backward from the end since we are inserting backward too
        out[count[arr[i] // div % 10] - 1] = arr[i] # out[count[arr[i]] - 1] = arr[i]
        count[arr[i] // div % 10] -= 1 # count[arr[i]] -= 1
    arr[:] = out[:] # put results back to the original array

# Time: O(d*(n+k)) where k is the base range (k=10 here), d is the nb of digit of the maximum element. 
#       If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers 
#       then it can perform in linear time however the intermediate sort takes large space.
# Space: O(n+k)
# Radix sort is used when:
# - DC3 algorithm (Kärkkäinen-Sanders-Burkhardt) while making a suffix array.
# - places where there are numbers in large ranges, e.g. sort 32-bit numbers (d=32)
def radix_sort(arr):
    div = 1
    max_num = max(arr)
    while max_num // div > 0:
        counting_sort(arr, div)
        div *= 10

# Time: worst O(n^2), avg=best O(n+k)
#   where O(n) is the complexity for making the buckets and O(k) is the complexity for sorting the 
#   elements of the bucket using algorithms having linear time complexity at the best case (e.g. insertion/bubble sort).
# Space: O(n+k)
# Bucket sort is used when:
# - input is uniformly distributed over a range.
# - there are floating point values
def bucket_sort(arr): # all elements range [0.0, 1.0)
    buckets = [[] for _ in range(10)]
    for i in arr:
        buckets[int(i * 10)].append([i])
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])
    arr[:] = [nb for bucket in buckets for nb in bucket]

arr = [4, 2, 2, 8, 3, 3, 1]
print("Original array: ", arr)
bubble_sort(arr)
print("Bubble sort in Ascending Order: ", arr)

arr = [4, 2, 2, 8, 3, 3, 1]
selection_sort(arr)
print("Selection sort in Ascending Order: ", arr)

arr = [4, 2, 2, 8, 3, 3, 1]
insertion_sort(arr)
print("Insertion sort in Ascending Order: ", arr)

arr = [4, 2, 2, 8, 3, 3, 1]
quick_sort(arr)
print("Quick sort in Ascending Order: ", arr)

arr = [4, 2, 2, 8, 3, 3, 1]
counting_sort(arr)
print("Counting sort in Ascending Order: ", arr)

print('---')
arr = [412, 235, 207, 84, 389, 39, 155]
print("Original array: ", arr)
radix_sort(arr)
print("Radix sort in Ascending Order: ", arr)

print('---')
arr = [.42, .32, .33, .52, .37, .47, .51]
print("Original array: ", arr)
bucket_sort(arr)
print("Bucket sort in Ascending order:", arr)