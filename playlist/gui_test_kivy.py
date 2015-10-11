'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
#from kivy.logger import Logger
#import logging
#Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder

kv = '''
    BoxLayout:
        padding: 10
        spacing: 10
        size_hint: 1, None
        pos_hint: {'top': 1}
        height: 44
        Image:
            size_hint: None, None
            size: 24, 24
            source: './cccircles.png'
        Label:
            height: 24
            text_size: self.width, None
            color: (1, 1, 1, .8)
'''


class TestCamera(App):
    def build(self):
        return Builder.load_string(kv)

TestCamera().run()