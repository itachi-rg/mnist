import numpy as np
import cv2

from os import listdir, makedirs
from os.path import join,isfile,exists
from shutil import rmtree

from time import sleep

def createImages() :
	narray = np.genfromtxt("train.csv", delimiter=",")
	
	parent_path = 'resources'
	training_set_path = 'training_set_images'
	
	if exists(join(parent_path,training_set_path)) :
		rmtree(join(parent_path,training_set_path))
		
	sleep(2)
	makedirs(join(parent_path,training_set_path))
	
	label, pixelArray = np.split(narray,[1], axis=1)
	
	for i in range(1,len(narray)) :
		char = str(int(label[i][0]))
		char_path = join(parent_path, training_set_path, char)
		if not exists(char_path) :
			makedirs(char_path)
			
		existingfiles = [f for f in listdir(char_path) if isfile(join(char_path,f))]
		
		imgfile = str(len(existingfiles)) + ".png"
		imgname = join(char_path,imgfile)
		
		img = np.reshape(pixelArray[i], (28,28))
		cv2.imwrite(imgname, img);
	
if __name__ == "__main__" :
	createImages()