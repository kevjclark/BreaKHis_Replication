from skimage import feature
from skimage import io
import numpy as np

class LBPGeneration:
	def __init__(self, p, r):
		#Sets number of points and radious for running of the LBP Algorithm, as provided in scikit-image (skimage)
		self.points = p
		self.radius = r

	def start(self, filelist, iter=-1, path):
		if iter < 0:
			for f in filelist:
				image = np.imread((path + filelist), as_grey=True )

		