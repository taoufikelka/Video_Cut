# Video_Cut
A python script that help cutting a long video or movie into small parts.

usage: video_cut.py [-h] [-mn MOVIENAME] [-fp FILEPATH] [-pn [PARTSNUMBER]]

Cutting mp4 videos/movies to parts.

optional arguments:
  -h, --help            show this help message and exit
  -mn MOVIENAME, --MovieName MOVIENAME
                        Video or Movie title
  -fp FILEPATH, --FilePath FILEPATH
                        Path to .mp4 video file
  -pn [PARTSNUMBER], --PartsNumber [PARTSNUMBER]
                        Number of parts, by default it will calculate it
                        automatically (each part will be 60Mb)
