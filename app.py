from flask import Flask, request, render_template, redirect, url_for
import os
import ffmpeg
import whisper

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Load the Whisper model
model = whisper.load_model("base")  # You can choose different sizes: tiny, base, small, medium, large

def extract_audio(video_path, audio_path):
    try:
        (
            ffmpeg
            .input(video_path)
            .output(audio_path)
            .run(overwrite_output=True)
        )
    except ffmpeg.Error as e:
        print(e)
        raise

def speech_to_text(audio_path, language="ar"):
    result = model.transcribe(audio_path, language=language)
    return result['text']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'video' not in request.files:
            return redirect(request.url)
        file = request.files['video']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            audio_path = os.path.join(app.config['UPLOAD_FOLDER'], "extracted_audio.wav")
            
            try:
                extract_audio(file_path, audio_path)
                transcription = speech_to_text(audio_path)
            except Exception as e:
                return str(e)
            
            return render_template('index.html', transcription=transcription)
    return render_template('index.html', transcription='')

if __name__ == '__main__':
    app.run(debug=True)
