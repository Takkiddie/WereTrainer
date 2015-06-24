from display import *
import os

class FileDisplay:
	def __call__(self,file):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		rel_path = os.path.join("dialog",file)
		path = os.path.join(script_dir, rel_path)
		file = open(path,"r")
		lines = file.readlines()
		for line in lines:
			disp(line)
fileLoad = FileDisplay()

