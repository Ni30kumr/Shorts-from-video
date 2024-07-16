# YouTube Shorts Generator from Podcast

Aim: Develop an ML system that automatically generates engaging and informative YouTube Shorts from a 30-minute video podcast. The generated Shorts should effectively capture the key points and insights discussed in the original podcast.

## Setup Instructions

1. Create a virtual environment:
2.Install required libraries:using command "pip install -r requirements.txt.\n
3. Gather API keys:
- Google Gemini API
- Assembly API
Replace them in the `.env` file

4. Update file paths:
In the Python file, change the following paths according to your needs:
- Line 126
- Line 127
- Line 160
- Line 165

File: `C:\Users\Dell\SHL2\vocal_remover\inference.py`

NOTE: For more details, visit [this repository](https://github.com/tsurumeso/vocal-remover.git)

5. Run the pipeline:
Execute `pipeline.py` by calling `full_pipeline()` and passing a random name as an argument.

## Demo

Open the folder named "pawan". You will find all components of the pipeline and the final output with names like `video1`, `video2`, etc.
