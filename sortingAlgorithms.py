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
    
    while len(insertionSortArray) < givenLength: #creates array of givenLength filled with random values between 0 and 100 to test run time
        randInteger = randint(0, 100)
        selectionSortArray.append(randInteger)
        bubbleSortArray.append(randInteger)
        insertionSortArray.append(randInteger)
        
    
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
            
testRunTime(1000)