import createfilelist as cfl
import LBPGeneration.py as lbp
from skimage import io
import matplotlib.pyplot as plt
from skimage import color


#Change this for running on your local machine
impath = '/home/taim/Documents/testImages'
imFilepath = '/home/taim/Documents/Honors/HonorsResults/imagefiles.txt'
featurePath = '/home/taim/Documents/Honors/HonorsResults/'

#these do not need to be changed per machine
lbpFeaturePath = featurePath + 'lbpFeat.txt'
cfl.createflist(impath, imFilepath)
imlist= []
with open(imFilepath) as f:
	for line in f:
		filepath = impath + '/' + line
		filepath = filepath[0:len(filepath)]
		filepath = filepath.replace('\n', '')
		imlist.append(filepath)

lbpgen = lbp(8,2)
print('complete')