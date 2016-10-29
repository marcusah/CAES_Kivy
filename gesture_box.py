from kivy.gesture import GestureDatabase
from kivy.uix.boxlayout import BoxLayout
from kivy.gesture import Gesture 

gesture_strings = {
    'left_to_right_line': 'eNq1mE1y3DYQhfe8iLXRFPofuICyTZUOkFLsKVllR5qSxkl8+zS7ZWWaFYfYaDajeQQf8PUDAVBXD18e/vx+uD++nL89H5dfXr9Pbbn6dILl9sPj3R/HD8sJ/U//ouXl9sPL+fnpy/HFf/Jy9fUky9V/mtxGs+Wkq5X5/aenh8fzeltfbxs/ue3XtdVyghzBOoTvfgvgctMOrQFpgz6odeEm1Nfx/L1ep+Xmuh2MGzJAM8HBXWV5+f3u/7vh6EaW+5/3cP/DvHU1Q0W2gebtd80DHSzNr+3AQm0gNGC3aXS8bvKvvWqXJm1oEzBk3bfvYT8m7QmVrI1GgJ3Jdu0xEkCYtG/aAQEVeus89iuPGPY0Zy8ioAjDBmjX1vftI1iUOXseStTfEoCJ6kS2aO/mH+HiZLiso1kfnYFJWPftKcKlyXAZGoqwsBFYh0H7/pEu0bv5R7w0GS+JzxkRVC+NDb931z7SJXsv+wiXJsMlAJRh0vvwpaftLwwc4fJkuL4aNP/YayPYLz5HuDwZLjLSIOjWjTxb3F8aOMLlyXCxIfo1BGZFvz4x/kiX7d38I16ejNcfWRrGAxuxNBu79hLxCryXfaQrk+m+7bU4RFHH/tIjka5Mpuvbiu+2zafoMCXfBfb9I12ZTNc3WzHxChHjMLS+//RKxCuT8b5NHEH0rdcmFjeNgHUmYPf3w8IAMFITtS77y4NGwEpz9uzLjwJZb6aGfT9fjXxV5uxNwfXmxy1jJtzf2DXiVZuyh8a9DViH7se53vZnj0a4OubsyY9UPvFxLcx6wNq1t4jW5qIFVWnYzISHL6Iz9hGtzUULozeVgb65+PFkYuJbJGtzySIOXxO88MqjC1lMnPXt4ePz8fj49i5gur4M+NWrG6ZDW24Yzb/OJ+vLnWtatLFqCpdab6FJ0WDVxqufpoarBtCLSCEiF5FDJC2ihGhYRF1FhNqRhUhwGJcfu2gRaGj1tmDzel6KI+B8aSpi0NGPMryKgUejFTHwuDKPwPNdoYiBx1J7DzzupToj8AS898uPXrQIPMHaQeAJFy9owedHv6oGoBhUNQilb9pSqqOqwehTsqqS0werGpSKG9VSlaoGmtJmZDktqTpATsw6jQCCTbk6AKZqVaVUKxsk26ZmkGyyaZts2qqabFqrA8mmG99k00qBybZJCJPNas0w2ayyYbL1OjJMtr7xTba+8U22vvFNtrHxTbZR2TDZRnWgZBu9qsFmrfoSplrHS5Rq7Y041U1vkmrNjYLNYNObpVpzo57qpreRaq0Zt1QrGycb1DFwstXH2E+TqdbeONmwzhJONqzEnGy46S3ZNs8QJxttxpBsVNkk2TbPmyQbVWJJNqpjkGTjWnU/r97l1vX5+HD/+bz+t8lPrzdr5i7+9fDp/Dk0XwJzLrl6fvp6fL57/HiMKxbb7aq/bqy/nZ6fPn37mF7dO/NXYD9kNfa5I92P6utWf/gHjU3d+Q==', 'right_to_left_line':'eNq1WNtuIzcMfZ8f2bxUEG+S+APpa4F8QJHuGtlgt4mReNvu35ci5bEMxDt+cWCcSeIzZ2QeiqR89/zt+Z+f6Wn3fvjxtlt+H9d9Xu6+7GF5+PTy+Pfu07JH+9UutLw/fHo/vL1+273bn7zcfd/LcvehyIPTln3pUtXu378+vxz6ba3fphdu+6Ozlj3ECvoSftotgMv9bznlzJmkYBHHLK0v6L9OoOU+J6EMXBkdQZf3vx5//RT2p8jytD6g1IJNFTu2ynV5fwpt1kaoSIG1bov7J4d6EofchFpu1LE2xZM4Q5YiEJhhW7y5uE7iIFNoYNLOx4h0LEyb4ujBR5jE15h0lFpWdSrrsg2lbccF0dXpRupuKU6WAkmzyMfLUuYUGcKzdJFtcbcUZ0sZp3xpsGpjWXPF8JqFu6Oot9AmN5TgmqAgSMmgJZCFt9XdUKIbqbuhJNekC8hZumwXAHJDqV6xjWxXzlvUUmFT3B0lvYk4u6UM11SXLGd5bjVgW949ZbqVvJvKc+FV1gwV1JHpWHj9PTNZmwSSvbut775yvZm+W8u63Tj6ewKl5loCUcq2u+LuyuRuFpqTvq9x1W/ErSkHMm13D3F3ZXL3g8Z6lAda125or215d1fkVvJurszmDlsDRcsUHagV0AaDwIZX6Lu5Mszt8rlaVgyErFakV3nEc3M31YtbW+CkDgxNx0utJ03B8fo2pea2ujtb6EbqbmyRkzr1gaIOrA1xUtdVGsUKxxWhcWNLPcmzDSygUDpihpM40VnOy/ZQU9zVMrkqkrVhy45cyqR+Hpjt/Vrd1DqZui67I1teT+qtWdxIA3sh3VJ3U+vJVNsz09IpT+JMa64bFtquZdVNrSdTQaZ0z9rnolWdzwPjkelngs9vu93LOuFbS7YR32bku3ujJs291Q9c7rG2HgO7BPJy2Ne2PAZZLFFRBgYZGaoNEYHS2RpsTsIIyAMvsFsONlkt4JJp4CU2BBsSQ6ECAzu7JuVWoQ4snY3OBk25YiYNDHLLCFoH9g/ZKMi27NqqcGAJtuVcsT3k6GQOMqaG1kFw4AWyODmXVG0nchnYySXZmGilaaAvunQ2q9qBqc9hA4NdaxEpga2Ta5Bzqsw2zw0swWabByzDHT167iM3YzdgO3o4tiATFdUS6Kt2G7loamy5qoEaZNDMVlYd0cjqLrJY7oANHG3gx8rqJlpdSFaYrd8M/HjN6h4yUTqJENWPw6HuISOmKjbqYGC7EGl1ExksmbCJTRaBYaJ1DoA60BfiLnLOqVUFK9WOl7JJ3UVSTlYmLakGlsjrrJbwLdA2r9HdRzswpGnr0YXtqG6jZViypsFAA4M83d6aS7uPVDidUs/QV6LpdLuhsa2mOF1sr88/HHQ7GVhVDCxOdy+JazruGMeubmmWnYJBsdo6b/FgWAsRP/kaorPdQmsgKRdRu8sRgr0+u2N1unto56wkKo3bwBp8acWPOB1juRJ0tgZYFTnQ1wJptdvR6eEiNHtyBWgDezAapmnjY47ghY1QLEcYqQRq0Nea0NHZ4SOIBcYOZTKws8lGF7JpcaCzw0cw19kShQbWoK97pmOnQ/hoyS3WJOxs41hcne1IY5MuD3Q6HOnHzHbkS3Q80q3d2VA7UC7R6Vd0tPrVeKBHxjbhY/Sur7vnp6+H/h0SGNt2zmxpfMP07/OXw1dn9Kyz+t202GUgdMrh9fvu7fHl885p1Q91/f+j5/65f3v98uNzPKZXi1R65y7UZ3e0lLZGmv4H3GXTZA==', 'down_to_up_line':'eNq1WMtu3EYQvPNHrIuJ7unX9A8o1wD+gEC2F7LgRFpI6yT++9TMkBQNZL0GhNWhVl4Xi8Ounpqmbh6+Pvz9fb4/vJy+PR+m35bPI003n488fXj3ePfX4d10LPgVHzK9fHj3cnp++np4wT91uvnzaNPN/4p86LTp6E0qcP3x6eHx1C6r7bI8c9nvjTUdeaygLeE7LuEy3b6n2dTNqRaV9KjF23L+bf8t0y3NJFKkRAYrCSnr9PLx7ud30X4Xm+7XGxBlVWWvSVSJp5f7RZvFokh1spqVLS9r9wfn2LS1Uo1grLsq17LTJtcirOZuEVLqL4jXLp6v4hYQDVSg18Ztp87kXNgkqHowX1YvvfhY4aouaWFuotUKPNBY1N/3xVOtVIxKEWWufFm+dHl5lbdSnSmLppTEQ+zla8CMJPaM1OJ+Wb6bWuxa8t3X8uprES+STNUiUYpiO3lm1Uwz4SgaYr9QnO5sySvJS7dW+Fry3VqRa8l3a+XVWq7odioQJgnD3XfqaEeB7eIuWYXssnp3Vl6dZXQFJCyNA71B+bbFd2clrySv3Vl9dZZQ91o5qChjAzj2xa7vE1+4WuGawHJZvjurci357qzateS7tfpqbWuPqIbIdA9D7NqbQkG7t7p4CwmsyhGInNRCU/VNgWndWuNVHWv3SoqauGute21RCrKsge8rynS5660ba3Id8W6r2XXEu6kWmzjOPxOpGlwVQvs0gJecoRk4GqtB/fIpaN1TyyvJezfVN1NREhF1juzV+aE2FC0eNEqoGLLhckN6d9XlSurdVt9sLThYjQ0Tk2J6wYSwmz5QGswOJIUDUac4OC+qd19981UMo55mi4HqGI924hilxkiS2KtU4heW3l31vIp4dE9j81QQYEVknH0o8L4ujDrVQMHwa6U+lVxS757G5imC0RAtFoy4MWi8ZeaLbmlslqogo3B4O5Hho8TFbm+vBp+eD4fHbdBHxTDpR0w3t5KJzY9gzQWnW2hisMziMVCn0zHqdNfIMeM0lxbLHR1s4RmRgZNwwdLoOeg611JaPQdqo0Mcq5dYMECvNOgyt8fCpD0QbGXcEO8VvGJj82CXWaO1xoLW6DrjJcBbDHT0Ri8rvVS8hZQFO91nS+SbL9jXIit9V5RCPui1uqov2NV10BmvKBh6eEGwjWe0LgsvKI1tg40XGpwzmH0Ggu1oSgxERANbzaHfyDXnBGDqGNjIObdIqLlgI8dK3qrdEI1RQmbPRMwMHDWsK70P4blgo6dhOETQ24J9KbnSGS8clAvCTyGfff/THjPpnDrSZt4q0rCxeWX/+FC3yPR5q2jDtpQsZ6oiMJ93zdL6MOVMvcV8brvEfGBt5M1K3v+AjAomp7Is2Mh2xnepMVfB4BsLNrKvZAwu3FKrIx5Rieat3xu2nspY6TWRJLwgWlCZ0OAYgKgjN3I9txu0wElivJoP5NYnmed2gwpasOAdlRYEm4nOqkuZ14ToqJ3P53aPYuOTp2UM5MEvZysj6If9Bd75cqbsqljOFipeorP1LBu9glHPdcGxGPsJ3bQwHnygdbr/hO67pIhRyjj7qD/G1hCvayQSXutZFpTG9nkXkqMscHUk/ZfDw/2XU/vTCxM2M9cZUy1ZXbD/oeifh8+nL52C5sY+2qIBiLuDcXr68/B89/jp0FljymrfL0fUH8fnp8/fPo3btMzAXgo0acGOJgzo7W3y4/wfIFqqZw=='  

}

#This database can compare gestures the user makes to its stored gestures 
#and tell us if the user input matches any of them.
gestures = GestureDatabase()
for name, gesture_string in gesture_strings.items():
    gesture = gestures.str_to_gesture(gesture_string)
    gesture.name = name
    gestures.add_gesture(gesture)

class GestureBox(BoxLayout):

	def __init__(self, **kwargs):
		for name in gesture_strings:
			self.register_event_type('on_{}'.format(name))
		super(GestureBox, self).__init__(**kwargs)

	def on_left_to_right_line(self):
		pass
	def on_right_to_left_line(self):
		pass
	def on_down_to_up_line(self):
		pass
	'''To recognize a gesture, you'll need to start recording each individual event in the
	touch_down handler, add the data points for each call to touch move, and then do the
	gesture calculations when all data points have been received in the touch up handler.'''

	def on_touch_down(self, touch):
		#create an user defined variable and add the touch coordinates 
		touch.ud['gesture_path'] = [(touch.x, touch.y)]    
		super(GestureBox, self).on_touch_down(touch)

	def on_touch_move(self, touch):
		touch.ud['gesture_path'].append((touch.x, touch.y))
		super(GestureBox, self).on_touch_move(touch)

	def on_touch_up(self, touch):
		try:
			if 'gesture_path' in touch.ud:
				#create a gesture object
				gesture = Gesture()    
				#add the movement coordinates 
				gesture.add_stroke(touch.ud['gesture_path'])
				#normalize so thwu willtolerate size variations
				gesture.normalize()
				#minscore to be attained for a match to be true
				match = gestures.find(gesture, minscore=0.3)
				if match:
					print("{} happened".format(match[1].name))
					self.dispatch('on_{}'.format(match[1].name))
				else:
					print "Nothing to see Here"
		except:
			print "gesture not found"

		super(GestureBox, self).on_touch_up(touch)






