import sys
import json
from matplotlib import pyplot as plt
import timeit


sys.setrecursionlimit(20000) # This is used to maximize the amount of recursion, this helps prevent a stack overflow error if something such as infinite recursion was implemented.

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high) # This is finding the pivot index, recursively, this is the index of the element that is in the correct posiiton
        func1(arr, low, pi-1) # This is calling on the bottom half of the array
        func1(arr, pi + 1, high) # This is calling on the top half of the array
def func2(array, start, end): # This is called on with the sub-array
    p = array[start] # First element of the sub-array -  This is set as the pivot
    low = start + 1 # low is the index of the second element in the sub-array
    high = end # high is set to the same value of the last element in the array
    while True:
        while low <= high and array[high] >= p:
            high = high - 1 # Goes down from the upper half of the sub-array downwards, stops when the upper index is less than the lower index or if the element value of the upper index is less than the pivot 
        while low <= high and array[low] <= p:
            low = low + 1 # Goes from the lower half of the sub-array (excluding the pivot which is the lowest index) and goes downwards only stopping when the lower index is greater than the upper index, or if the value of the lower index is greater than the pivot
        if low <= high: # Swaps the elements that violate the boundaries of the pivot
            array[low], array[high] = array[high], array[low] # Swaps the elements in the low and high indices, this syntax makes it so that you don't have to use a temp variable
        else: # The lower index is greater than the high or upper index, exiting the loop
            break
    array[start], array[high] = array[high], array[start] # Swaps the pivot with the new index of high, the pivot is now placed in the correct position
    return high # returns the index of the element that is correctly sorted

def main():
    with open("Exercise2/ex2.json", "r") as file:
        data = json.load(file)
    
    entry_length = []
    entry_time = []


    for entry in data:
        end_length = len(entry)
        entry_length.append(end_length)
        
        elapsed_time = timeit.timeit(lambda : func1(entry, 0, end_length - 1), number = 1)
        entry_time.append(elapsed_time)

    plt.plot(entry_length, entry_time)
    plt.title("Quicksort: Length of Data vs. Time")
    plt.xlabel("Data Size")
    plt.ylabel("Time")
    plt.show()

    with open("sorted.json", "w") as file:
        json.dump(data, file)

if __name__ == '__main__':
    main()