# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading
import os
import pyaudio
import wave
import time
import numpy as np
import cv2
import sys
from PIL import ImageGrab
from PIL import Image
import datetime

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 2000000000
WAVE_OUTPUT_FILENAME = "voice.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* recording")

frames = []

def record_video(num): 
    """ 
    function to print cube of given num 
    """
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #you can use other codecs as well.
    #vid = cv2.VideoWriter('record.avi', fourcc, 16, (1920, 1080))
    vid = cv2.VideoWriter('record.avi', fourcc, 19, (1920, 1080))
    while(True):
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        #frame = rescale_frame(frame)
        vid.write(frame)
        cv2.imshow("frame", frame)
        cv2.resizeWindow('frame', 300,300)
        key = cv2.waitKey(1)
        if key == 27:
            break    


    vid.release()
    cv2.destroyAllWindows()
  
def record_audio(num): 
    """ 
    function to print square of given num 
    """
    #os.system('python E:\\Python-Tools\\PyAudioExample.py')


    try:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    except:
        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

  
if __name__ == "__main__":
    a = datetime.datetime.now()
    # creating thread
    flag=True
    t1 = threading.Thread(target=record_video, args=(10,)) 
    t2 = threading.Thread(target=record_audio, args=(10,))
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start()
    
    # wait until thread 1 is completely executed 
    t1.join()
    # wait until thread 2 is completely executed
    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    b = datetime.datetime.now()
    print("Duration : "+str(b-a))
    time.sleep(1)
    os.system('ffmpeg -y -i record.avi -y -i voice.wav -map "0:a? -map "0:a? -c:v copy -c:a copy record_with_audio.avi')
    #os.close()
    # both threads completely executed 
    print("Done!") 
