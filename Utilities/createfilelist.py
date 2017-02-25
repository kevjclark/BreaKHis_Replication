#This method takes a given file path (pathF) and stores a text list of all of those files in the location specified in (pathT)
#This allows for easily consistant ordering, and easier start/resume operations with the feature vectors

from os import listdir as listdirec

def createfilelist(pathF, pathT):
	file_list = listdirec(pathF)
	filesFile = open(pathT, w)
	for f in file_list:
		filesFile.write(f)
	filesFile.close()

createfilelist('/home/taim/Documents/testImagesV', '/home/taim/Documents/Honors/HonorsResults')