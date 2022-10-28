# Track Tracker
Recognition of video data using a trained convolutional neural network

## Introduction

The Track Tracker application (track_tracker.py) provides extended running statistics for runners. Using recorded video data of one's running activity, the Track Tracker calculates (1) the asphalt ratio and (2) forest ratio of a running activity.

The asphalt ratio gives the percentage of the running activity that was performed on an asphalt track.

The forst ratio gives the percentage of the running activity that was performed in a forest environment. 

A streamlit app can be used to display the total summary of one's running activities on asphalt tracks and forest tracks.

## Technical Set Up

The track_tracker.py is the main file to execute the Track Tracker via terminal. Once executed, it requires to provide the recorded video file name, the average pace of the running activity and the date of the run as input data.

Once the input has been inserted, the Track Tracker performs the following tasks:
(1) Takes every 10 sec a snapshot of the video file,
(2) the size of the snapshots is reduced to a 480x270 format,
(3) each snapshot is classified either as asphalt_track_field, asphalt_track_forest, dirt_track_field or dirt_track_forest,
(4) the asphalt ratio and forest ratio of the running activity are provided as output.

## Output



