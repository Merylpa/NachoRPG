import pickle
import os
# Create a save file
# New game / Continue menu
# Continue looks for existing save files

def find_saves():
	saves = []
	for filename in os.listdir():
		if filename.endswith(".save"):
			saves.append(filename)
	return saves

def create_save(data, filename):
	with open(filename, "wb") as savefile_out:
		pickle.dump(data,savefile_out)

def load_save(save_file):
	with open(save_file, "rb") as savefile_in:
		return pickle.load(savefile_in)

find_saves()
