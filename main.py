from DataUtilities import FitsReader

filename = "jw02739-o001_t001_nircam_clear-f187n_segm.fits"
fits_data = FitsReader(filename)
fits_data.load_image_data_from_extension(1)
print(fits_data.image_data)

FitsReader.print_without_compression(fits_data.image_data[1:100,1:100])
print(fits_data.image_data)
