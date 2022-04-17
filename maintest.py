"""Test Vosk microphone."""
import json
import os
import sys

import pyaudio

from vosk import KaldiRecognizer
from vosk import Model

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
        print(KIRA_PARSED_JSON['text'])