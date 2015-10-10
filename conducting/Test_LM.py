import os, sys, inspect, thread, time, play_wav, io
# src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# lib_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.append("../lib")
sys.path.append("../lib/x64")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class conductor_listener_trainer(Leap.Listener):
	first_call = 0
	curr_song = None
	def set_song(self, new_song):
		self.curr_song = new_song

	def on_connect(self, controller):
		print "Connected"
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

	def get_frame(self, controller):
		frame = controller.frame()

		for gesture in frame.gestures():
			if gesture.type is Leap.Gesture.TYPE_SCREEN_TAP:
				return "tap"
			if gesture.type is Leap.Gesture.TYPE_SWIPE:
				return "swipe"
			if gesture.type is Leap.Gesture.TYPE_CIRCLE:
				return "circle"
		# if frame.hands:
		# 	return "change"

# class conductor_controller(Leap.Controller):
# 	def __init__(self, conductor_listener_trainer):
# 		super

def create_training_set_play():
	listener = conductor_listener_trainer()
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)
	new_song = play_wav.song(sys.argv[1], listener, controller)

	new_song.play()
	controller.remove_listener(listener)


def main():
	# Create a sample listener and controller
	listener = conductor_listener_trainer()
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)
	new_song = play_wav.song(sys.argv[1], listener, controller)

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