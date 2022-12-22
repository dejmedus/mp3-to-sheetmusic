# -*- coding: utf-8 -*-
from audio_to_midi.monophonic import wave_to_midi
import librosa

def create_file_name(file_path):
    index = file_path.rfind('.')
    file_path = file_path[:index]
    file_path = f'{file_path[:index]}.mid'
    return file_path


def audio_to_midi(file_input):
    file_out = create_file_name(file_input)

    audio_data, srate = librosa.load(file_input, sr=None)

    midi = wave_to_midi(audio_data, srate=srate)
    
    # midi.save(os.path.join('uploads', file_input))
    with open(file_out, 'wb') as file:
        midi.writeFile(file)
    return file_out
    # return midi
