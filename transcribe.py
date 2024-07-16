import assemblyai as aai
import os
from dotenv import load_dotenv

load_dotenv()

# Get API key from environment variable
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

# # You can also transcribe a local file by passing in a file path
# FILE_URL = 'C:\\Users\\Dell\\SHL2\\vocal-remover\\audio_Vocals.wav'

# Create a transcriber object
def transcript(name):
    transcriber = aai.Transcriber()

    # Configure transcription options
    config = aai.TranscriptionConfig(
        punctuate=True,
        format_text=True
    )

    # Transcribe the audio file with the specified config
    transcript = transcriber.transcribe(f"{name}/Vocals.wav", config=config)

    if transcript.status == aai.TranscriptStatus.error:
        print(transcript.error)
    else:
        # Open a file to write the transcription
        with open(f'{name}/transcription_5sec.txt', 'w', encoding='utf-8') as f:
            # Get all words with their timestamps
            words = transcript.words

            segment_start = 0
            segment_text = []
            
            for i, word in enumerate(words):
                segment_text.append(word.text)
                
                # If we've reached 30 seconds or it's the last word, write the segment
                if (word.end - segment_start >= 5000) or (i == len(words) - 1):
                    segment_end = word.end
                    line = f"[{segment_start/1000:.2f}s - {segment_end/1000:.2f}s] {' '.join(segment_text)}\n"
                    f.write(line)
                    print(line, end='')  # Also print to console
                    
                    # Reset for next segment
                    segment_start = segment_end
                    segment_text = []

        print("Transcription saved to 'transcription_5sec.txt'")



# transcript("pawan")