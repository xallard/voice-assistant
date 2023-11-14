# audio_capture.py
# Script for capturing audio input using PyAudio in VoiceAssistantAI

# For the VoiceAssistantAI project, we can create a fictitious Python script that incorporates PyAudio for audio capture and processing. This script, which might be named audio_capture.py, will focus on capturing user speech through a microphone and converting it into a format suitable for further processing like speech recognition. This file would ideally be part of the speech-recognition application within the project.

# File Location:
# /voice-assistant/apps/speech-recognition/audio_capture.py

# Content of audio_capture.py:

import pyaudio
import wave

class AudioCapture:
    def __init__(self, format=pyaudio.paInt16, channels=1, rate=44100, chunk=1024):
        self.format = format
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.pyaudio_instance = pyaudio.PyAudio()

    def record(self, duration=5, output_filename="output.wav"):
        """
        Record audio from the microphone and save it to a file.
        """
        stream = self.pyaudio_instance.open(format=self.format, channels=self.channels,
                                            rate=self.rate, input=True,
                                            frames_per_buffer=self.chunk)
        print("Recording...")

        frames = []

        for _ in range(int(self.rate / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(data)

        print("Recording finished.")

        stream.stop_stream()
        stream.close()
        self.pyaudio_instance.terminate()

        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.pyaudio_instance.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))
        print(f"File saved: {output_filename}")

    def play_audio(self, filename):
        """
        Play an audio file.
        """
        wf = wave.open(filename, 'rb')
        stream = self.pyaudio_instance.open(format=self.pyaudio_instance.get_format_from_width(wf.getsampwidth()),
                                            channels=wf.getnchannels(),
                                            rate=wf.getframerate(),
                                            output=True)

        data = wf.readframes(self.chunk)
        while data:
            stream.write(data)
            data = wf.readframes(self.chunk)

        stream.stop_stream()
        stream.close()
        wf.close()
        print(f"Finished playing: {filename}")

# Example usage
if __name__ == "__main__":
    audio_capture = AudioCapture()
    audio_capture.record(duration=10, output_filename="user_input.wav")
    audio_capture.play_audio("user_input.wav")

# In this script:

# An AudioCapture class is defined, handling audio recording and playback functionalities.
# The record method captures audio input from the microphone and saves it as a WAV file.
# The play_audio method plays back the recorded audio file.
# PyAudio is used for managing audio streams, both input (microphone) and output (speakers).
# This example includes basic functionalities and can be extended or integrated with speech recognition and other components of the voice assistant.
# This script, as part of the speech-recognition module in the VoiceAssistantAI project, would serve as a foundational component in enabling the voice assistant to interact with users through speech.
