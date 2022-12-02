import numpy as np
from astropy.io import fits
from astropy.utils.data import download_file

class FitsReader:
    def __init__(self, file_location, local = True):
        # if the file is not stored locally the data will be fetched from the given url.
        if(not local):
            file_location = download_file(file_location, cache=True)
        self.file_location = file_location
        # Header Data Unit List
        self.hdul = fits.open(file_location)

    # void - prints out the general information about the file headers
    def print_general_file_info(self):
        self.hdul.info()
    
    # void - prints out the information in the specified header
    def print_header_info_from_extension(self, header_extention_index):
        print(self.hdul[header_extention_index].header)
    
    # void - loads the images data from the specified header and stores it in a self.image_data
    # the size of the images is stored as well
    def load_image_data_from_extension(self, header_extention_index):
        self.image_data = fits.getdata(self.file_location, ext = header_extention_index)
        self.image_size = self.image_data.shape
        self.image_rows, self.image_columns = self.image_size
    
    # returns the value of the keywrod stored in the specidfied header extention 
    def get_keyword_value_from_extension(self, header_extention_index, keyword):
        header_keywords = self.hdul[header_extention_index].header
        if (keyword in header_keywords):
            return header_keywords[keyword]
        else:
            print(f"Error: The given Keyword [{keyword}], does not exist in the header extention index {header_extention_index}.")
    
    # takes a function and returns the image data mapped with the given function
    def map_func_to_image_data(self, func):
        vfunc = np.vectorize(func)
        return vfunc(self.image_data)
    
    # A statis func that prints the data given to the function witouth comppression
    # e.g. [ 0 0 ... 0 0 ] will be printed as [ 0 0 0 0 0 0 0 0 0 0 0 0 ]
    @staticmethod
    def print_without_compression(data):
        import sys
        np.set_printoptions(threshold = sys.maxsize)

        print(data)

        # setting back the treshold to default value
        np.set_printoptions(threshold = 1000)
         


