import numpy as np
from astropy.visualization import simple_norm, astropy_mpl_style
import matplotlib.pyplot as plt

class mplPlotter:
    def __init__(self, data = np.array([])):
        plt.style.use(astropy_mpl_style)
        self.data = data

        self.plot_2d = self._instance_plot_2d
        self.plot_3d = self._instance_plot_3d
    
    # Void static fucntion - takes the data as a 2d array and displayes/saves it in matplotlib
    @staticmethod
    def plot_2d(data, filter = "jet", title = "2d Plot", display_plot = True, save_plot_as_image = True, file_name = "Saved Charts/Untitled_2d.png"):
        if(data.ndim == 2 and data.size !=0):
            plt.title(title)
            # plt.imshow(data, cmap = filter, norm = simple_norm(data, 'sqrt'))
            plt.imshow(data, cmap = filter)

            if display_plot:
                plt.show()
            
            if save_plot_as_image:
                plt.savefig(file_name)
            
            plt.close()
        else:
            print(f"Error: Number of dimensions of the the data should be 2. the # of dimentions of the given data is {data.ndim} and the size of it is {data.size}.")
    
    # Void fucntion - diplays/saves the data that the class was initilized with
    # same funcitnallity as plot_2d() 
    def _instance_plot_2d(self, filter = "jet", title = "2d Plot", display_plot = True, save_plot_as_image = True, file_name = "Saved Charts/Untitled_2d.png"):
        if(self.data.ndim == 2 and self.data.size != 0):

            plt.title(title)
            plt.imshow(self.data, cmap = filter)

            if display_plot:
                plt.show()

            if save_plot_as_image:
                plt.savefig(file_name)

            plt.close()
        else:
            print(f"Error: Number of dimensions of the the data should be 2. the # of dimentions of the given data is {self.data.ndim} and the size of it is {self.data.size}.")

    # Void static function - turns the given 2d data into a 3d chart
    # if the plot_plane value is set to True it will draws a plane based on the plane_value
    @staticmethod
    def plot_3d(data, plot_plane = False, plane_values = np.array([]), filter = "jet", title = "3d Plot", display_plot = True, save_plot_as_image = True, file_name = "Saved Charts/Untitled_23.png"):
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
                plt.savefig(file_name)

            if display_plot:
                plt.show()

            plt.close()

        else:
            print(f"Error: Number of dimensions of the the data should be 2. the # of dimentions of the given data is {data.ndim} and the size of it is {data.size}.")
    
    # Void function - turns the 2d data of the class into a 3d chart
    # same functionality as plot_3d()
    def _instance_plot_3d(self, plot_plane = False, plane_values = np.array([]), filter = "jet", title = "3d Plot", display_plot = True, save_plot_as_image = True, file_name = "Saved Charts/Untitled_3d.png"):
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
                plt.savefig(file_name)

            if display_plot:
                plt.show()

            plt.close()

        else:
            print(f"Error: Number of dimensions of the the data should be 2. the # of dimentions of the given data is {self.data.ndim} and the size of it is {self.data.size}.")
    
