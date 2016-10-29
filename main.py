from kivy.app import App

from kivy.clock import Clock
from kivy.clock import Clock as clock

from kivy.config import Config
from kivy.gesture import Gesture,GestureDatabase

from kivy.graphics.vertex_instructions import (Rectangle,
                                               Ellipse)
from kivy.graphics.context_instructions import Color

from kivy.lang import Builder

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.anchorlayout import AnchorLayout

from kivy.garden.knob import Knob
from kivy.garden.gauge import Gauge
from kivy.garden.light_indicator import  Light_indicator

from kivy.properties import ListProperty, ObjectProperty



import collections 
import math
import os
import random
import sys
from math import *


import gesture_box as gesture

# This is where Kivy captures gestures.
class Runner(gesture.GestureBox):
	pass


#define the Screen Manager
class NuclearScreenManager(ScreenManager):
	pass
#define the screens
class NCPScreen(Screen):
	pass
class MenuScreen(Screen):
	pass
class KnobScreen(Screen):

	def __init__(self, **kwargs):
		super(KnobScreen, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init)
		


	def _finish_init(self,dt):
		self.knob_value = self.ids.knob1.value


		
	def pause():
		time.sleep(5)
	def stop(self):
		sys.exit()
	def start(self):
		pass


class NuclearControlPanel(Screen):

	def __init__(self, **kwargs):
				
		super(NuclearControlPanel, self).__init__(**kwargs)
		Clock.schedule_once(self._finish_init)
		Clock.schedule_interval(self.warning,0.1)


	def _finish_init(self,dt):
		self.gauge1 = self.ids.gauge1
		self.knob1 = self.ids.knob1
		self.knob1value = self.knob1.value
		self.warning1 = self.ids.warning1
		self.warning2 = self.ids.warning2
		self.warning3 = self.ids.warning3
		self.warning4 = self.ids.warning4

	def stop(self):
		sys.exit()
	def warning(self,dt):
		
		
		self.knob1 = self.ids.knob1
		self.knob1value = self.knob1.value
		self.value = self.knob1value
		if self.value >75:
			self.warning1.color = 'red'
			self.warning2.turn_on_off()
			self.warning3.turn_on_off()
			self.warning4.turn_on_off()
#		else:
#			self.warning. = 'grey'

#Building the app. The program will look for the file "nuclear.kv" because the app is called Nuclear			
class NuclearApp(App):
	def build(self):
		Config.set('graphics','fullscreen', 'auto')
		return NuclearScreenManager()
# Run the program
if __name__ == "__main__":
	NuclearApp().run()

