import google.generativeai as genai
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file (assuming it's in the same directory)
load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])
def ai_analysis(name):
    with open(f'{name}/transcription_5sec.txt', 'r') as file:
        # Read the entire content of the file
        content = file.read()
        
        # Print the content
        # print(content)
        

    model = genai.GenerativeModel('gemini-1.5-pro')

    prompt=prompt=f"""Task: Analyze the audio transcription and identify 10 key points that represent the overall content. Generate a dictionary where each key is a key point and the value is another dictionary containing "start_time" and "end_time" keys corresponding to the timestamp of the key point in the transcription (in seconds).

    {content}

    Output: A dictionary in the following format:
    NOTE: Output should be just dictionary no extra content and difference between start_time and end_time should be 30 seconds in each.
    {{
      \"key_point_1\": {{
        \"start_time\": \"start_time_in_seconds\",
        \"end_time\": \"end_time_in_seconds\"
      }},
      \"key_point_2\": {{
        \"start_time\": \"start_time_in_seconds\",
        \"end_time\": \"end_time_in_seconds\"
      }},
      (up to 10 key points)
    }}"""

    print()

    response = model.generate_content(prompt)
    print(type(response.text))

  # a= json.dumps(response.text)
  # data_string = a[1:-1]  # This removes the first and last characters

  # # Now data_string will contain the desired dictionary format without JSON delimiters
  # print(data_string)


    response_dict = json.loads(response.text)

      # Save dictionary to JSON file
    os.makedirs(name, exist_ok=True)

    file_path = f"{name}/key_points.json"

    # Check if the file exists
    if not os.path.exists(file_path):
        # If it doesn't exist, create an empty JSON file
        with open(file_path, 'w') as outfile:
            json.dump({}, outfile)

    # Now, write the data to the file (whether it existed before or was just created)
    with open(file_path, 'w') as outfile:
        json.dump(response_dict, outfile, indent=4) 
        
# ai_analysis("pawan")