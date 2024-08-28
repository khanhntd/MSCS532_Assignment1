

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