# -*- coding: utf-8 -*-
import librosa
from sound_to_midi.monophonic import wave_to_midi


def check_audio_file(file_path):
    if file_path.endswith('.mp3') | file_path.endswith('.wav') | file_path.endswith('.aiff'):
        return file_path
    else:
        print('Filetype must be a .mp3, .wav, or .aiff')
        return None


def create_file_name(file_path):
 # output file is original file without path,
 # saved in the 'saved midi files' folder
 # with the .mid filetype
    index = file_path.rfind('/')
    file_path = file_path[index + 1:]
    index = file_path.rfind('.')
    file_path = file_path[:index]
    file_path = f'saved_midi_files/{file_path[:index]}.mid'
    return file_path


def audio_to_midi(file_input):
    check_audio_file(file_input)
    print("Input file looks okay. Starting...")

    file_in = file_input
    file_out = create_file_name(file_input)

    audio_data, srate = librosa.load(file_in, sr=None)
    print("Audio file loaded. Please wait while the audio file is converted. This may take a while.")
    midi = wave_to_midi(audio_data, srate=srate)
    with open(file_out, 'wb') as file:
        midi.writeFile(file)
    return file_out
