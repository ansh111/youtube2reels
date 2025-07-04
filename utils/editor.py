import ffmpeg
import os

def cut_clips(input_file, clips):
    output_files = []
    for i, clip in enumerate(clips):
        
        start = float(clip['start'])
        end = float(clip['end'])
        duration = end- start
        print(f"anshul:{duration}")
        out_path = f"static/clip_{i}.mp4"

        ffmpeg.input(input_file, ss=start, t=duration) \
              .filter('scale', 720, 1280) \
              .output(out_path) \
              .overwrite_output() \
              .run()

        output_files.append(out_path)
    return output_files

