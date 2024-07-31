import face_recognition
import os
import cv2
import numpy as np

print("Imports successful")

path = os.getcwd() + "/server/Faces"
print("Path:", path)

# Check if the directory exists
if os.path.exists(path):
    print("Directory exists")
else:
    print("Directory does not exist")
#this file is for checking whether all the libraries and packages are installed correctly or not.
