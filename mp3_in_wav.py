from pydub import AudioSegment
sound = AudioSegment.from_mp3("/path/to/file.mp3")
sound.export("/output/path/file.wav", format="wav")