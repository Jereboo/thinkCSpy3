"""
Whack a mole game- based on ThinkCSpy3 lesson 14.31 (not my original work)
"""

import tkinter as tk
from tkinter import ttk

class WhackAMole:
	
	def __init__(self):
		self.window = tk.Tk()
		self.mole_frame, self.status_frame = self.create_frames()
	
	def create_frames(self):
		mole_frame = tk.Frame(self.window, bg='red', width=300, height=300)
		mole_frame.grid(row=1, column=1)
		
		status_frame= tk.Frame(self.window, bg='green', width=100, height=300)
		status_frame.grid(row=1, column=2)
		
		return mole_frame, status_frame
		
#Creates the GUI Program
program = WhackAMole()

#Start the GUI event loop
program.window.mainloop()