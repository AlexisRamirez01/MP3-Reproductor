""" 
In this module i make the logic for the reproductor. The reproductor its basically a circular queue
where this structure allows you to go through the song directory forwards and backwards. 
"""

import os
from collections import deque
import random
from pydub import AudioSegment
from pydub.playback import play
import threading
import time

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
        self.pause = threading.Event()
        self.next_song = False
        self.back_song = 0 #If 0 == normal, 1 == repeat the current song, 2 == back to the past song
        self.songs = songs
        self.current_song = None
        self.mode = False #If true, activate the random reproduction
        self.thread = None

    def play_song(self):
        #Now start in other thread the reproduction
        if self.thread and self.thread.is_alive():
            return #Cannot allow more reproductions
        
        self.pause.clear() #If the reproduction is paused, we restart
        self.thread = threading.Thread(target=self._play_loop, daemon=True)
        self.thread.start()

    #This function change the reproduction mode and control the pause
    def _play_loop(self):
        while not self.pause.is_set():
            if not self.songs:
                print("Don't have song to reproduction.\n")
                break

        #If the mode of reproduction are changed
        if self.mode:
            self.current_song = random.choice(list(self.songs))
            sound = AudioSegment.from_mp3(self.current_song)
        else:
            self.current_song = self.songs[0]
            sound = AudioSegment.from_mp3(self.current_song)
        
        #Now this is  the loop to management the reproduction
        start = 0
        while start < len(sound):
            #If pause is activeated, we wait the flag
            self.pause.wait()
            chunk = sound[start: start+1000]
            play(chunk)
            start += 1000
        self.next_song(self)
        
    
                
    #Change the mode in normal reproduction to shuffle reproduction
    def change_mode(self):
        self.mode = True
        return self.mode

    #Change the flag to stop the reproduction
    def stop_reproduction(self):
        if not self.pause.is_set():
            self.pause.set()
        else:
            self.pause.clear()

    #Rotate to the left the list of the songs 
    def next_song(self):
        self.songs.rotate(-1)
        print(f"{self.songs}")
        self.current_song = self.songs[0]
        print(f"{self.current_song}")

    #Rotate to the right the list of the songs if the counter is two
    def back_song(self):
        self.back_song +=1 
        if self.back_song >= 2:
            self.songs.rotate(1)
            self.current_song = self.songs[0]
        return self.back_song





    
        

