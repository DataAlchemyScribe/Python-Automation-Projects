from pytube import YouTube
from sys import argv

# url variable will hold the link of youtube video which we pass in the arguments in command 
# and the link will be the second argument and so index 1 is given in the argv
url_link = argv[1]

# creating a youtube object
yt_obj = YouTube(url_link)

# temporary
# general info about youtube video which we will be downloading
print("Video Title : ", yt_obj.title)

print("Video Views : ", yt_obj.views)

print("Length of video (in seconds) : ", yt_obj.length)

# downloading the youtube video
yt_video_download = yt_obj.streams.get_highest_resolution()
yt_video_download.download('C:/Devanshu 7-7-20/Education LDRP/4th Year - B.E. IT/Learning Python/Python Automation Projects/youtubeVideoDownloads')