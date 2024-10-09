# 🎙️ Flask Arabic Speech Recognition with Whisper

## Objective
Develop a Flask web application that extracts audio from uploaded videos and converts Arabic speech to text using OpenAI's Whisper model.

## Tools
- **Flask**: Web framework for routing and handling HTTP requests.
- **FFmpeg**: For extracting audio from video files.
- **Whisper (OpenAI)**: For Arabic speech-to-text transcription.
- **HTML**: For rendering the user interface.

## Key Features
- **Real-Time Arabic Transcription**: Converts uploaded video files to text by extracting and transcribing the audio.
- **User-Friendly Interface**: Simple upload interface for submitting video files.
- **Scalable Model Options**: Supports different Whisper model sizes (tiny, base, small, medium, large) for varying performance needs.
- **Seamless Audio Extraction**: Uses FFmpeg to handle video-to-audio conversion for accurate transcription.
