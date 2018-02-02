class Solution:
    def binarySearch(self, arr, n):
        if not arr:
            return -1

        low = 0
        hi = arr.length - 1

        while low <= hi:
          mid = low + (hi - low) / 2

          if n < arr[mid]:
            hi = mid - 1
          elif n > arr[mid]:
            low = mid + 1
          else:
            return mid
        return -1