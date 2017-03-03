import createfilelist as cfl
from skimage import io
import matplotlib.pyplot as plt
from skimage import color


#Change this for running on your local machine
impath = '/home/taim/Documents/testImages'
imFilepath = '/home/taim/Documents/Honors/HonorsResults/imagefiles.txt'
cfl.createflist(impath, imFilepath)
imlist= []
with open(imFilepath) as f:
	for line in f:
		filepath = impath + '/' + line
		filepath = filepath[0:len(filepath)]
		filepath = filepath.replace('\n', '')
		imlist.append(filepath)

	
print('complete')