'''
Created on 12 Oct 2018

@author: Chad Morrow
'''
# Tracks 3 values for each node
# The next node, previous node, and element (Track info)
class DLLNode:
    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode

#You could have other fields for e.g. the mp3 file, the album it came from
#The artiste or band image, the size of track, the genre, bpm, etc.
# Track class takes in the name of the song, artist of the song, and the number of times played        
# In our example cases the user defaults to 0 because it is a new track in their playlist, but can be any value at the beginning
class Track:
    def __init__(self, name, artiste, timesplayed):
        self.name = name
        self.artiste = artiste
        self.timesplayed = timesplayed
    
    def __str__(self): 
        stringSong = []
        stringSong.append("(" + str(self.name) + ", " + str(self.artiste) + ", " + str(self.timesplayed) + ")")
        return ''.join(stringSong)
    
    def get_name(self):
        return self.name
    
    def get_artiste(self):
        return self.artiste
    
    def play(self):
        self.timesplayed += 1
        return str(self.name) + ", " + str(self.artiste)

# Doubly Linked List created with a head and tail node with no elements to represent the ends
# A cursor can be moved around to call the current track much quicker than iterating through the entire list to find the item
# MY dummyCursor is used for printing in the __str__ method and play_all() methods to ensure the real cursor is not touched
class PyToonz:
    def __init__(self):
        self.head = DLLNode(None, None, None)
        self.tail = DLLNode(None, self.head, None)
        self.head.next = self.tail
        self.size = 0
        self.cursor = self.head
        self.dummyCursor = self.head
     
    #Loop that add the tracks to a list
    #The list is joined and printed with new line value already added for viewing purposes    
    def __str__(self):
        trackList = []
        self.dummyCursor = self.head
        while self.dummyCursor.next.element != None:
            if self.dummyCursor.next == self.cursor and self.dummyCursor.next != self.tail and self.dummyCursor.next != self.head:
                trackList.append(">>>" + str(self.dummyCursor.next.element))
            else:
                trackList.append(str(self.dummyCursor.next.element))
            self.dummyCursor = self.dummyCursor.next
        return '\n'.join(trackList) + "\n"
 
    #Adds track to the end of the list     
    def add_track(self, track):
        newTrack = DLLNode(track, None, None)
        newTrack.prev = self.tail.prev
        newTrack.next = self.tail
        self.tail.prev.next = newTrack
        self.tail.prev = newTrack
        self.size += 1     
    
    #Returns the current track     
    def get_current(self):
        #returns NONE when the cursor is at the tail or head because it has no elements
        if self.cursor == self.head or self.cursor == self.tail:
            return None
        #Otherwise it returns the name and artist of the track
        return "Current Track: " + str(self.cursor.element.name) + ", " + str(self.cursor.element.artiste) + "\n"
    
    #Sets the current track to the next track  
    #loops around to the head when the cursor is at the tail
    def next_track(self):         
        if self.cursor == self.tail:
            self.cursor = self.head
        else:
            self.cursor = self.cursor.next
    
    #Sets the current track to the previous track 
    #loops around to the tail when the cursor is at the head
    def prev_track(self):    
        if self.cursor == self.head:
            self.cursor = self.tail
        else:
            self.cursor = self.cursor.prev
    
    #changes the cursor to the head node
    def reset(self):  
        self.cursor = self.head
    
    #Simulates the track being played
    #DOES NOT play an mp3 file, but can be added later if wanted 
    def play(self):
        #calls the Tracks play() method
        if self.cursor != self.head and self.cursor != self.tail:
            print("Playing: " +  str(self.cursor.element.play()) + "\n")
        else:
            #Returns None if the cursor is on the head or tail
            return None
    
    #Removes the current node from our list 
    def remove_current(self):
        #if there are no elements it will return None
        if self.size == 0:
            return None
        
        #If the user is trying to remove the head or tail it will return NONE
        if self.cursor == self.head or self.cursor == self.tail:
            return None
        
        #REDUCE SIMILAR CODE!!!!!!!!!!!!  
        #Removes the current node and makes the succeeding track the current track
        else:
#             create temp variable to clear data
            temp = self.cursor.next
            temp.prev = self.cursor.prev
            self.cursor.prev.next = self.cursor.next
            self.cursor.prev = None
            self.cursor.element = None
            self.cursor.next = None
            self.cursor = temp
            temp = None
        self.size -= 1
    
    #returns the number of tracks in our list
    def length(self):
        print(self.size)
    
#     Moves the current track to the "k" location in the list
#     first track is the 0
    def move_to_pos(self, k): 
        index = 0
        
        #If the user inputs a location too long or negative it outputs a prompt
        if k > self.size and k > 0:
            return None
            
        #Connects the surrounding nodes of the current track
        #Cuts ties with any node by setting next and prev to None
        self.cursor.next.prev = self.cursor.prev
        self.cursor.prev.next = self.cursor.next
        self.cursor.prev = None
        self.cursor.next = None
        
        #Iterates through the list until the user's location is found
        while index != k:
            self.dummyCursor.next
            index += 1
            
        #REDUCE SIMILAR CODE!!!!!!!!!!!!    
        #Connects the current node to the surround nodes of the location
        #Redirects prev and next of the surrounding nodes to the current node, finishing the insert
        self.cursor.next = self.dummyCursor.next
        self.cursor.prev = self.dummyCursor
        self.cursor.next.prev = self.cursor
        self.cursor.prev.next = self.cursor
        
    #Outputs a prompt that each song is being played by iterating through with a dummy cursor and calling the play method
    def play_all(self):
        self.dummyCursor = self.head
        while self.dummyCursor.next.element != None:
            print("Playing: " + str(self.dummyCursor.next.element.play()))
            self.dummyCursor = self.dummyCursor.next
    
rapPlaylist = PyToonz()
firstSong = Track("Promises", "Calvin Harris & Sam Smith", 0)
rapPlaylist.add_track(firstSong)
secondSong = Track("Eastside", "Benny Blanco/Halsey/Khalid", 0)
rapPlaylist.add_track(secondSong)
thirdSong = Track("I Love It", "Kanye West and Lil Pump", 0)
rapPlaylist.add_track(thirdSong)
print(rapPlaylist)
rapPlaylist.next_track()
rapPlaylist.remove_current()
rapPlaylist.length()