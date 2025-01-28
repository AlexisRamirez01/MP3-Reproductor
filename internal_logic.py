""" 
In this module i make the logic for the reproductor. The reproductor its basically a circular queue
where this structure allows you to go through the song directory forwards and backwards. 
"""

import os
from collections import deque
import random
from nava import play

def create_songs_queue(directory):
    queue_songs = deque()
    #First, we are cheaking if the directory exist and if not empty
    if os.path.exists(directory) and os.path.isdir(directory):
        if not os.listdir(directory):
            print("The directory is empty.\n")
            return queue_songs
        else:
            #Its already for open the directory and load the songs
            songs = [file for file in os.listdir(directory) if file.endswith(('.mp3', '.wav'))]
            queue_songs.extend(songs)
            return queue_songs
    else:
        print("The directory doesn't exist.\n")
        return queue_songs

class Reproductor:
    def __init__(self, songs):
        self._pause = False
        self._next_song = False
        self._back_song = 0 #If 0 == normal, 1 == repeat the current song, 2 == back to the past song
        self._songs = songs
        self._current_song = None
        self._mode = False #If true, activate the random reproduction

    #Later make the methods for the class 

    
        

