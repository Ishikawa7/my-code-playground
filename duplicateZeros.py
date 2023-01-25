# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
def duplicateZeros(self, arr):
    i = 0 
    while i < len(arr):
        if arr[i] == 0:
            for j in range(len(arr)-1, i, -1):
                arr[j] = arr[j - 1]
            i = i + 1
        i = i + 1