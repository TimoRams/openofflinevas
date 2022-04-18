"""Test Vosk microphone."""
import json
import os
import sys

import pyaudio
import pyttsx3

from vosk import KaldiRecognizer
from vosk import Model
import command_handler.command_handler as command

prefix='q '

engine = pyttsx3.init()

if not os.path.exists("model"):
    print("Please download the model and unpack as 'model' in the current folder.")
    sys.exit()


MODEL = Model("model")
REC = KaldiRecognizer(MODEL, 16000)

P = pyaudio.PyAudio()
STREAM = P.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=8000)
STREAM.start_stream()

while True:
    DATA = STREAM.read(14000)
    if len(DATA) == 0:
        pass
    if REC.AcceptWaveform(DATA):
        KIRA_RESULT = REC.Result()
        KIRA_PARSED_JSON = json.loads(KIRA_RESULT)
        wval = KIRA_PARSED_JSON['text']
        print(wval)
        if wval == "":
            wval = ""
        elif (" ") + prefix in (" " + wval + " "):
            before, sep, after = wval.partition(prefix)
            if len(after) > 0:
                wval = after
            x = wval.replace(prefix, "")
            print(x)
            oput = command.h(x)
            engine.say(oput)
            engine.runAndWait()