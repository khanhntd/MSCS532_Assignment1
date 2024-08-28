
# insertionSort will following the two steps:
# Step 1: Detach the rightest element
# Step 2: Swap the each element from the current element's left side and swap it with the smallest element
# (since we are doing decreasing order)
def insertionSort(array: list[int]):
  for index in range(1, len(array)):
    key = array[index]
    j = index - 1

    while j >= 0 and key > array[j]:
      array[j+1] = array[j]
      j -=1
    array[j+1] = key


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

if __name__ =="__main__":
  arr = [12, 11, 13, 5, 6]
  insertionSort(arr)
  printArray(arr)