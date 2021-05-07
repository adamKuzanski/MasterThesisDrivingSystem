#%% Import libraries
import numpy as np
import camera_calibration as cc
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

input_path = '../input_videos/'
level = 0   # easy
# level = 1 # medium
# level = 2 # hard

#%% Step One - Calibrate the camera
camera = cc.Camera()
mtx, dist = camera.calibrateCamera()
# %% Step Two - Read the input movie
def setInputPath(level):
    if level == 0:
        input_path += 'easy.mp4'
    elif level == 1:
        input_path += 'medium.mp4'
    elif level == 2:
        input_path += 'hard.mp4'
# %%
