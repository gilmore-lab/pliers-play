# test pydub conversion

from pydub import AudioSegment

snd = 'snd/peep-I-hap-tlk.mp3'

song = AudioSegment.from_mp3(snd)

song.export("test.wav", format="wav")