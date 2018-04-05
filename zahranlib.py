import cv2
import numpy as np
import math
import subprocess
import time

def getBlob(image):
	return cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))

def processNetForward(preds,n=5):             # n is the the no of of top predictions to be considered. preds is the output of net.forward()
	idxs = np.argsort(preds[0])[::-1][:n]
	return idxs

def checkifjpeg(fp):
	file = open(fp,'rb')
	bytevals = file.read()
	hexvals = bytevals.hex()
	if(hexvals[:6] == 'ffd8ff'):
		return False
	else:
		return True

def xy_diff(xy1,xy2):
	xdiff = xy1[0] - xy2[0]  # Gets the difference between the x coordinates
	ydiff = xy1[1] - xy2[1]  # Same for the y coordinates.
	diff = math.sqrt(xdiff*xdiff+ydiff*ydiff) # The logic behind this is pretty simple, consider two xy coords, using them you can form a right angled triangle,
	return diff  # Where the difference between the x coords form one side, and the distance between the y coords, the other. Therefore using the Pythogoras theorem, you can find the third side.

def CaseInsensitiveRegex(string,regex):       # Self explanatory, it seraches for a string in another string, disregarding case
	try:
		for i in range(len(string)):
				for l in range(len(regex)):
					if(string[i+l] == regex[l].lower() or string[i+l] == regex[l].upper()):
						if(l == len(regex)-1):
							return True
					else:
						return False
	except Exception:
		pass
	pass

def grabfrominsta(url):
	if("?taken-by" in url):
		url = url.split("?")
		url = url[0]
	html = request.urlopen(url)
	html = html.read()
	html = str(html)[2:-1]
	line = html.split("<")
	for i in line:
		if('meta property="og:image"' in i):
			upurl = i
	upurl = upurl.split('"')
	upurl = upurl[3]
	return upurl

def getTerminalOutput(cmd=["test"]):
	output = subprocess.Popen(params, stdout=subprocess.PIPE ).communicate()[0].replace("\x03","\n")  #the "\xo3" part is there since this program was originally for IRC
	return("output")

class Timer(object):
	"""This creades a periodic timer object. every time interval in seconds is reached , function will be executed"""
	def __init__(self, every,function):
		super(Timer, self).__init__()
		self.every = every
		self.last = time.time()
		self.function = function
	def update(self):
		if(time.time() - self.last >= self.every):
			self.function()
			self.last = time.time()



