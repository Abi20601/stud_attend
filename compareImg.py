# USAGE
# python compare.py

# import the necessary packages
#from skimage.measure import structural_similarity as ssim
from skimage.measure import compare_ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
import sys

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	#s = ssim(imageA, imageB)
	s = compare_ssim(imageA, imageB)
	return s*100
	'''
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	# plt.show()
	'''

# load the images -- the original, the original + contrast,
# and the original + photoshop
#img1 = cv2.imread(sys.argv[1])
#img2 = cv2.imread(sys.argv[2])

img1 = cv2.imread(sys.argv[1])
img2 = cv2.imread(sys.argv[2])
# convert the images to grayscale
image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("Original", image1), ("Contrast", image2)

# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	#plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
#plt.show()

# compare the images

Similarity  = compare_images(image1, image2, "Comparaison Between Images")

print Similarity
