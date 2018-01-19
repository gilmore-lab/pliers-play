# peep_spectrum.py

from pliers.extractors import STFTAudioExtractor
import matplotlib

snd_0 = 'snd/peep-I-neu-chk.wav'
snd_1 = 'snd/peep-I-hap-tlk.mp3'
snds = [snd_0, snd_1] 

# result will generate spectrogram
ext = STFTAudioExtractor(freq_bins=10, spectrogram=True)

result = ext.transform(snds)

print(result[0])
print(result[1])