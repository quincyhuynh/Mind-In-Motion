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
		self.track = self.session.get_track('spotify:track:5nNmj1cLH3r4aA4XDJ2bgY')
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
			print action
			if action == "play/pause":
				time.sleep(0.3)
				play = not play
				if play:
					print "play"
					self.session.player.play()
				if not play:
					print "pause"
					self.session.player.pause()
			action = self.listener.get_frame(self.controller)
		print "stop"
		self.session.player.unload()
