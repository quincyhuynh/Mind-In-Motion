import os, sys, inspect, thread, time, play_wav, io, glob, getpass
sys.path.append("../lib")
sys.path.append("../lib/x64")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class playlist_listener(Leap.Listener):
	def on_connect(self, controller):
		print "Connected"
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_INVALID);

	def get_frame(self, controller):
		frame = controller.frame()
		types = [i.type for i in frame.gestures()]
		if len(frame.hands) == 0:
			return None
		# if Leap.Gesture.TYPE_KEY_TAP in types:
		# 	return "shuffle"
		if Leap.Gesture.TYPE_SWIPE in types:
			return "play/pause"
 		if Leap.Gesture.TYPE_CIRCLE in types:
			return "shuffle"
		if len(frame.hands) == 2:
			return "stop"

	def all_invalid(self, gestures):
		for i in gestures:
			if i is not i.is_valid:
				return False
		return True


def main():
	listener = playlist_listener()
	controller = Leap.Controller()

	controller.add_listener(listener)
	new_session = session(listener, controller)
	new_session.login()
	new_session.play_track()

	controller.remove_listenier(listener)

if __name__ == "__main__":
	main()
