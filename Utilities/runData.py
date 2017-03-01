import createfilelist as cfl
from skimage import io

#Change this for running on your local machine
impath = '/home/taim/Documents/testImageV'
imFilepath = '/home/taim/Documents/Honors/HonorsResults/imagefiles.txt'
cfl.createflist(impath, imFilepath)
imlist= []
with open(imFilepath) as f:
	for line in f:
		filepath = impath + line
		filepath = filepath.remove('\n')
		imlist.append(filepath)

#for testing only
imtest = io.imread(imlist[0], as_grey=True )
print(imtest)
	
print('complete')