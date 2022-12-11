## Audio to Sheet Music 🎵

### Takes in a .mp3, .wav, or .aiff and returns sheet music

This file combines and modifies [sound_to_midi](https://github.com/tiagoft/audio_to_midi) and [midi2piano](https://github.com/tgstation/tgstation/blob/master/tools/midi2piano/midi2piano.py). Both of which are under a GENERAL PUBLIC LICENSE which permits copying, distributing and modifying.


**Command**
```
    python3 main.py inputfile.mp3
```

Optionally, add tag -k to save the generated midi files to the saved_midi_files folder
```
    python3 main.py inputfile.mp3 -k
```

Output will print to console and to music_sheets.txt