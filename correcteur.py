from tkinter import *
import os


import nltk

from win10toast import ToastNotifier



from pynput.keyboard import Key, Listener , KeyCode
import sys
f = open("liste_francais.txt", "r")
liste = f.read().splitlines()

arguments = len(sys.argv) - 1
position = 1
while (arguments >= position):
    if sys.argv[position] == "--add":
    	f = open("liste_francais.txt", "a+")
    	if sys.argv[position+1] in liste:
    		print("mot deja connu")
    	else:
    		f.write('\n{}'.format(sys.argv[position+1]))
    		print("le mot {} a ete ajouté avec succes !".format(sys.argv[position+1]))
    	f.close()
    if sys.argv[position] == "--help":
    	print("use \"python3 correcteur.py -- add <word>\" for add word in wordlist")
    position = position + 1

while True:

	user_word = []
	
	
	bon_mot = []

	

	def on_release(key):
		current = set()
		global user_word
		if key == Key.space:
			return False
		try:
			user_word+=key.char
		except:
			pass
	# Collect events until released
	with Listener(
	        on_release=on_release) as listener:
	    listener.join()


	# To check if any notifications are active,
	# use `toaster.notification_active()`
	for element in liste:
		a = nltk.edit_distance(element, user_word)

		if a<2:
			bon_mot.append(element)
		if a == 0:
			bon_mot=[]
			break


	# One-time initialization
	toaster = ToastNotifier()

	# Show notification whenever needed
	try:
		toaster.show_toast("Voulez vous dire \"{}\" ?".format(bon_mot[0]), "correcteur orthographique", threaded=True,icon_path=None, duration=3)  # 3 seconds
	except:
		pass