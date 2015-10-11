import spotify
import time
import random
import sys
import getpass

class session():
	def __init__(self, listener, controller):
		self.listener, self.controller = listener, controller
		self.session = spotify.Session()
		self.audio = spotify.AlsaSink(self.session)
		self.loop = spotify.EventLoop(self.session)
		self.track = self.session.get_track('spotify:track:3N2UhXZI4Gf64Ku3cCjz2g')
	def login(self):
                username = raw_input("Username: ")
                password = getpass.getpass("Password: ")
		print "Logging in..."
		self.session.login(username, password)
		while self.session.connection.state is not spotify.ConnectionState.LOGGED_IN:
			self.session.process_events()
		print "Connected"
	def play_track(self):
		self.track.load()
		self.session.player.load(self.track)
		action = self.listener.get_frame(self.controller)
		play = False
		while action != "stop":
			if action == "play/pause":
				play = not play
				if play:
					self.session.player.play()
				if not play:
					self.session.player.pause()
			action = self.listener.get_frame(self.controller)
		self.session.player.unload()
