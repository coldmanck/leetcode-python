'''
K-Messed Array Sort
Given an array of integers arr where each element is at most k places away from its sorted position, code an efficient function sortKMessedArray that sorts arr. For instance, for an input array of size 10 and k = 2, an element belonging to index 6 in the sorted array will be located at either index 4, 5, 6, 7 or 8 in the input array.

Analyze the time and space complexities of your solution.

Example:

input:  arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2

output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer k

0 ≤ k ≤ 20
[output] array.integer
'''
def sort_k_messed_array(arr, k):
  '''
  Inspired by bucket sort
  Time O(nlogk) Space O(k)
  '''
  def insertion_sort(arr):
    for i in range(1, len(arr)):
      j = i
      while j > 0 and arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
    return arr
        
  if k == 0:
    return arr

  bucket_size = k + 1
  n_bucket = len(arr) // bucket_size
  if not len(arr) % bucket_size:
    n_bucket += 1
  for j in range(bucket_size): # O(k)
    for i in range(n_bucket): # O(n/k)
      start, end = i * bucket_size + j, min(len(arr), (i + 1) * bucket_size + j)
      if start < len(arr):
        arr[start:end] = insertion_sort(arr[start:end])
        # arr[start:end] = sorted(arr[start:end])
  return arr