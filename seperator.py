import imageio
import moviepy.editor
from moviepy.video.VideoClip import VideoClip
import os
from pydub import AudioSegment
import wave
import threading
from text_analysis import *
from speech_emotion import *

def reducequality():
    sound = AudioSegment.from_wav("audio/converted.wav")
    sound = sound.set_channels(1)
    sound.export("audio/convertednew.wav", format="wav")


def covertingfile():
    video1=moviepy.editor.VideoFileClip("new.mp4")
    audio=video1.audio
    audio.write_audiofile("audio/converted.wav")
    video2=moviepy.editor.VideoFileClip("new.mp4")
    clip = video2.without_audio()
    clip.write_videofile("video/converted.mp4")


def main():
    covertingfile()
    reducequality()
    
    t1 = threading.Thread(target=speech_to_text , )
    t2 = threading.Thread(target=,)
    t1.start()
    t2.start()
    
    t1.join()    
    t2.join()


main()
