import wave

wr = wave.open('Imagine_Dragons_-_Believer_74640917.mp3', 'r')
# Set the parameters for the output file.
par = list(wr.getparams())
par[3] = 0  # The number of samples will be set by writeframes.
par = tuple(par)
ww = wave.open('pitch1.wav', 'w')
ww.setparams(par)