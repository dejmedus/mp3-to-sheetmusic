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
        # results = midi_to_music_sheet(midi, filename)
        # results = {
        #     'date': 'date',
        #     'name': 'output_name',
        #     'sheet_music': 'sdhjdfhjdskfhdsu'
        # }
        # os.remove(os.path.join(
        #     ['UPLOAD_FOLDER'], filename))

        # return render_template('app.html', date=results['date'], name=results['name'], sheet_music=results['sheet_music'])

    return render_template('app.html', sheet_music='false')

