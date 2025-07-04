import uuid
from utils.downloader import download_video
from utils.transcriber import transcribe
from utils.summerizer import get_highlights
from utils.editor import cut_clips

def process_video(youtube_url: str):
    task_id = str(uuid.uuid4())[:8]
    input_path = f"static/{task_id}_input.mp4"

    download_video(youtube_url, output_path=input_path)
    transcript = transcribe(input_path)
    highlights = get_highlights(transcript)
    clips = cut_clips(input_path, highlights)

    return clips
