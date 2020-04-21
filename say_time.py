from datetime import datetime
import pyaudio
import wave
import time
import os

AUDIOS_DIR_NAME = "audios"


TOP_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIOS_DIR = os.path.join(TOP_DIR, AUDIOS_DIR_NAME)


def play_audio(fname):
    audio_path = os.path.join(AUDIOS_DIR, fname)
    ding_wav = wave.open(audio_path, 'rb')
    ding_data = ding_wav.readframes(ding_wav.getnframes())
    audio = pyaudio.PyAudio()
    stream_out = audio.open(
        format=audio.get_format_from_width(ding_wav.getsampwidth()),
        channels=ding_wav.getnchannels(),
        rate=ding_wav.getframerate(),
        input=False, output=True)
    stream_out.start_stream()
    stream_out.write(ding_data)
    time.sleep(0.2)
    stream_out.stop_stream()
    stream_out.close()
    audio.terminate()


def say_time(obj: datetime = datetime.now()):
    hour = obj.hour % 12 or 12
    play_audio("it's.wav")
    play_audio(f"{hour}.wav")

    if obj.minute == 0:
        play_audio("o'clock.wav")
        return

    if obj.minute < 10:
        play_audio("o.wav")

    play_audio(f"{obj.minute}.wav")
