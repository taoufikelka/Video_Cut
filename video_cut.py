# script to cut mp4 video to parts

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy import editor
import os
import argparse
import pathlib
import math
import zipfile

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'y'):
        return True
    elif v.lower() in ('no', 'n'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def Cut(index, fpath, stime, etime, out, zip):

    outputmp4 = out + ".mp4"
    outputzip = out + ".zip"

    print("\n[+] Part "+str(index+1)+" from "+str(stime)+" to "+str(etime)+" : "+convert_time(etime)+"\n")

    ffmpeg_extract_subclip(fpath, stime, etime, outputmp4)   #create part
    if zip:
        zipObj = zipfile.ZipFile(outputzip, mode='w', compression=zipfile.ZIP_DEFLATED)
        zipObj.write(outputmp4)
        os.remove(outputmp4)
        zipObj.close()

# Arguments
parser = argparse.ArgumentParser(description='Cutting mp4 videos/movies to parts.')

parser.add_argument("-mn","--MovieName", help="Video or Movie title")
parser.add_argument("-fp","--FilePath", help="Path to .mp4 video file", type=pathlib.Path)
parser.add_argument("-pn","--PartsNumber", help="Number of parts, by default it will calculate it automatically (each part will be 60Mb)", type=int, const=0, nargs='?')
parser.add_argument("-z","--Zip", help="Compress the part to zip, values can be (yes/y) or (no/n), by default it's No.", type=str2bool, nargs='?', const=True, default=False)
args = parser.parse_args()

#file variables
filepath = args.FilePath.as_posix()			#path to the file
Movie_name = args.MovieName 				#name of the movie
filename = args.FilePath.name 				#file name
directory = args.FilePath.parent.as_posix()	#the file's parent directory

filesize = args.FilePath.stat().st_size 	#get file size (in bytes)

# if number of parts not set, calculate it automatically (60Mo in each part)
if args.PartsNumber in (None, 0):
	# calculate the number of parts from the size, default part size is 60Mb
	nbrp = filesize // (60*(1024**2))
else:
	nbrp = args.PartsNumber

#creat a directory to store the parts
outputname = directory + "/" + Movie_name+"_parts/"

if not os.path.exists(outputname):
    os.makedirs(outputname)

#read the file
video = editor.VideoFileClip(filepath)

#calculate parameters
start_time = 0
duration = int(video.duration)
step = duration // nbrp
step_size = filesize // nbrp
end_time = step
rest = duration % nbrp

#function to convert time from seconds to hours and minuts
def convert_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    mins = seconds // 60
    seconds %= 60
    return str(hours)+"h "+str(mins)+"min "+str(seconds)+"s"

#function to convert size from bytes to higher scales
def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

#printing
print("             Report   ")
print("----------------------------------")
print("[!] Cutting file : " + filename)
print("[!] File duration : "+convert_time(duration))
print("[!] File size : "+convert_size(filesize))
print("[!] Number of parts : "+str(nbrp))
print("[!] Step duration : "+convert_time(step))
print("[!] Step size : "+convert_size(step_size))
print("[!] Rest : "+convert_time(rest))
print("[!] Compression : ",args.Zip)
print("----------------------------------")
input("Press Enter to continue...")

#start partitioning
print("\n[!] Start\n")

for i in range(nbrp):

    output = outputname + Movie_name + "_part_"+str(i+1)	#set name of the part

    if i < nbrp-1 :
        Cut(i, filepath, start_time, end_time, output, args.Zip)
        start_time = end_time
        end_time += step

    else :
        end_time += rest 	#if it is the last part, it will add the remainder
        Cut(i, filepath, start_time, end_time, output, args.Zip)

print("\n[!] End\n")
