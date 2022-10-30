import cv2
import os
import os.path
import csv
import numpy as np
import pandas as pd
from datetime import timedelta
from PIL import Image
import shutil
# i.e if video of duration 30 seconds, saves 10 frame per second = 300 frames saved in total
SAVING_FRAMES_PER_SECOND = 0.1 # saves one snaphshot every ten seconds


def format_timedelta(td):
    """Utility function to format timedelta objects in (e.g 00:00:20.05)
    omitting microseconds and retaining milliseconds"""
    result = str(td)
    try:
        result, ms = result.split(".")
    except ValueError:
        return result + ".00".replace(":", "-")
    ms = int(ms)
    ms = round(ms / 1e4)
    return f"{result}.{ms:02}".replace(":", "-")


def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s

def main(video_file):
    filename, _ = os.path.splitext(video_file)
    filename += "-opencv"
    #filename_new = "Raw Data"
    # make a folder by the name of the video file
    if not os.path.isdir(filename):
        os.mkdir(filename)
    # read the video file
    cap = cv2.VideoCapture(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # start the loop
    count = 0
    #pbar = tqdm(desc='while')
    while True:
        is_read, frame = cap.read()
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        # get the duration by dividing the frame count by the FPS
        frame_duration = count / fps
        try:
            # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration,
            # then save the frame
            frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
            cv2.imwrite(os.path.join(filename, f"frame{video_file + frame_duration_formatted}.jpg"), frame)
            # drop the duration spot from the list, since this duration spot is already saved
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        # increment the frame count
        count += 1

resize_ratio = 0.25  # where 0.5 is half size, 2 is double size

def resize_aspect_fit(video_file):
    filename, _ = os.path.splitext(video_file)
    #filename += "-opencv"
    path_folder = "/Users/justusweissmuller/Desktop/spiced/FinalProject/finalcode/"
    path = path_folder+filename+"-opencv/"
    dirs = os.listdir(path)
    new_path_folder = "/Users/justusweissmuller/Desktop/spiced/FinalProject/finalcode/"
    new_path = new_path_folder+filename+"-img/"
    os.makedirs(new_path)

    for item in dirs:
        if item.endswith('.jpg'):
            #print(path+item,'Hello')
            #continue
    #if os.path.isfile(path+item):
            image = Image.open(path+item)
            file_path, extension = os.path.splitext(path+item)
            #print(file_path,'Good morning', extension, path, 'Goodbye', item)
            new_file_path, new_extension = os.path.splitext(new_path+item)

            new_image_height = int(image.size[0] / (1/resize_ratio))
            new_image_length = int(image.size[1] / (1/resize_ratio))

            image = image.resize((new_image_height, new_image_length), Image.Resampling.LANCZOS)
            image.save(new_file_path + "_small" + extension, 'JPEG', quality=90)
    return new_path, new_path_folder, path

def delete_folders(path, new_path):
    shutil.rmtree(path)
    shutil.rmtree(new_path)
