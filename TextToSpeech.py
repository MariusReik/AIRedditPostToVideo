from gtts import gTTS
import os

def text_to_speech(text, output_file="voiceover.mp3"):
    tts = gTTS(text)
    tts.save(output_file)
    return output_file
