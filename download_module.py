#In this module I create the logic for download music or videos in the best quality

from pytube import YouTube
import os

def download():
	#I prepare the path to where to save the music or videos
	down = input("Do you want to download, Music or Videos?: ")
	if down.lower() == "music":
			path = "/home/alex/Música"
	else:
		path = "/home/alex/Vídeos"

	if not os.path.exists(path):
		print(f"The directory {path} doesn´t exist. Creating it now.\n")
		os.makedirs(path)

	#Now, i make the logic for the download the url
	url = input("Please enter the url the video or music do you want download: ")
	try:
		yt = YouTube(url)

		if down.lower() == "music":
			audio = yt.streams.filter(only_audio=True).first()
			audio.download(path)
			print("Your music is ready to listen!!\n")
		else:
			video = yt.streams.get_highest_resolution()
			video.download(path)
			print("Your video is ready to watch!!\n")
	except Exception as e:
		print(f"An error ocurred: {e}")



