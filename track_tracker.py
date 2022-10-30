#from datetime import timedelta
import cv2
#import numpy as np
import os

from img_processing import format_timedelta, get_saving_frames_durations, main, resize_aspect_fit, delete_folders
from CNN import prediction, img_per_track
from running_stats import minutes_seconds_separator, time_per_track, distance_per_track, output, create_csv, append_running_summary



def question():
    answer = input("Do you want to see your total results? (yes or no): ")
    if answer == "yes":
        os.system("python -m streamlit run track_tracker_app.py")
        #exec(open("./filename").read()) track_tracker_app.py
        #print("Please see the following link:")
    elif answer == "no":
        print("See you next time!")



if __name__ == "__main__":
    import sys
    video_file = input('Enter the name of the video file here: ')
    minutes_seconds = float(input('Enter your average pace per km here (minutes.seconds): '))
    date = input('Enter the date of the run here (dd/mm/yyyy): ')

    #seconds = int(input('enter the avg seconds here: '))
    #video_file = sys.argv[1]
    #minutes_seconds = 5.30

    #date ='12/12/1212'
    main(video_file)
    new_path, new_path_folder, path = resize_aspect_fit(video_file)
    ypred = prediction(video_file)
    asphalt_track_field, asphalt_track_forest, dirt_track_field, dirt_track_forest = img_per_track(ypred)
    minutes, seconds = minutes_seconds_separator(minutes_seconds)
    asphalt_field_time, asphalt_forest_time, dirt_field_time, dirt_forest_time, total_time = time_per_track (asphalt_track_field, asphalt_track_forest, dirt_track_field, dirt_track_forest)
    asphalt_field_distance, asphalt_forest_distance, dirt_field_distance, dirt_forest_distance, total_distance, asphalt_track_ratio, forest_track_ratio = distance_per_track(minutes, seconds, asphalt_field_time, asphalt_forest_time, dirt_field_time, dirt_forest_time, total_time)
    output(minutes_seconds, asphalt_field_time, asphalt_forest_time, dirt_field_time, dirt_forest_time, total_time, asphalt_field_distance, asphalt_forest_distance, dirt_field_distance, dirt_forest_distance, total_distance, asphalt_track_ratio, forest_track_ratio)
    create_csv()
    append_running_summary(asphalt_forest_time, asphalt_forest_distance, asphalt_field_time, asphalt_field_distance, dirt_field_time, dirt_field_distance, dirt_forest_time, dirt_forest_distance, total_time, total_distance, minutes, seconds, date, minutes_seconds, asphalt_track_ratio, forest_track_ratio)
    delete_folders(path, new_path)
    question()
