import os
os.environ['IMAGEMAGICK_BINARY'] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

from FetchReddit import get_top_post  # Import the function to get Reddit posts
from TextToSpeech import text_to_speech  # Import the TTS function
from GenerateCaptions import create_video_with_captions  # Import video creation function

def generate_tiktok_video(subreddit):
    # Fetch Reddit post
    title, selftext = get_top_post(subreddit)
    
    # Convert Reddit post to voiceover
    voiceover_file = text_to_speech(title + " " + selftext)
    
    # Split the text for captions
    captions = (title + " " + selftext).split('. ')  # Simplified caption splitting

    # Create an output directory if it doesn't exist
    output_dir = "output_videos"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create video with captions and voiceover
    output_file = os.path.join(output_dir, f"{subreddit}_{title[:10]}.mp4")  # Use a unique name for each video
    create_video_with_captions(voiceover_file, captions, background_video="background.mp4", output_file=output_file)
    
    print(f"Video generated successfully: {output_file}")

# Call the function for each subreddit
if __name__ == "__main__":
    for subreddit in ['AmItheAsshole', 'relationship_advice']:
        generate_tiktok_video(subreddit)
