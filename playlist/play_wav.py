import pyaudio
import wave
import sys
import time
import random

class song: 
    CHUNK = 1024
    rate = 0
    
    def __init__(self, songs, listener, controller):
        self.songs = songs
        self.cur_song = songs[0]
        print self.cur_song
        self.pyaudio_object = pyaudio.PyAudio()
        self.wave_file = wave.open(self.cur_song)
        self.rate = self.wave_file.getframerate()
        self.listener, self. controller = listener, controller
        self.stream = self.pyaudio_object.open(format=self.pyaudio_object.get_format_from_width(self.wave_file.getsampwidth()),
                        channels=self.wave_file.getnchannels(), 
                        rate=self.rate,
                        output=True)
        self.pos = self.wave_file.tell()

    def shuffle(self):
        self.cur_song = random.choice(self.songs)
        print self.cur_song
        self.wave_file = wave.open(self.cur_song)
        self.rate = self.wave_file.getframerate()
        self.stream = self.pyaudio_object.open(format=self.pyaudio_object.get_format_from_width(self.wave_file.getsampwidth()),
                        channels=self.wave_file.getnchannels(), 
                        rate=self.rate,
                        output=True)
        self.pos = self.wave_file.tell()

    def play(self):
        self.rate = self.wave_file.getframerate()
        data = self.wave_file.readframes(self.CHUNK)
        self.wave_file.setpos(self.pos)
        play = False
        while data != '':
            action = self.listener.get_frame(self.controller)
            if action:
                print action
            if not action:
                if play: 
                    self.stream.write(data)
                    data = self.wave_file.readframes(self.CHUNK) 
                elif not play:
                    self.pos = self.wave_file.tell()
            elif action == "stop": 
                self.wave_file.rewind()
                self.pos = self.wave_file.tell()
                self.stream.stop_stream()
                self.stream.close() 
                return
            elif action == "shuffle":
                time.sleep(2)
                self.shuffle()
                play = True
                continue
            while self.listener.get_frame(self.controller) == "play/pause":
                time.sleep(1)
                play = not play
                if play:
                    self.stream.write(data)
                    data = self.wave_file.readframes(self.CHUNK) 
                elif not play:
                    self.pos = self.wave_file.tell()
        self.play()

    def end(self): 
        self.stream.stop_stream()
        self.stream.close() 






