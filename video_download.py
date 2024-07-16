from pytube import YouTube
import os

def download_youtube_video(url, name):
    """
    Download a YouTube video given its URL.
    
    :param url: str, the URL of the YouTube video
    :param output_path: str, the directory where the video will be saved (default is current directory)
    :return: str, the path of the downloaded video file
    """
    try:
        # Create a YouTube object
        yt = YouTube(url)
        
        # Get the highest resolution progressive stream
        stream = yt.streams.get_highest_resolution()
        
        # Get the video title (to use as filename)
        title = yt.title
        
        # Remove characters that are invalid for filenames
        filename = "".join([c for c in title if c.isalpha() or c.isdigit() or c==' ']).rstrip()
        
        # Download the video
        print(f"Downloading: {filename}")
        output_path=name
        output_file = stream.download(output_path=output_path, filename='original'+'.mp4')
        
        print(f"Download complete: {output_file}")
        return output_file
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage:
video_path = download_youtube_video('https://youtu.be/BGdrjMzsSlI?si=ihgq9NcNNq36oxRW',"ayush")