from skimage import feature
from skimage import io
import numpy as np

class LBPGeneration:
	def __init__(self, p, r):
		#Sets number of points and radious for running of the LBP Algorithm, as provided in scikit-image (skimage)
		self.points = p
		self.radius = r
		self.bins = np.arange(0,257) #Grey scale intensity
		self.range = (0, 255)

	def start(self, filelist, path, iter=-1, label = '', append=False ):

		if iter < 0:
			if append == False:
				resultFile = open(path, 'w')
				for f in filelist:
					print(f)
					image = io.imread(f, as_grey=True )
					lbp = feature.local_binary_pattern(image, self.points,self.radius, method="ror")
					lbp = np.ravel(lbp)
					(imhist, hold ) = np.histogram(np.asarray(lbp), self.bins, self.range, density = True)
					for i in range(0,256):
						resultFile.write(str(imhist[i]) + " ")
					resultFile.write(label)
					resultFile.write('\n')
			else:
				resultFile = open(path, 'a')
				for f in filelist:
					print(f)
					image = io.imread(f, as_grey=True )
					lbp = feature.local_binary_pattern(image, self.points,self.radius, method="ror")
					lbp = np.ravel(lbp)
					(imhist, hold ) = np.histogram(np.asarray(lbp), self.bins, self.range, density = True)
					for i in range(0,256):
						resultFile.write(str(imhist[i]) + " ")
					resultFile.write(label)
					resultFile.write('\n')
		else:
			count =0
			if append == False:
				resultFile = open(path, 'w')
				for f in filelist:
					if count <iter:
						count +=1
						print(f)
						image = io.imread(f, as_grey=True )
						lbp = feature.local_binary_pattern(image, self.points,self.radius, method="ror")
						lbp = np.ravel(lbp)
						(imhist, hold ) = np.histogram(np.asarray(lbp), self.bins, self.range, density = True)
						for i in range(0,256):
							resultFile.write(str(imhist[i]) + " ")
						resultFile.write(label)
						resultFile.write('\n')
					else:
						break
			else:
				resultFile = open(path, 'a')
				for f in filelist:
					if count <iter:
						count +=1
						print(f)
						image = io.imread(f, as_grey=True )
						lbp = feature.local_binary_pattern(image, self.points,self.radius, method="ror")
						lbp = np.ravel(lbp)
						(imhist, hold ) = np.histogram(np.asarray(lbp), self.bins, self.range, density = True)
						for i in range(0,256):
							resultFile.write(str(imhist[i]) + " ")
						resultFile.write(label)
						resultFile.write('\n')
					else:
						break



		resultFile.close()



		