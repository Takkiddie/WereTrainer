from display import *
import os

#Grabs and reads "story files" line by line
#It also changes portrates on command.
class FileDisplay:
	def __call__(self,file):
		script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
		rel_path = os.path.join("dialog",file)
		path = os.path.join("assets", rel_path)
		file = open(path,"r")
		lines = file.readlines()
		for line in lines:
			if(line[0:3] == "(p)"):
				picName = line[3:].strip();
				disp.dispPortrate = picName
				#disp.dispPortrate = "happy.png"
			else:
				disp(line)
fileLoad = FileDisplay()

