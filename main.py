from DataUtilities import FitsReader
from VisualUtilities import mplPlotter

filename = "jw02739-o001_t001_nircam_clear-f187n_segm.fits"
fits_data = FitsReader(filename)
fits_data.load_image_data_from_extension(1)

mpl = mplPlotter(fits_data.image_data)
mpl.plot_2d(display_plot = False)
mpl.plot_3d()
