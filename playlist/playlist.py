import os, sys, inspect, thread, time, play_wav, io, glob, spotify_session
sys.path.append("../lib")
sys.path.append("../lib/x64")

import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
class playlist_listener(Leap.Listener):
	def on_connect(self, controller):
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_INVALID);

	def get_frame(self, controller):
		frame = controller.frame()
		gestures = frame.gestures()
		types = [i.type for i in gestures]
		if len(frame.hands) == 0:
			return None
		# hand = frame.hands[0]
		# speed = hand.palm_velocity.magnitude
		if Leap.Gesture.TYPE_SWIPE in types:
			return "swipe"
 		if Leap.Gesture.TYPE_CIRCLE in types:
 			for gesture in gestures:
 				circle = Leap.CircleGesture(gesture)
				if (circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2):
				    return "next"
				else:
				    return "prev"
		if len(frame.hands) == 2:
			return "stop"
		if len(frame.hands) == 1:
			hand = frame.hands[0]
			num_fingers = len(frame.fingers.extended())
			if num_fingers == 0:
				return "play/pause"
			if num_fingers == 2:
				return "prev playlist"
			if num_fingers == 3:
				return "next playlist"
			if num_fingers == 5:
				return "mode change"
		time.sleep(0.1)


	def all_invalid(self, gestures):
		for i in gestures:
			if i is not i.is_valid:
				return False
		return True


def main():
	listener = playlist_listener()
	controller = Leap.Controller()

	controller.add_listener(listener)
	new_session = spotify_session.session(listener, controller)
	new_session.login()
	new_session.load_initial()
	new_session.play_track()

	controller.remove_listener(listener)

if __name__ == "__main__":
	main()
