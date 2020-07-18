import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import scipy.ndimage as scimg
from rpi_init import *
from scipy.spatial import distance
import statistics

def RPI_cam():
    from picamera import PiCamera
    # picamera setup
    h = 640 #largest resolution length
    cam_res = (int(h),int(0.75*h)) # resizing to picamera's required ratios
    cam_res = (int(32*np.floor(cam_res[0]/32)),int(16*np.floor(cam_res[1]/16)))
    cam = PiCamera(resolution=cam_res)
    # preallocating image variables
    data = np.empty((cam_res[1],cam_res[0],3),dtype=np.uint8)
    x,y = np.meshgrid(np.arange(cam_res[0]),np.arange(cam_res[1]))

    # different edge detection methods
    cam.capture(data,'rgb') # capture image
    return data


def load_image(image_file, issave):
    image = plt.imread(image_file)
    fig, ax = plt.subplots()
    ax.imshow(image)
    ax.vlines([x0, x1 ], y0, y1,  colors='r')
    ax.hlines([y0, y1 ], x0, x1,  colors='r')
    if issave:
        plt.savefig(image_file.split('.')[0]+'_b.png')
    else:            
        plt.show()
    return image


def findedges(image, image_file, issave):
    data = image[y0:y1 , x0:x1, :]
    x,y = np.meshgrid(np.arange(data.shape[1]),np.arange(data.shape[0]))
    gaus = scimg.fourier_gaussian(data[:,:,0],sigma=0.01)
    can_x = scimg.prewitt(gaus,axis=0)
    can_y = scimg.prewitt(gaus,axis=1)
    can = np.hypot(can_x,can_y)
    # pulling out object edges
    fig3,ax3 = plt.subplots(2,1,figsize=(10,7))
    ax3[0].pcolormesh(x,y,can,cmap='gist_ncar')
    bin_size = 30 # total bins to show
    percent_cutoff = 0.05 # cutoff once main peak tapers to 5% of max
    hist_vec = np.histogram(can.ravel(),bins=bin_size)    
    hist_x,hist_y = hist_vec[0],hist_vec[1]
    for ii in range(np.argmax(hist_x),bin_size):
        hist_max = hist_y[ii]
        if hist_x[ii]<percent_cutoff*np.max(hist_x):
            break        
    # scatter points where objects exist
    ax3[1].plot(x[can>hist_max],y[can>hist_max],marker='.',linestyle='',
                label='Scatter Above 5% Dropoff')
    ax3[1].set_xlim(np.min(x),np.max(x))
    ax3[1].set_ylim(np.min(y),np.max(y))
    ax3[1].legend()
    if issave:
        plt.savefig(image_file.split('.')[0]+'_edges.png')
    else:            
        plt.show()
    print(hist_vec[1])    
    return stat_dsp(hist_vec[1],threshold)    
    

def stat_dsp(current, threshold):    
    d = distance.euclidean(current, threshold)
    print("Euclidean distance: ",d)
    std = statistics.stdev([abs(j-i) for i,j in zip(current , threshold)])
    print("Standard Deviation of sample is % s " 
                % (std))
    if d > max_eucl or std*100 > deviation_percentage:
        return True
    return False


if __name__ == "__main__":
    # Load a image
    image_file = 'data/child/ch_1.png'
    #image_file = 'data/seat/seat_1.png'
    image = load_image(image_file, issave)
    print(findedges(image, image_file, issave))
