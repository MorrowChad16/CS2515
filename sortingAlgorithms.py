'''
Created on Oct 8, 2018

@author: Chad
'''

import time
import random
from random import randint

def testRunTime(givenLength):
    selectionSortArray = []
    bubbleSortArray = []
    insertionSortArray = []
    shellSortArray = []
    mergeSortArray = []
    quickSortArray = []
    heapSortArray = []
    
    while len(insertionSortArray) < givenLength: #creates array of givenLength filled with random values between 0 and 100 to test run time
        randInteger = randint(0, 100)
        selectionSortArray.append(randInteger)
        bubbleSortArray.append(randInteger)
        insertionSortArray.append(randInteger)
        shellSortArray.append(randInteger)
        mergeSortArray.append(randInteger)
        quickSortArray.append(randInteger)
        heapSortArray.append(randInteger)
        
    
    startTime = time.time()
    selectionSort(selectionSortArray)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("SELECTION:", elapsedTime)
    print(selectionSortArray)
        
    startTime = time.time()
    bubbleSort(bubbleSortArray)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("BUBBLE:", elapsedTime)
    print(bubbleSortArray)
    
    startTime = time.time()
    insertionSort(insertionSortArray)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("INSERTION:", elapsedTime)
    print(insertionSortArray)
    
    startTime = time.time()
    shellSort(shellSortArray)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("SHELL:", elapsedTime)
    print(shellSortArray)
    
    startTime = time.time()
    listx = mergeSort(mergeSortArray)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("MERGE:", elapsedTime)
    print(listx)
    
    startTime = time.time()
    listy = quickSort(quickSortArray)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("QUICK:", elapsedTime)
    print(listy)
    
    startTime = time.time()
    heapSort(heapSortArray)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("HEAP:", elapsedTime)
    print(heapSortArray)
    
def selectionSort(arrayValues):
    for i in range(len(arrayValues)):
        mini = min(arrayValues[i:]) #find minimum element
        min_index = arrayValues[i:].index(mini) #find index of minimum element
        arrayValues[i + min_index] = arrayValues[i] #replace element at min_index with first element
        arrayValues[i] = mini                  #replace first element with min element
    return arrayValues    

def bubbleSort(arrayValues):
    sorted = False  # We haven't started sorting yet

    while not sorted:
        sorted = True  # Assume the list is now sorted
        for i in range(len(arrayValues) - 1):
            if arrayValues[i] > arrayValues[i + 1]:
                sorted = False  # We found two elements in the wrong order
                hold = arrayValues[i + 1]
                arrayValues[i + 1] = arrayValues[i]
                arrayValues[i] = hold
    return arrayValues

def insertionSort(arrayValues):
    for i in range(1, len(arrayValues)):
        j = i
        while j > 0 and arrayValues[j - 1] > arrayValues[j]:
            arrayValues[j - 1], arrayValues[j] = arrayValues[j], arrayValues[j - 1]
            j -= 1
            
def generate_increments_sequence(length):
    """Generate the sequence of increments needed by shellsort
    for a sequence of the given length"""
    e = 2.718281828459
    increment_sequence = []
    counter = 0
    while True:
        counter += 1
        current_value = int(round(e ** (counter - 2)) + 1)
        if current_value >= length:
            break
        increment_sequence.append(current_value)
    return increment_sequence

def shellSort(sequence):
    """Sort a sequence using the shell sort algorithm
    :sequence: the sequence to be sorted
    """
    seq_len = len(sequence)
    increment_sequence = generate_increments_sequence(seq_len)

    for incr in increment_sequence:
        # loop through each subset of the sequence
        for j in range(incr):
            # loop through each element in the subset
            for k in range(j, seq_len, incr):
                guess = k
                # find the correct place for the element
                while guess >= incr and sequence[guess - incr] > sequence[guess]:
                    sequence[guess], sequence[guess - incr] = sequence[guess - incr], sequence[guess]
                    guess -= incr

    return sequence

def mergeSort(arrayValues):
    result = []
    if len(arrayValues) < 2:
        return arrayValues
    mid = int(len(arrayValues) / 2)
    y = mergeSort(arrayValues[:mid])
    z = mergeSort(arrayValues[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j]) 
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
#     arrayValues = result
    return result

def quickSort(arrayValues):
    less = []
    equal = []
    greater = []

    if len(arrayValues) > 1:
        pivot = arrayValues[0]
        for x in arrayValues:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        # Don't forget to return something!
        return quickSort(less)+equal+quickSort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return arrayValues
    
# def heapSort(arrayValues):
#     # convert aList to heap
#     length = len(arrayValues) - 1
#     leastParent = length / 2
#     for i in range(leastParent):
#         moveDown(arrayValues, i, length)
#  
#     # flatten heap into sorted array
#     for i in range (length):
#         if arrayValues[0] > arrayValues[i]:
#             swap(arrayValues, 0, i )
#             moveDown(arrayValues, 0, i - 1 )
# 
#  
# def moveDown( aList, first, last ):
#     largest = 2 * first + 1
#     while largest <= last:
#         # right child exists and is larger than left child
#         if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
#             largest += 1
#  
#     # right child is larger than parent
#     if aList[largest] > aList[first]:
#         swap( aList, largest, first )
#         # move down to largest child
#         first = largest;
#         largest = 2 * first + 1
#     else:
#         return # force exit
#  
#  
# def swap(A, x, y):
#     tmp = A[x]
#     A[x] = A[y]
#     A[y] = tmp

testRunTime(1000)