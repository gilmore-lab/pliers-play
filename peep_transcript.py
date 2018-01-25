# peep_transcript.py
import imageio
imageio.plugins.ffmpeg.download()
import speech_recognition
from pliers.converters import IBMSpeechAPIConverter

snd_0 = 'snd/peep-I-neu-chk.wav'
snd_1 = 'snd/peep-I-hap-tlk.wav'
snds = [snd_0, snd_1] 

ext = IBMSpeechAPIConverter()

result = ext.transform(snds[0])

print("Words in " + snds[0])
print("Onset" +"\t" + "Dur (s)" + "\t" + "Word")
for ts in result:
    print(str(ts.onset) + "\t" + str(ts.duration) + "\t" + ts.text)

result = ext.transform(snds[1])

print("Words in " + snds[1])
print("Onset" +"\t" + "Dur (s)" + "\t" + "Word")
for ts in result:
    print(str(ts.onset) + "\t" + str(ts.duration) + "\t" + ts.text)
