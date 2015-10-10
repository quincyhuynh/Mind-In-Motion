import pyaudio
import wave
import sys

class song: 
    CHUNK = 1024
    rate = 0
    
    def __init__(self, current_song):
        self.cur_song = current_song
        self.pyaudio_object = pyaudio.PyAudio()
        self.wave_file = wave.open(current_song)
        self.rate = self.wave_file.getframerate()
        
        self.stream = self.pyaudio_object.open(format=self.pyaudio_object.get_format_from_width(self.wave_file.getsampwidth()),
                        channels=self.wave_file.getnchannels(), 
                        rate=self.rate,
                        output=True)
        self.pos = self.wave_file.tell()

    def play(self, action, pause, stop): 
        if action: 
            return

        self.rate = wave_file.getframerate()
        data = self.wave_file.readframes(CHUNK)
        self.wave_file.setpos(self.pos)
        while data != '' and not pause and not stop: 
            self.stream.write(data)
            data = self.wave_file.readframes(CHUNK)
        if pause: 
            self.pos = self.wave_file.tell()
            return 
        elif stop: 
            self.wave_file.rewind()
            self.pos = self.wave_file.tell()
            return
        end(self)

    def end(self): 
        self.stream.stop_stream()
        self.stream.close()





