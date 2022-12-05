from DataUtilities import FitsReader, ImageProcessor
from VisualUtilities import mplPlotter, cv2Helpmate
import numpy as np

filename = "jw02739-o001_t001_nircam_clear-f187n_segm.fits"
fits_data = FitsReader(filename) 
fits_data.load_image_data_from_extension(1)

# mpl = mplPlotter(fits_data.image_data)
# mpl.plot_2d()
# mpl.plot_3d()

k = np.array([
    [ -1., -1., -1., -1., -1.],
    [ -1.,  1.,  1.,  1., -1.],
    [ -1.,  1.,  4.,  1., -1.],
    [ -1.,  1.,  1.,  1., -1.],
    [ -1., -1., -1., -1., -1.]])


cvim = cv2Helpmate(fits_data.image_data)
cvim.rescale(0.05)
cv2Helpmate.save(cvim.data, "Saved Images/t1-raw.png")
convoluted_data = ImageProcessor.convolve(cvim.data, k)

cv2Helpmate.save(convoluted_data, "Saved Images/t1.png")

image_segment = cv2Helpmate.rescale(fits_data.image_data[-1000:-1,-1000:-1], 0.5)
cv2Helpmate.save(ImageProcessor.convolve(image_segment, k), "Saved Images/t2.png")
