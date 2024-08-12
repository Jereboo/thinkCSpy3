"""
Whack a mole game- based on ThinkCSpy3 lesson 14.31 (not my original work)
"""

import tkinter as tk
from tkinter import PhotoImage

class WhackAMole:
	#Can adjust number of moles in window
	NUM_MOLES_ACROSS = 4	
	
	def __init__(self):
		self.window = tk.Tk()
		self.mole_frame, self.status_frame = self.create_frames()
		self.mole_photo = PhotoImage(file= "small_mole.gif")
		self.mole_buttons = self.create_moles()
	
	def create_frames(self):
		#Width & Height arguments removed as framework adjusts for it with addition of moles in this frame?
		mole_frame = tk.Frame(self.window, bg='red')
		mole_frame.grid(row=1, column=1)
		
		#H arg. removed as it will adjust window height based on number of moles?
		status_frame= tk.Frame(self.window, bg='green', width=100)
		status_frame.grid(row=1, column=2, sticky= tk.E + tk.W + tk.N + tk.S)
		
		return mole_frame, status_frame
	
	def create_moles(self):
        # Source of mole image: https://play.google.com/store/apps/details?id=genergame.molehammer (Huh?- this is not a link to a static image, but a playable whackamole game??)
	 	
	 	mole_buttons = []
	 	for r in range(WhackAMole.NUM_MOLES_ACROSS):
	 		row_of_buttons = []
	 		for c in range(WhackAMole.NUM_MOLES_ACROSS):
	 			mole_button = tk.Button(self.mole_frame, image=self.mole_photo)
	 			mole_button.grid(row=r, column=c, padx=8, pady=8)
	 			
	 			row_of_buttons.append(mole_button)
	 			
	 		mole_buttons.append(row_of_buttons)
	 		
	 	return mole_buttons
	 	
#Creates the GUI Program
program = WhackAMole()

#Start the GUI event loop
program.window.mainloop()