# Reddit to Video AI

## Overview
This project is designed for fun and learning, exploring the potential of AI technology in generating engaging YouTube Shorts and TikTok videos. It leverages the Reddit API to fetch the top posts from specified subreddits within the last 24 hours, converts the content into audio using Google Text-to-Speech (TTS), and combines the audio with captions over a pre-recorded background video. The result is a polished video file ready for sharing.

## How It Works
The process is broken down into several key modules:

1. **Top Reddit Posts API**  
   Fetches the top posts from selected subreddits.

2. **Text Preprocessing Module**  
   Cleans and prepares the fetched text for further processing.

3. **Text-to-Speech Generation**  
   Converts the cleaned text into speech using the TTS API.

4. **Video Creation**  
   Combines the voiceover with captions using MoviePy or FFmpeg.

5. **Export as Video**  
   Saves the final video in a format suitable for TikTok or YouTube Shorts.

6. **Automate Posting**  
   Plans to automate the posting of generated videos to TikTok and YouTube Shorts.


## Usage
- Create a `.env` file with your Reddit API credentials.
- Generate your own background video and add it to the project.
- Run the main script:
  ```bash
  python main.py
  ```
