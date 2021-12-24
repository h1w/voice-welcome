import wave

def ConvertPcmToWav(name, output_name):
    with open(name, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    
    with wave.open(output_name, 'wb') as wavfile:
        wavfile.setparams((1, 2, 44100, 1, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)