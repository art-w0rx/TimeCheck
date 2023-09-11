from tkinter import PhotoImage, Tk, Label
import os
import time
import pystray
from PIL import Image, ImageTk
import sys
import datetime

icon_logo = '../img/icon.png'
img_bg = '../img/bg.png'
start_time = datetime.datetime.now()
target_time = 0
bg = '#C0C0C0'

def window_configure():
	global window, photo_wall
	window = Tk()
	icon_win = PhotoImage(file=icon_logo)
	photo_wall = PhotoImage(file=img_bg)
	wide = window.winfo_screenwidth()
	high = window.winfo_screenheight()
	w = wide - 420
	h = high - 520
	window.attributes("-topmost", True)
	window.title("TimeCheck")
	window.attributes("-topmost", True)
	window.geometry(f"412x224+{w}+{h}")
	window.resizable(False, False)
	window.configure(bg=bg)
	window.iconphoto(True, icon_win)
	label = Label(window, image=photo_wall)
	label.pack(fill="both", expand=True)

def start_window():
	window_configure()
	window.update()
	time.sleep(1.5)
	try:
		window.destroy()
	except:
		update()
	update()

def update():
	while True:
		global check_exit, target_time
		elapsed_time = datetime.datetime.now() - start_time
		target_time = elapsed_time.total_seconds()
		if check_exit == 1:
			sys.exit()
		if target_time >= 3600:
			start_window()
		time.sleep(1)

def tray():
	global check_exit
	check_exit = 0
	image = Image.open(icon_logo)
	def on_click(icon, item):
		global check_exit
		check_exit = 1
		icon.stop()
	def ok_click(icon, item):
		global target_time, start_time
		if target_time >= 3600:
			start_time = datetime.datetime.now()
	icon = pystray.Icon("TimeCheck", image, menu = pystray.Menu(pystray.MenuItem("Я понял!", ok_click), pystray.MenuItem("Выйти", on_click)))
	def run(icon):
		icon.visible = True
		update()
	icon.run(run)

tray()
