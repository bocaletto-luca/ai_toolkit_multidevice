# tasks/transcription.py
import whisper

_model = whisper.load_model("base")

def transcribe(audio_path: str, language: str = "en") -> str:
    """Trascrive il file audio."""
    result = _model.transcribe(audio_path, language=language)
    return result["text"]
