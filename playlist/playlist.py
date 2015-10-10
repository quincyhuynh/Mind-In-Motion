import os, sys, inspect, thread, time, play_wav, io, glob
# src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# lib_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.append("../lib")
sys.path.append("../lib/x64")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class playlist_listener_trainer(Leap.Listener):
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

# class conductor_controller(Leap.Controller):
# 	def __init__(self, conductor_listener_trainer):
# 		super

# def create_training_set_play():
# 	listener = conductor_listener_trainer()
# 	controller = Leap.Controller()

# 	# Have the sample listener receive events from the controller
# 	controller.add_listener(listener)
# 	new_song = play_wav.song(sys.argv[1], listener, controller)

# 	new_song.play()
# 	controller.remove_listener(listener)


def main():
	# Create a sample listener and controller
	listener = playlist_listener_trainer()
	controller = Leap.Controller()
	songs = glob.glob("*.wav")

	# # Have the sample listener receive events from the controller
	controller.add_listener(listener)
	new_song = play_wav.song(songs, listener, controller)

	new_song.play()
	# Keep this process running until Enter is pressed
	# print "Press Enter to quit..."
	# try:

	# 	sys.stdin.readline()
	# except KeyboardInterrupt:
	# 	pass
	# finally:
	# 	# Remove the sample listener when done
	controller.remove_listener(listener)

if __name__ == "__main__":
	main()