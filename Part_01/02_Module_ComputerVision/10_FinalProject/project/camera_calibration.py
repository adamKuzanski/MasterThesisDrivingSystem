#%% import libraries
import glob
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2

class Camera():
    def __init__(self):
        self.images_path = glob.glob('../camera_calibration/calibration*.jpg')
        self.chessboard_corners_x = 9
        self.chessboard_corners_y = 6
        self.images_shape = None

        #Calibration coefficients
        self.ret = 0
        self.mtx = 0
        self.dist = 0
        self.rvecs = 0
        self.tvecs = 0
    
    def _getRealPoints(self):
        points = np.zeros( (self.chessboard_corners_x * self.chessboard_corners_y, 3), np.float32)
        points[:, :2] = np.mgrid[ 0:self.chessboard_corners_x, 0:self.chessboard_corners_y].T.reshape(-1, 2)
        return points
    
    def _findCorners(self, real_p, obj_p, img_p):
        for index, filename in enumerate(self.images_path):
            image = mpimg.imread(filename)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            if index == 0:
                self.images_shape = gray_image.shape[::-1]

            ret, corners = cv2.findChessboardCorners(
                gray_image, 
                (self.chessboard_corners_x, self.chessboard_corners_y),
                None)
            
            if ret == True:
                obj_p.append(real_p)
                img_p.append(corners)
    

    def _performCalibration(self, obj_p, img_p):
        self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv2.calibrateCamera(
            obj_p, img_p, self.images_shape, None, None)

    def calibrateCamera(self):
        raw_object_points, raw_image_points = [], []

        real_points = self._getRealPoints()
        self._findCorners(real_points, raw_object_points, raw_image_points)
        self._performCalibration(raw_object_points, raw_image_points)

        return self.mtx, self.dist

    def undistortImage(self, img):
        return cv2.undistort(img, self.mtx, self.dist, None, self.mtx)
    
    def testUndistortion(self):
        # Visualize undistortion
        image = mpimg.imread('../camera_calibration/calibration1.jpg')
        undistorted = self.undistortImage(image)
        f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20,10))
        ax1.imshow(image)
        ax1.set_title('Original Image', fontsize=30)
        ax2.imshow(undistorted)
        ax2.set_title('Undistorted Image', fontsize=30)




        



        
    
   





        

    




# %%
