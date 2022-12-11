from audio_to_midi.audio2midi import audio_to_midi
from midi_to_sheet_music.midi2piano import midi_to_music_sheet
import sys

audio = sys.argv[1]

keep = False
if len(sys.argv) == 3:
    if sys.argv[2] == '-k':
        keep == True

midi = audio_to_midi(audio)
midi_to_music_sheet(midi, keep)
