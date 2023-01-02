## Audio to Sheet Music 🎵

### Convert .mp3, .wav, or .aiff to SS13 sheet music

Flask app that modifies and combines the [audio_to_midi](https://github.com/tiagoft/audio_to_midi) and [midi2piano](https://github.com/tgstation/tgstation/tree/master/tools/midi2piano) packages.

More information about SS13 sheet music and its use can be found [here.](https://tgstation13.org/wiki/Songs)

### Local Setup
- fork & clone
- create virtual env
- pip install requirements.txt
- flask run

*example results:*
```python
results = {
    'date': '2023-01-02 14:52:36.523920',
    'name': 'song',
    'sheet_music': """BPM: 200
        F4/0.14,C#4/3,D4,F5/0.67,F4,F#5/1.2,G5/0.05
        E5/1.5,G/3,F#/0.25,G4/2,F#4/1.5,A4/0.67,A#
        A#/1.5,B4/6,Cn5,C#/3,D5/0.55,D/0.55,D6,B/3
        C#/1.5,Cn,A#3/0.6,A#4/3,C/0.75,C/0.01,An3/0.01
        A/0.46,A/0.19,A/0.38,A/0.05,A/0.38,A/0.05
        A/0.08,A/0.01,A/0.01,A/0.05,A/0.01,A/0.27
        A/0.08,A/0.13,A/0.3"""
}```
