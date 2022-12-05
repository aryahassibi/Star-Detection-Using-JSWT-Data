import numpy as np
from astropy.visualization import simple_norm, astropy_mpl_style
import matplotlib.pyplot as plt
import cv2

# A class to facilitate plotting graphs using matplotlib
class mplPlotter:
    def __init__(self, data = np.array([])):
        plt.style.use(astropy_mpl_style)
        self.data = data
        self.default_path = "Saved Images/"

        self.plot_2d = self._instance_plot_2d
        self.plot_3d = self._instance_plot_3d
    
    # Void static fucntion - takes the data as a 2d array and displayes/saves it in matplotlib
    @staticmethod
    def plot_2d(data, filter = "jet", title = "2d Plot", display_plot = True, show_color_bar = True, save_plot_as_image = True, file_path = "Saved Images/Untitled_2d.png",):
        if(data.ndim == 2 and data.size !=0):
            plt.title(title)
            # plt.imshow(data, cmap = filter, norm = simple_norm(data, 'sqrt'))
            plt.imshow(data, cmap = filter)
            if show_color_bar:
                plt.colorbar()

            if display_plot:
                plt.show()
            
            if save_plot_as_image:
                plt.savefig(file_path)
            
            plt.close()
        else:
            print(f"Error: Number of dimensions of the the data should be 2. the # of dimentions of the given data is {data.ndim} and the size of it is {data.size}.")
    
    # Void fucntion - diplays/saves the data that the class was initilized with
    # same funcitnallity as plot_2d() 
    def _instance_plot_2d(self, filter = "jet", title = "2d Plot", display_plot = True, show_color_bar = True, save_plot_as_image = True, file_name = "Untitled_2d.png"):
        if(self.data.ndim == 2 and self.data.size != 0):

            plt.title(title)
            plt.imshow(self.data, cmap = filter)
            
            if show_color_bar:
                plt.colorbar()

            if display_plot:
                plt.show()

            if save_plot_as_image:
                plt.savefig(self.default_path + file_name)

            plt.close()
        else:
            print(f"Error: Number of dimensions of the the data should be 2. the # of dimentions of the given data is {self.data.ndim} and the size of it is {self.data.size}.")

    # Void static function - turns the given 2d data into a 3d chart
    # if the plot_plane value is set to True it will draws a plane based on the plane_value
    @staticmethod
    def plot_3d(data, plot_plane = False, plane_values = np.array([]), filter = "jet", title = "3d Plot", display_plot = True, show_color_bar = True, save_plot_as_image = True, file_path = "Saved Images/Untitled_2d.png"):
        if(data.ndim == 2 and data.size != 0):
            data_height, data_width = data.shape
            X, Y = np.meshgrid(range(data_width), range(data_height))
            Z = data
            plt3d = plt.figure().add_subplot(111, projection = '3d')
            plt.title(title)
            plt3d.plot_surface(X, Y, Z, cmap = filter)

            if (plot_plane):
                if (plane_values.size != 0 and plane_values.shape == data.shape):
                    planeX, planeY = X, Y
                    plt3d.plot_surface(planeX, planeY, plane_values, alpha=0.25, color = 'black')
                else:
                    print("Error: The given plane_values are not correct")

            if save_plot_as_image:
                plt.savefig(file_path)

            if display_plot:
                plt.show()

            plt.close()

        else:
            print(f"Error: Number of dimensions of the the data should be 2. the # of dimentions of the given data is {data.ndim} and the size of it is {data.size}.")
    
    # Void function - turns the 2d data of the class into a 3d chart
    # same functionality as plot_3d()
    def _instance_plot_3d(self, plot_plane = False, plane_values = np.array([]), filter = "jet", title = "3d Plot", display_plot = True, show_color_bar = True, save_plot_as_image = True, file_name = "Untitled_3d.png"):
        if(self.data.ndim == 2 and self.data.size !=0):
            data_height, data_width = list(self.data.shape)
            X, Y = np.meshgrid(range(data_width), range(data_height))
            Z = self.data
            plt3d = plt.figure().add_subplot(111, projection = '3d')
            plt.title(title)
            plt3d.plot_surface(X, Y, Z, cmap = filter)

            if (plot_plane):
                if (plane_values.size != 0 and plane_values.shape == self.data.shape):
                    planeX, planeY = X, Y
                    plt3d.plot_surface(planeX, planeY, plane_values, alpha=0.25, color = 'black')
                else:
                    print("Error: The given plane_values are not correct")
            
            if save_plot_as_image:
                plt.savefig(self.default_path + file_name)

            if display_plot:
                plt.show()

            plt.close()

        else:
            print(f"Error: Number of dimensions of the the data should be 2. the # of dimentions of the given data is {self.data.ndim} and the size of it is {self.data.size}.")
    
# A class to facilitate displaying/saving/modifying data as images using cv2
class cv2Helpmate:
    def __init__(self, data = np.array([])):
        self.data = data

        # values in data are mapped to values in range 0,255
        self.mapped_data = ((self.data - np.min(self.data)) * (1 / (np.max(self.data) - np.min(self.data)) * 255)).astype('uint8')

        self.image = np.stack((self.mapped_data,) * 3, axis=-1)
        self.save = self._instance_save
        self.rescale = self._instance_rescale
    
    # opens the image based on the given path
    def open(self, image_path):
        self.data = cv2.imread(image_path)

    # Void function - Displays the given 2d data as an B&W image 
    def plot(self, window_title = "Untitled", close_window_after = 10):
        cv2.imshow(window_title, self.image)
        cv2.waitKey(close_window_after * 1000)

    # void fucntion - saves the self.data as png image.
    def _instance_save(self, file_path = "Saved Images/Untitled_cv2Image.png"):
        cv2.imwrite(file_path, self.image)
    
    # static void fucntion - saves the data as png image.
    
    def save(data, file_path = "Saved Images/Untitled_cv2Image.png"):
        mapped_data = ((data - np.min(data)) * (1 / (np.max(data) - np.min(data)) * 255)).astype('uint8')
        cv2.imwrite(file_path, data)

    # void fucntion - rescales the data that class was initilized with
    def _instance_rescale(self, scale):
        image_height, image_width = self.data.shape
        rescaled_height, rescaled_width = int(image_height * scale), int(image_width * scale)

        rescaled_image = cv2.resize(self.mapped_data, dsize = (rescaled_width, rescaled_height), interpolation = cv2.INTER_CUBIC)
        self.data = rescaled_image
        self.image = np.stack((self.data,)*3, axis=-1)
    
    # static void fucntion - rescales the given data
    @staticmethod
    def rescale(data, scale):
        image_height, image_width = data.shape
        rescaled_height, rescaled_width = int(image_height * scale), int(image_width * scale)

        mapped_data = ((data - np.min(data)) * (1 / (np.max(data) - np.min(data)) * 255)).astype('uint8')

        rescaled_image = cv2.resize(mapped_data, dsize = (rescaled_width, rescaled_height), interpolation = cv2.INTER_CUBIC)
        return rescaled_image
