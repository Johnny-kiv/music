from pydub import AudioSegment

audio_file = AudioSegment.from_file("ACDC_-_Back_In_Black_47830042.mp3", format="mp3")
lowered_audio = audio_file._spawn(audio_file.raw_data, overrides={"frame_rate": audio_file.frame_rate + 14000})
lowered_audio.export("output.mp3", format="mp3")