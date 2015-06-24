
#Each mood has two parts, high and low
#The value determines which side the mood is on
class wereMood:
	def __init__(self,low,high,value):
		self.high = high
		self.low = low
		self.value = value
	def __str__(self):
		if(self.value > 0):
			return self.high
		else:
			return self.low
	def absolute(self):
		if(self.value < 0):
			return self.value*-1
		else:
			return self.value
#To compare to see which mood takes president
	def moodWin(self,mood):
		if (self.absolute() < mood.absolute()):
			return mood
		else:
			return self

class wereMoods:
	def __init__(self):
		#Moods acts like a 1based list
		self.moods = {}
		#This is to match mood lookup
		#It a positive and a negative at each index
		#And, thus, can't be zero based
		self.moodLookup = {}
		#mood names and default values
		#move this into the were class
	#sets the index of the mood name in mood lookup
	#will sets it to be negative on the low ends
	def addMood(self,low,high,value):
		#it ac
		index = 1+len(self.moods)
		self.moodLookup[high] = (index)
		self.moodLookup[low] =  -(index)
		self.moods[index] = wereMood(low,high,value)
	def changeMood(self,moodName,adjustment=1):
		i = self.moodLookup[moodName]
		if(i < 0):
			i *= -1
			adjustment *= -1
		self.moods[i].value += adjustment
		return moodName + " " + str(i) + " " + str(adjustment)
	def __str__(self):
		return self.getMood().__str__();
	#Searches moods recursivly, starting at index 1
	def getMood(self,index = 1):
		if(index == len(self.moods)):
			return self.moods[index]
		else:
			cmood = self.moods[index]
			nmood = self.getMood(index+1)
			return cmood.moodWin(nmood)
	def __getitem__(self,index):
		for mood in self.moodLookup.keys():
			if mood == index:
				key = self.moodLookup[mood]
				if(key < 0):
					key *= -1
				return self.moods[key].value