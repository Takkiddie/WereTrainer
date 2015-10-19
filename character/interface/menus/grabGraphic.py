import sys, pygame, os
def grabG(file):
	ret = "";
	try:
		imagePath = os.path.join('assets', 'graphics',file);	
		ret = pygame.image.load(imagePath);
	except:
		imagePath = os.path.join('assets', 'graphics',"error.png");	
		ret = pygame.image.load(imagePath);		
	return ret;
