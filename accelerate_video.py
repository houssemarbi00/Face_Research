import face_recognition
import cv2
import os
import glob
import numpy as np

from moviepy.editor import VideoFileClip

def accelarate(video_path):
    # ouvrir la vidéo
    clip = VideoFileClip(video_path)

    # définir le facteur d'accélération de la lecture
    acceleration_factor = 10

    # accélérer la vidéo
    new_clip = clip.speedx(acceleration_factor)

    path=os.getcwd()
    # enregistrer la vidéo accélérée dans un fichier
    new_clip.write_videofile(f"{path}/video_accelerated.mp4")    