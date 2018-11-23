
#---------------------------------------
# 3D Jupyter
import numpy as np
import k3d

def visualization_inter3D_xyz(pa):
    
    if (pa.shape[1]==4):
        pa = np.delete(pa, (3), axis=1)
    plot = k3d.plot()
    print(pa.shape[0])
    points_number = pa.shape[0]
    colors = np.random.randint(0, 0xFFFFFF, points_number)

    points = k3d.points(pa, colors, point_size=0.01, shader='3d')
    plot += points
    plot.camera_auto_fit = False
    plot.display()
    print("(x) : {:2.1f}m".format(pa[:,0:1].max() - pa[:,0:1].min()))
    print("(y) : {:2.1f}m".format(pa[:,1:2].max() - pa[:,1:2].min()))
    print("(z) : {:2.1f}m".format(pa[:,2:3].max() - pa[:,2:3].min()))
    #print("mean(z) : {:2.1f}m".format(numpy.mean(pa[:,2:3])))


#---------------------------------------------------------------------------
# 2D Jupyter 

import matplotlib.pyplot as plt
#import pypcd



def visualization2D_xyz(new_cloud_data):
    # set the size of pyplot charts
    plt.rcParams['figure.figsize'] = (14, 6)

    # split the rgb column into three columns: red, green and blue
    rgb_columns = np.asarray(random_color_gen())
    
    # normalize the rgb values (they should be between [0, 1])
    rgb_columns = (rgb_columns / 255.0).astype(np.float)

    # plot the points of the columns
    plt.scatter(new_cloud_data[:, [0]], -new_cloud_data[:, [1]], color=rgb_columns)

    # scale the axis equally 
    # (Note: append a semicolon to your last line to prevent jupyter notebook 
    # from outputting your last cell's content)
    plt.axis('scaled');
    print("(x) : {:2.1f}m".format(new_cloud_data[:,0:1].max() - new_cloud_data[:,0:1].min()))
    print("(y) : {:2.1f}m".format(new_cloud_data[:,1:2].max() - new_cloud_data[:,1:2].min()))
    print("(z) : {:2.1f}m".format(new_cloud_data[:,2:3].max() - new_cloud_data[:,2:3].min()))


# 3D Jupyter

from mpl_toolkits.mplot3d import Axes3D

# Create a figure with a subplot with three axes

def visualization3D_xyz(new_cloud_data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # split the rgb column into three columns: red, green and blue
    rgb_columns = np.asarray(random_color_gen())
    
    # normalize the rgb values (they should be between [0, 1])
    rgb_columns = (rgb_columns / 255.0).astype(np.float)

    ax.scatter(new_cloud_data[:,0], new_cloud_data[:,1], new_cloud_data[:,2], color=rgb_columns);
    print("(x) : {:2.1f}m".format(new_cloud_data[:,0:1].max() - new_cloud_data[:,0:1].min()))
    print("(y) : {:2.1f}m".format(new_cloud_data[:,1:2].max() - new_cloud_data[:,1:2].min()))
    print("(z) : {:2.1f}m".format(new_cloud_data[:,2:3].max() - new_cloud_data[:,2:3].min()))



#----------------------------------------------------------


from random import randint
import struct
import ctypes

def random_color_gen():
    """ Generates a random color
    
        Args: None
        
        Returns: 
            list: 3 elements, R, G, and B
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return [r, g, b]

def rgb_to_float(color):
    """ Converts an RGB list to the packed float format used by PCL
    
        From the PCL docs:
        "Due to historical reasons (PCL was first developed as a ROS package),
         the RGB information is packed into an integer and casted to a float"
    
        Args:
            color (list): 3-element list of integers [0-255,0-255,0-255]
            
        Returns:
            float_rgb: RGB value packed as a float
    """
    hex_r = (0xff & color[0]) << 16
    hex_g = (0xff & color[1]) << 8
    hex_b = (0xff & color[2])

    hex_rgb = hex_r | hex_g | hex_b

    float_rgb = struct.unpack('f', struct.pack('i', hex_rgb))[0]

    return float_rgb


def float_to_rgb(float_rgb):
    """ Converts a packed float RGB format to an RGB list    
        
        Args:
            float_rgb: RGB value packed as a float
            
        Returns:
            color (list): 3-element list of integers [0-255,0-255,0-255]
    """
    s = struct.pack('>f', float_rgb)
    i = struct.unpack('>l', s)[0]
    pack = ctypes.c_uint32(i).value
			
    r = (pack & 0x00FF0000) >> 16
    g = (pack & 0x0000FF00) >> 8
    b = (pack & 0x000000FF)
			
    color = [r,g,b]
			
    return color