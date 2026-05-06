from moviepy import ImageClip, AudioFileClip, VideoClip, CompositeVideoClip, ColorClip, concatenate_videoclips
import os

# Paths
avatar_path = r"C:\Users\PC\.gemini\antigravity\brain\d6a2a901-3811-45d7-9968-57b02d56dc59\marco_villagran_presenter_1778051760777.png"
audio_path = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_section1_gtts.mp3"
slides_dir = r"c:\proyectos\vitaminas\scratch\slides"
output_path = r"c:\proyectos\vitaminas\Magnesio citrato y glicinato\n8n_output\08_masterclass_section1_demo.mp4"

# Load audio to get duration
audio = AudioFileClip(audio_path)
duration = audio.duration

# 1. Background
bg = ColorClip(size=(1920, 1080), color=(26, 26, 46)).with_duration(duration)

# 2. Avatar (Left 1/3)
# Resize avatar to width 640, keeping aspect ratio
avatar = ImageClip(avatar_path).with_duration(duration).resized(width=640)
avatar = avatar.with_position((0, "center"))

# 3. Slides (Right 2/3)
# We'll cycle 3 slides
slide_files = [os.path.join(slides_dir, f"slide{i}.png") for i in [1, 2, 3]]
slide_duration = duration / len(slide_files)

slide_clips = []
for i, sf in enumerate(slide_files):
    sc = ImageClip(sf).with_duration(slide_duration).resized(width=1280)
    sc = sc.with_position((640, "center"))
    slide_clips.append(sc)

all_slides = concatenate_videoclips(slide_clips)

# 4. Final Composition
final_video = CompositeVideoClip([bg, avatar, all_slides])
final_video = final_video.with_audio(audio)

# Write file
# We use a lower bitrate/fps for the demo to save time
final_video.write_videofile(output_path, fps=10, codec="libx264", audio_codec="aac")

print(f"Video saved to {output_path}")
