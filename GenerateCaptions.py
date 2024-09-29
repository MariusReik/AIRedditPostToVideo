import moviepy.editor as mp

def create_video_with_captions(voiceover_file, captions, background_video="Background.mp4", output_file="output_video.mp4"):
    # Load background video
    background = mp.VideoFileClip(background_video)

    # Load audio
    audio = mp.AudioFileClip(voiceover_file)
    
    # Add captions dynamically based on text timing
    caption_clips = []
    for i, caption in enumerate(captions):
        txt_clip = (mp.TextClip(caption, fontsize=50, color='white')
                    .set_position('bottom')
                    .set_duration(2)  # Set duration for each caption
                    .set_start(i * 2))  # Timing offset for captions
        caption_clips.append(txt_clip)

    # Combine everything into a final video
    video = mp.CompositeVideoClip([background] + caption_clips).set_audio(audio)

    # Export final video
    video.write_videofile(output_file, fps=24)
