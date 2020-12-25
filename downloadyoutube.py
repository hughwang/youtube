from pytube import YouTube

# misc
import os
import shutil
import math
import datetime
from FrameExtractor import FrameExtractor
# plots
#import matplotlib.pyplot as plt
#%matplotlib inline

# image operation
import cv2

# create the instance of the YouTube class
video = YouTube('https://www.youtube.com/watch?v=NqC_1GuY3dw')

# print a summary of the selected video
print('Summary:')
print(f'Title: {video.title}')
print(f'Duration: {video.length / 60:.2f} minutes')
print(f'Rating: {video.rating:.2f}')
print(f'# of views: {video.views}')

result=video.streams.filter(file_extension = "mp4").all()
#video.streams.get_by_itag(18).download()
fe = FrameExtractor('Game Boy Longplay [009] Mega Man Dr Wilys Revenge.mp4')
duration = fe.get_video_duration()
images= fe.get_n_images(every_x_frame=1000)
fe.extract_frames(every_x_frame=1000,
                  img_name='megaman',
                  dest_path='megaman_images')
i=1
#https://github.com/erykml/medium_articles/blob/master/Computer%20Vision/downloading_youtube_videos.ipynb
