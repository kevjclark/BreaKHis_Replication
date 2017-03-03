from skimage import feature
from skimage import io
import numpy as np

class LBPGeneration:
	def __init__(self, p, r):
		#Sets number of points and radious for running of the LBP Algorithm, as provided in scikit-image (skimage)
		self.points = p
		self.radius = r
		self.bins = 256 #Grey scale intensity
		self.range = range(0, 255)

	def start(self, filelist, path, iter=-1 ):
		resultFile = open(path, 'w')
		if iter < 0:
			for f in filelist:
				image = io.imread(f, as_grey=True )
				lbp = feature.local_binary_pattern(image, self.numPoints,self.radius, method="ror")
				lbp = lbp.ravel()
				(imhist, _) = np.histogram(lbp, self.bins, self.range, density = True)
				for i in self.range:
					resultFile.write(imhist[i] + " ")
				resultFile.write('\n')

		resultFile.close()



		