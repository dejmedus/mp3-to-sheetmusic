import os

from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename

from dotenv import load_dotenv

from audio_to_midi.audio2midi import audio_to_midi
from midi_to_sheet_music.midi2piano import midi_to_music_sheet


app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = 'uploads'

# allows files up to 50MB
# mp3 10MB avg, .wav 40MG average
app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000


ALLOWED_EXTENSIONS = {'wav', 'aiff', 'mp3'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('File not found.')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # convert audio to midi
        midi = audio_to_midi(f'uploads/{filename}')
        # convert midi to sheet music
        results = midi_to_music_sheet(midi)
        
        # results = {
        #     'date': 'date',
        #     'name': 'output_name',
        #     'sheet_music': """BPM: 200
        #         F4/0.14,C#4/3,D4,F5/0.67,F4,F#5/1.2,G5/0.05
        #         E5/1.5,G/3,F#/0.25,G4/2,F#4/1.5,A4/0.67,A#
        #         A#/1.5,B4/6,Cn5,C#/3,D5/0.55,D/0.55,D6,B/3
        #         C#/1.5,Cn,A#3/0.6,A#4/3,C/0.75,C/0.01,An3/0.01
        #         A/0.46,A/0.19,A/0.38,A/0.05,A/0.38,A/0.05
        #         A/0.08,A/0.01,A/0.01,A/0.05,A/0.01,A/0.27
        #         A/0.08,A/0.13,A/0.3"""
        # }

        # clear uploads
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template('app.html', date=results['date'], name=results['name'], sheet_music=results['sheet_music'])

    return render_template('app.html', sheet_music='false')

