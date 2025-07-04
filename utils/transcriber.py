import whisper

def transcribe(audio_path):
    model = whisper.load_model("base", device="cpu")
    result = model.transcribe(audio_path)
    return result["text"]
