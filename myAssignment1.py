'''
Created on 21 Sep 2018

@author: Chad Morrow
'''

import time

def performance_check():
    startTime = time.time()
    appendToNewList(read_garda_stations_tuples())
    endTime = time.time()
    print('APPEND: %f' % (endTime - startTime))
    
    startTime = time.time()
    insertBeginningOfList(read_garda_stations_tuples())
    endTime = time.time()
    print('INSERT: %f' % (endTime - startTime))
    
    startTime = time.time()
    predeterminedSizeList(read_garda_stations_tuples())
    endTime = time.time()
    print('COPY: %f' % (endTime - startTime))
    
def performance_check2():
    startTime = time.time()
    linearSearch(read_garda_stations_tuples(), 'Annascaul')
    endTime = time.time()
    print('LINEAR: %f' % (endTime - startTime))
    
    startTime = time.time()
    binarySearch(read_garda_stations_tuples(), 'Annascaul')
    endTime = time.time()
    print('BINARY: %f' % (endTime - startTime))
    
def performance_check3():
    startTime = time.time()
    builtInSort(read_garda_stations_tuples())
    endTime = time.time()
    print('BUILT IN: %f' % (endTime - startTime))
    
    startTime = time.time()
    bubbleSort(read_garda_stations_tuples())
    endTime = time.time()
    print('BUBBLE: %f' % (endTime - startTime))

def read_garda_stations_tuples():
    """ Read and return a list of garda stations. """
    all_stations = []
    file = open('garda_stations', 'r')
    for line in file:
        line = line.replace('\n','')
        new_tuple = tuple(line.split('\t'))
        all_stations.append(new_tuple)
    file.close()
    return all_stations
    
def appendToNewList(all_stations):
    emptyList = []
    for element in all_stations:
        emptyList.append(element)
    return emptyList

def insertBeginningOfList(all_stations):
    emptyList = []
    for element in all_stations:
        emptyList.insert(0, element)
    return emptyList

def predeterminedSizeList(all_stations):
    listSize = (len(all_stations))
    emptyList = [None] * listSize
    pos = 0
    while pos < len(all_stations):
        emptyList[pos] = all_stations[pos]
        pos += 1
    return emptyList

def linearSearch(all_stations, name):
    #index = 0
    for index in range(len(all_stations)):
        if name in all_stations[index]:
            return index
    return False   

def binarySearch(all_stations, name):
    all_stations.sort(key=lambda tup: tup[0]) #sorts by 1st position in the tuple, necessary for binarySearch
    start = 0
    end = len(all_stations) - 1
    
    while start <= end:
        mid = int((start + end) / 2)
        if all_stations[mid][0] < name:
            start = mid + 1
        elif all_stations[mid][0] > name:
            end = mid - 1
        else:
            return mid

def builtInSort(all_stations):
    all_stations.sort(key=lambda tup: tup[0])
    return 'QUIETEST: \n%s\n BUSIEST: \n%s' % (str(all_stations[0]), str(all_stations[len(all_stations) - 1]))

def bubbleSort(all_stations):
    for index in range(len(all_stations)):
        sorted = False
        for j in range(len(all_stations)- 1):
            if all_stations[index] < all_stations[j]:
                copy = all_stations[index]
                all_stations[index] = all_stations[j]
                all_stations[j] = copy
                sorted = True
                if(sorted == False):
                    break       
    return all_stations

#print (bubbleSort(read_garda_stations_tuples()))
#print(performance_check3())   
#print(builtInSort(read_garda_stations_tuples()))   
#print(performance_check2())        
#print(binarySearch(read_garda_stations_tuples(), 'Annascaul'))
#print(linearSearch(read_garda_stations_tuples(), 'Annascaul'))            
#print(performance_check())    
#print(predeterminedSizeList(read_garda_stations_tuples()))    
#print(insertBeginningOfList(read_garda_stations_tuples()))
#print(appendToNewList(read_garda_stations_tuples()))