A python script that help cutting a long video or movie into small parts. If number of parts isn't defined, the script will automaticlly define one based on parts with the size of 60Mb for each part.

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
  -z [yes/y or no/n], --Zip [yes/y or no/n]
                        Compress every part to zip, values can be (yes/y) or (no/n), by default it's No.
