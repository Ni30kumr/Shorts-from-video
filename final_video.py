# from moviepy.editor import *
# clip = VideoFileClip("C:/Users/Dell/SHL2/Advanced English Conversation Talking Jobs and Time Off British  American English with subtitles.mp4")
# clip = clip.subclip(10, 25)
# # showing clip
# # clip.ipython_display(width = 360)
# clip.write_videofile("clip.mp4")


import json
from moviepy.editor import VideoFileClip

def process_video_clips(name):
    # Read the JSON file
    with open(f"{name}/key_points.json", 'r') as f:
        timestamps = json.load(f)
    
    # Load the video
    main_clip = VideoFileClip(f"{name}/original.mp4")
    
    # Process each segment
    for i, (segment_name, time_info) in enumerate(timestamps.items(), start=1):
        start_time = time_info['start_time']
        end_time = time_info['end_time']
        
        # Extract the subclip
        subclip = main_clip.subclip(start_time, end_time)
        
        # Generate output filename
        output_filename = f"{name}/video{i}.mp4"
        
        # Write the subclip to a file
        subclip.write_videofile(output_filename)
        
        print(f"Created {output_filename} for segment: {segment_name}")
    
    # Close the main video clip
    main_clip.close()
