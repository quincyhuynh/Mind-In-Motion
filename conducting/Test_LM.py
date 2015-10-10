import os, sys, inspect, thread, time
# src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# lib_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.append("../lib")
sys.path.append("../lib/x64")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class conductor_listener_trainer(Leap.Listener):
	def on_connect(self, controller):
		print "Connected"
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.frame().fps = 4

	def on_frame(self, controller):
		frame = controller.frame()
		play = False
		pause = False
		end = False
		if not frame.hands:
			pause = True
			return
		for gesture in frame.gestures():
			if gesture.type is Leap.Gesture.TYPE_SWIPE:
				play = True
			if gesture.type is Leap.Gesture.TYPE_CIRCLE:
				end = True
		if play:
			print "keep playing"
			return
		elif end:
			print "end song"
			return

class conductor_controller(Leap.Controller):
	def __init__(self):
		self = Leap.Controller()

def create_training_set_play():
	listener = conductor_listener_trainer()
	controller = conductor_controller()
	print "Press Enter to stop training"
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		# Remove the sample listener when done
		controller.remove_listener(listener)


def main():
	# Create a sample listener and controller
	listener = conductor_listener_trainer()
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		# Remove the sample listener when done
		controller.remove_listener(listener)

if __name__ == "__main__":
	main()