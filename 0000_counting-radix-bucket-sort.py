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
counting_sort(arr)
print("Sorted Array in Ascending Order: ", arr)

arr = [412, 235, 207, 84, 389, 39, 155]
print("Original array: ", arr)
radix_sort(arr)
print("Sorted Array in Ascending Order: ", arr)

arr = [.42, .32, .33, .52, .37, .47, .51]
print("Original array: ", arr)
bucket_sort(arr)
print("Sorted Array in Ascending order:", arr)