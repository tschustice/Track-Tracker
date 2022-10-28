import pandas as pd
from prettytable import PrettyTable
import os.path
import csv

def minutes_seconds_separator(minutes_seconds):
    minutes = minutes_seconds // 1
    minutes = int(minutes)

    seconds = round(minutes_seconds % 1,2)
    seconds = int(seconds*100)


    return minutes, seconds

def time_per_track (asphalt_track_field, asphalt_track_forest, dirt_track_field, dirt_track_forest):
    '''Calculates the total duration of the run as well as the time on each track'''
    img_per_minute = 10/60
    length = len(asphalt_track_field) + len(asphalt_track_forest) + len(dirt_track_field) + len(dirt_track_forest)

    #Total time
    total_time = round(img_per_minute*length,1)

    #Time on asphalt field track
    asphalt_field_time = round(img_per_minute*len(asphalt_track_field),1)

    #Time on asphalt forest track
    asphalt_forest_time = round(img_per_minute*len(asphalt_track_forest),1)

    # Time on dirt field track
    dirt_field_time = round(img_per_minute*len(dirt_track_field),1)

    # Time on dirt forest track
    dirt_forest_time = round(img_per_minute*len(dirt_track_forest),1)

    return asphalt_field_time, asphalt_forest_time, dirt_field_time, dirt_forest_time, total_time



def distance_per_track(minutes, seconds, asphalt_field_time, asphalt_forest_time, dirt_field_time, dirt_forest_time, total_time):
    '''Calculates the total duration of the run as well as the time on each track'''
    time = seconds/60+ minutes

    total_distance= round(total_time/time,1)

    asphalt_field_distance = round(asphalt_field_time/time,1)

    asphalt_forest_distance = round(asphalt_forest_time/time,1)

    dirt_field_distance = round(dirt_field_time/time,1)

    dirt_forest_distance = round(dirt_forest_time/time,1)

    asphalt_track_ratio = round((asphalt_field_distance+asphalt_forest_distance)/total_distance,2)

    field_track_ratio = round((dirt_field_distance+asphalt_field_distance)/total_distance,2)

    return asphalt_field_distance, asphalt_forest_distance, dirt_field_distance, dirt_forest_distance, total_distance, asphalt_track_ratio, field_track_ratio


def output(minutes_seconds, asphalt_field_time, asphalt_forest_time, dirt_field_time, dirt_forest_time, total_time, asphalt_field_distance, asphalt_forest_distance, dirt_field_distance, dirt_forest_distance, total_distance, asphalt_track_ratio, field_track_ratio):

    print('\x1b[6;30;42m' + 'Congratulations! Your activity has been tracked. Well done!' + '\x1b[0m')
    tt = PrettyTable(['', 'Total Time (in min)', 'Total Distance (in km)', 'Pace', 'Asphalt Track Ratio', 'Field Track Ratio'])
    tt.add_row(['Total', total_time, total_distance, minutes_seconds, asphalt_track_ratio, field_track_ratio])
    print(tt)
    #print(f'You have run in total {total_distance} km in {total_time} minutes!')
    print(f'Your run went along the following tracks:')

    t = PrettyTable(['Track', 'Time (in min)', 'Distance (in km)'])
    t.add_row(['Asphalt Forest Track', asphalt_forest_time, asphalt_forest_distance])
    t.add_row(['Asphalt Field Track', asphalt_field_time, asphalt_field_distance])
    t.add_row(['Dirt Forest Track', dirt_forest_time, dirt_forest_distance])
    t.add_row(['Dirt Field Track', dirt_field_time, dirt_field_distance])
    print(t)

    return

def create_csv():
    file_exists = os.path.exists('running_summary.csv')
    if file_exists == False:
        with open('running_summary.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["date", "total_time", "total_distance", "Pace", "ATR", "FTR", "asphalt_forest_time", "asphalt_forest_distance", "asphalt_field_time", "asphalt_field_distance", "dirt_field_time", "dirt_field_distance", "dirt_forest_time", "dirt_forest_distance"])
    else:
        pass

def append_running_summary(asphalt_forest_time, asphalt_forest_distance, asphalt_field_time, asphalt_field_distance, dirt_field_time, dirt_field_distance, dirt_forest_time, dirt_forest_distance, total_time, total_distance, minutes, seconds, date, minutes_seconds, asphalt_track_ratio, field_track_ratio):
    add =[date, total_time, total_distance, minutes_seconds, asphalt_track_ratio, field_track_ratio, asphalt_forest_time, asphalt_forest_distance, asphalt_field_time, asphalt_field_distance, dirt_field_time, dirt_field_distance, dirt_forest_time, dirt_forest_distance]
    with open('running_summary.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(add)
