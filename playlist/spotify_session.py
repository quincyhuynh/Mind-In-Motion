import spotify
import time
import random
import sys
import getpass
import previous

class session():
	def __init__(self, listener, controller):
		self.listener, self.controller = listener, controller
		self.session = spotify.Session()
		self.audio = spotify.AlsaSink(self.session)
		self.loop = spotify.EventLoop(self.session)
		self.logged_in = False
		self.playlist = None
		self.shuffledlist = None
		self.playlists = None
		self.track = None
		self.shuffle_mode = False 
		self.playlist_length = 0
		self.playlists_length = 0

	def login(self):
		username = ""
		password = ""
		# login_credentials a 2 line txt file
		with open("login_credentials.txt", "r") as f:
			username = f.readline()
			username = username.replace("\n", "")
			password = f.readline()
			password = password.replace("\n", "")
		print "Logging in..."
		self.session.login(username, password)
		timeout = 20000000
		time = 0
		while self.session.connection.state is not spotify.ConnectionState.LOGGED_IN:
			self.session.process_events()
			if self.session.connection.state is spotify.ConnectionState.LOGGED_IN:
				self.logged_in = True
				print "Connected"
				return
			time += 1
			if time >= timeout:
				print "Connection Failed: Timeout. Try Again"
				break
		self.login()

	def load_initial(self):
		if not self.logged_in:
			print "Not logged in"
			return
		self.playlists = self.session.playlist_container
		self.playlists.load()
		self.playlist_length = len(self.playlists)
		self.playlist = self.playlists[1]
		self.playlist.load()
		print "Current Playlist:", self.playlist.name
		self.playlist_length = len(self.playlist.tracks)
		copy = self.playlist.tracks[:]
		random.shuffle(copy)
		self.shuffledlist = copy
		self.track = self.playlist.tracks[0]

	def next_playlist(self):
		self.playlist_length = len(self.playlist.tracks)
		self.session.player.unload()
		curr_index = self.playlists.index(self.playlist)
		if curr_index < self.playlist_length - 1:
			self.playlist = self.playlists[curr_index+1]
		else:
			self.playlist = self.playlists[0]
		if self.shuffle_mode:
			copy = self.playlist.tracks[:]
			random.shuffle(copy)
			self.shuffledlist = copy
		self.playlist.load()
		print "Current Playlist:", self.playlist.name
		self.track = self.playlist.tracks[0]
		self.track.load()
		print self.track.name
		self.session.player.load(self.track)
		self.session.player.play()


	def prev_playlist(self):
		self.playlist_length = len(self.playlist.tracks)
		self.session.player.unload()
		curr_index = self.playlists.index(self.playlist)
		if curr_index < self.playlist_length - 1:
			self.playlist = self.playlists[curr_index-1]
		else:
			self.playlist = self.playlists[0]
		if self.shuffle_mode:
			copy = self.playlist.tracks[:]
			random.shuffle(copy)
			self.shuffledlist = copy
		self.playlist.load()
		print "Current Playlist:", self.playlist.name
		self.track = self.playlist.tracks[0]
		self.track.load()
		print self.track.name
		self.session.player.load(self.track)
		self.session.player.play()

	def mode_change(self):
		self.shuffle_mode = not self.shuffle_mode
		if self.shuffle_mode:
			copy = self.playlist.tracks[:]
			random.shuffle(copy)
			self.shuffledlist = copy
			self.track = self.shuffledlist[0]			
			print "Playback: shuffle"
		else:
			print "Playback: normal"

	def next(self):
		next_available = True
		if self.shuffle_mode:
			curr_index = self.shuffledlist.index(self.track)
			if curr_index < self.playlist_length - 1:
				self.track = self.shuffledlist[curr_index+1]
			else:
				next_available = False
		else:
			curr_index = self.playlist.tracks.index(self.track)
			if curr_index < self.playlist_length - 1:
				self.track = self.playlist.tracks[curr_index+1]
			else:
				next_available = False
		if next_available:
			self.track.load()
			print self.track.name
			self.session.player.load(self.track)
			self.session.player.play()
		else:
			print "No next song available"
			self.session.player.unload()

	def previous(self):
		prev_available = True
		if self.shuffle_mode:
			curr_index = self.shuffledlist.index(self.track)
			if curr_index:
				self.track = self.shuffledlist[curr_index-1]
			else:
				prev_available = False
		else:
			curr_index = self.playlist.tracks.index(self.track)
			if curr_index:
				self.track = self.playlist.tracks[curr_index-1]
			else:
				prev_available = False

		if prev_available:
			self.track.load()
			print self.track.name
			self.session.player.load(self.track)
			self.session.player.play()
		else:
			print "No previous song available"
			self.session.player.unload()

	def play_track(self):
		if not self.logged_in:
			return
		self.track.load()
		print self.track.name
		self.session.player.load(self.track)
		action = self.listener.get_frame(self.controller)
		play = False
		while action != "stop":
			# if action:
			# 	print action
			if action == "play/pause":
				time.sleep(0.5)
				play = not play
				if play:
					print "play"
					self.session.player.play()
				if not play:
					print "pause"
					self.session.player.pause()
			if action == "next":
				self.session.player.unload()
				print "next"
				time.sleep(0.5)
				self.next()
				play = True
			if action == "prev":
				print "prev"
				time.sleep(0.5)
				self.previous()
				play = True
			if action == "next playlist":
				time.sleep(1)
				self.next_playlist()
				play = True
			if action == "prev playlist":
				time.sleep(1)
				self.prev_playlist()
				play = True
			if action == "mode change":
				time.sleep(1)
				self.mode_change()
			action = self.listener.get_frame(self.controller)
			time.sleep(0.1)
		print "stop"
		self.session.player.unload()

