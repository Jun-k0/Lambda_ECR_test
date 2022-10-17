# -*- coding: utf-8 -*-
import speech_recognition as sr
import librosa
from posixpath import split
from playsound import playsound
import wave
import time
import keyboard
import sys
import io
import pyaudio


FORMAT = pyaudio.paInt16

CHANNELS = 1

RATE = 16000

CHUNK = 1024

RECORD_SECONDS = 10

WAVE_OUTPUT_FILENAME = "file.wav"
#"C:/Users/jayoo/OneDrive/문서/소리 녹음/file.wav"

def habit_word():

    audio = pyaudio.PyAudio()


    # start Recording

    stream = audio.open(format=pyaudio.paInt16,

                        channels=CHANNELS,

                        rate=RATE,

                        input=True,

                        input_device_index=1,

                        frames_per_buffer=CHUNK)

    print("recording...")
    frames = []
    k = 0

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        if keyboard.is_pressed('space'):
            break
        data = stream.read(CHUNK)

        frames.append(data)


    print("finished recording")


    # stop Recording

    stream.stop_stream()

    stream.close()

    audio.terminate()


    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')

    waveFile.setnchannels(CHANNELS)

    waveFile.setsampwidth(audio.get_sample_size(FORMAT))

    waveFile.setframerate(RATE)

    waveFile.writeframes(b''.join(frames))

    waveFile.close()

    time.sleep(3)

    r = sr.Recognizer()

    sample_wav, rate = librosa.core.load(
        "file.wav")

    korean_audio = sr.AudioFile(
        "file.wav")

    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

    with korean_audio as source:
        audio = r.record(source)
    num = r.recognize_google(audio_data=audio, language='ko-KR')

    print(num)
    print(len(num))

    wav, sr = librosa.load("file.wav", sr=16000)
    print('sr:', sr)
    print('wav shape:', wav.shape)
    print('length:', wav.shape[0]/float(sr), 'secs')

    print(num)
    temp = num.split(' ')

    word = ['아', '아니', '그', '음']

    for i in range(len(word)):
        print(word[i], ":", temp.count(word[i]))

    return temp
