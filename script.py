"""
Created on Mon Jun 10 20:00:31 2024

@author: Dea
"""

from pytube import YouTube

# URL of the YouTube video you want to download
url = 'https://www.youtube.com/watch?v=j3Q0i6zPi4g' 

video1 = YouTube(url)

print(f'Title: {video1.title}')
stream = video1.streams.get_highest_resolution()
stream.download()

print('Download completed!')
