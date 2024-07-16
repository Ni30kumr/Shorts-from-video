import moviepy.editor as mp

def extracted_audio(name):
    """
    Extract audio from a video file and save it to a specified location.
    
    :param video_path: str, path to the input video file
    :param output_path: str, path where the extracted audio will be saved
    """
    try:
        # Load the video file
        video = mp.VideoFileClip(f"{name}/original.mp4")
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to the specified output path
        audio.write_audiofile(f"{name}/audio.mp3")
        
        # Close the video to release resources
        video.close()
        
        print(f"Audio extracted successfully and saved to audio.mp3")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
# extracted_audio("pawan")