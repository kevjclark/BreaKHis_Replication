from skimage import feature
from skimage import io
import numpy as np

class LBPGeneration:
	def __init__(self, p, r):
		#Sets number of points and radious for running of the LBP Algorithm, as provided in scikit-image (skimage)
		self.points = p
		self.radius = r
		self.bins = np.arange(0, p+2)
		self.range = range(0, p+1)

	def start(self, filelist, iter=-1, path):
		if iter < 0:
			for f in filelist:
				image = np.imread((path + filelist), as_grey=True )
				lbp = feature.local_binary_pattern(image, self.numPoints,self.radius, method="ror")
				lbp = lbp.ravel()
				(imhist, _) = np.histogram(lbp, self.bins, self.range, density = True)


		