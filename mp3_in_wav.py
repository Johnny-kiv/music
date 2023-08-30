from pydub import AudioSegment
sound = AudioSegment.from_mp3("noty-do.mp3")
sound.export('noty-do.wav', format="wav")