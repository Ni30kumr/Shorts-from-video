from video_download import download_youtube_video
from extract_audio import extracted_audio
from transcribe import transcript
from gem import ai_analysis
from final_video import process_video_clips
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Add the vocal_remover directory to the Python path
sys.path.append(r'C:\\Users\\Dell\\SHL2\\vocal_remover')

from inference import separate_vocals_and_instruments


def full_pipeline(url,name):
    download_youtube_video(url, name)
    extracted_audio(name)
    separate_vocals_and_instruments(name)
    transcript(name)
    ai_analysis(name)
    process_video_clips(name)
    
