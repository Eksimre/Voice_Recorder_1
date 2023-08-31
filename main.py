import sounddevice
from scipy.io.wavfile import write
sr=44100
seconds=5
print("recording\n")
record_voice = sounddevice.rec(sr*seconds,samplerate=sr,channels=2)
sounddevice.wait()
write("mynewfile.wav",sr,record_voice)
print("finished")

print("5 saniyelik kayıt tamamlandı!!!")
