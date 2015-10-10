import pyaudio
import wave
import sys
import time

class song: 
    CHUNK = 1024
    rate = 0
    
    def __init__(self, current_song, listener, controller):
        self.cur_song = current_song
        self.pyaudio_object = pyaudio.PyAudio()
        self.wave_file = wave.open(current_song)
        self.rate = self.wave_file.getframerate()
        self.listener, self. controller = listener, controller
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
            print action
            # if not action:
            #     if play: 
            #         self.stream.write(data)
            #         data = self.wave_file.readframes(self.CHUNK) 
            #     elif not play:
            #         self.pos = self.wave_file.tell()
            # elif action == "stop": 
            #     self.wave_file.rewind()
            #     self.pos = self.wave_file.tell()
            #     self.stream.stop_stream()
            #     self.stream.close() 
            #     break
            # while self.listener.get_frame(self.controller) == "change":
            #     time.sleep(1)
            #     play = not play
            #     if play: 
            #         self.stream.write(data)
            #         data = self.wave_file.readframes(self.CHUNK) 
            #     elif not play:
            #         self.pos = self.wave_file.tell()
            time.sleep(0.1)

    def end(self): 
        self.stream.stop_stream()
        self.stream.close() 






